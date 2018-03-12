#!/usr/bin/env python3
import struct
import sys
import unittest
from collections import OrderedDict
from os import urandom
from pathlib import Path

try:
	import mujson as json
except ImportError:
	import json


def getTestsDir() -> Path:
	try:
		return Path(__file__).parent.absolute()
	except BaseException:
		return Path(".").absolute() / "tests"


testsDir = getTestsDir()
parentDir = testsDir.parent.absolute()
sys.path.insert(0, str(parentDir))
testModelsDir = testsDir / "models"
modelFileName = "random.model"
modelPath = testModelsDir / modelFileName

dict = OrderedDict


import pyxgboost
import pyxgboost.compiler
from pyxgboost.setuptoolsHelper import pyxgboostHelper


def randomNumbers(count):
	bytes = urandom(count * 4)
	return struct.unpack("f" * count, bytes)


def randomDataset(vectorCount, vectorLen):
	import numpy as np

	return np.random.rand(vectorCount, vectorLen)


# WARNING: with other hyperparams it may choose another path in the tree, need to investigate this
hyperparams = {
	"colsample_bytree": 0.9451615772532829,
	"learning_rate": 0.44981231171492403,
	"max_depth": 22,
	"min_child_weight": 0.07894413336299037,
	"min_split_loss": 0.7796040450315559,
	"num_parallel_tree": 2,
	"reg_alpha": 0.0170901963375754,
	"subsample": 0.9654030894680347
}


def randomModel(vectorCount=1000, vectorLen=100):
	import numpy as np
	import xgboost

	ds = randomDataset(vectorCount, vectorLen)
	targetResult = np.random.rand(vectorCount)
	dm = xgboost.DMatrix(ds, label=targetResult)
	return xgboost.train(hyperparams, dm, 10)


class Tests(unittest.TestCase):
	def setUp(self):
		self.vectorLen = 1000
		vectorCount = 1000
		self.model = randomModel(vectorCount=vectorCount, vectorLen=self.vectorLen)
		testModelsDir.mkdir(exist_ok=True)
		#self.model.save_model(str(modelPath))
		self.modelBinary = self.model.save_raw()

	def tearDown(self):
		#modelPath.unlink()
		pass

	def testHeaderParsing(self):
		from pyxgboost.kaitai.xgboost import Xgboost

		c = json.loads(self.model.save_config())
		m = Xgboost.from_bytes(self.modelBinary)
		p = m.param
		self.assertAlmostEqual(float(c['learner']["learner_model_param"]["base_score"]), p.base_score, delta=sys.float_info.epsilon)
		self.assertEqual(int(c['learner']["learner_model_param"]['num_class']), p.num_class)
		self.assertEqual(int(c['learner']["learner_model_param"]["num_feature"]), p.num_feature)
		self.assertEqual(c['version'][1], p.xgboost_version.minor)
		self.assertEqual(c['version'][0], p.xgboost_version.major)

		self.assertEqual(c['learner']['learner_train_param']['booster'], m.name_gbm_.str)
		self.assertEqual(c['learner']['learner_train_param']['objective'], m.name_obj_.str)

	def testInference(self):
		import numpy as np
		import xgboost

		testVec = randomNumbers(self.vectorLen)
		resXGBoost = self.model.predict(xgboost.DMatrix(np.array([testVec])))[0]

		for useSigmoids, errorThreshold in ((False, 0.0001), (True, 0.001)):
			for useNumPy in (False, True):
				with self.subTest(useSigmoids=useSigmoids):
					with self.subTest(useNumPy=useNumPy):
						regress = pyxgboost.compiler.compile(self.modelBinary, pyxgboost.compiler.OutputType.func, useSigmoids=useSigmoids, useNumPy=useNumPy)
						resPyXGBoost = regress(testVec)[0]

						mean = (resPyXGBoost + resXGBoost) / 2
						diff = np.abs(resPyXGBoost - resXGBoost)
						err = diff / mean
						print(err)
						self.assertTrue(err < errorThreshold)

	def testHelper(self):
		testCfg = {
			"pyxgboost": {
				"models": {},
				"outputDir": testsDir / "output",
				"inputDir": testModelsDir,
				"search": True
			}
		}
		pyxgboostHelper(None, None, testCfg["pyxgboost"])


if __name__ == "__main__":
	unittest.main()
