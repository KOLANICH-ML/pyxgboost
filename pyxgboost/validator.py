import json
from pathlib import Path

import jsonschema

thisDir = Path(__file__).parent
with (thisDir / "config.schema.json").open("rt", encoding="utf-8") as f:
	schema = json.load(f)


def isPath(val):
	if isinstance(val, Path):
		return True
	elif isinstance(val, str):
		try:
			Path(val)
		except BaseException:
			return False
	return False


types = {"function": callable, "path": isPath}
ValidatorT = jsonschema.validators._LATEST_VERSION
ourTypeChecker = ValidatorT.TYPE_CHECKER.redefine_many(types)
ValidatorT = jsonschema.validators.extend(ValidatorT, type_checker=ourTypeChecker)
validator = ValidatorT(schema)
