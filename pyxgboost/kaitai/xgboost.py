# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import str_pair_arr
from . import linear_booster
from . import pas_str
from . import tree_booster
from . import str_arr
class Xgboost(KaitaiStruct):
    """It is an xgboost tree model.
    
    .. seealso::
       Source - https://github.com/dmlc/xgboost/blob/98d6faefd629050dc4c0347b8373a989d06a3864/src/learner.cc#L831-L1076
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        if self.binf_signature_present:
            self.binf_signature = (self._io.read_bytes(4)).decode(u"ascii")

        self.param = Xgboost.ModelParam(self._io, self, self._root)
        self.name_obj_ = pas_str.PasStr(self._io)
        self.name_gbm_ = pas_str.PasStr(self._io)
        _on = self.name_gbm_.str
        if _on == u"gblinear":
            self.gbm_ = linear_booster.LinearBooster(self._io)
        else:
            self.gbm_ = tree_booster.TreeBooster(self._io)
        if self.param.contain_extra_attrs != 0:
            self.attributes_ = str_pair_arr.StrPairArr(self._io)

        if self.name_obj_.str == u"count:poisson":
            self.max_delta_step_str = pas_str.PasStr(self._io)

        if self.param.contain_eval_metrics != 0:
            self.metrics_ = str_arr.StrArr(self._io)


    class Reserved(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.zero = []
            i = 0
            while not self._io.is_eof():
                self.zero.append(Xgboost.Reserved.ZeroFill(self._io, self, self._root))
                i += 1


        class ZeroFill(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.zero = self._io.read_bytes(1)
                if not self.zero == b"\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00", self.zero, self._io, u"/types/reserved/types/zero_fill/seq/0")



    class ModelParam(KaitaiStruct):
        """training parameter for regression.
        
        .. seealso::
           Source - https://github.com/dmlc/xgboost/blob/98d6faefd629050dc4c0347b8373a989d06a3864/src/learner.cc#L78-L94
        
        
        
        .. seealso::
           Source - https://github.com/dmlc/xgboost/blob/98d6faefd629050dc4c0347b8373a989d06a3864/src/learner.cc#L162-L177
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_score = self._io.read_f4le()
            self.num_feature = self._io.read_u4le()
            self.num_class = self._io.read_u4le()
            self.contain_extra_attrs = self._io.read_u4le()
            self.contain_eval_metrics = self._io.read_u4le()
            self.xgboost_version = Xgboost.ModelParam.Version(self._io, self, self._root)
            self.num_target = self._io.read_u4le()
            self._raw_reserved = self._io.read_bytes((26 * 4))
            _io__raw_reserved = KaitaiStream(BytesIO(self._raw_reserved))
            self.reserved = Xgboost.Reserved(_io__raw_reserved, self, self._root)

        class Version(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.major = self._io.read_u4le()
                self.minor = self._io.read_u4le()



    @property
    def binf_signature_present(self):
        if hasattr(self, '_m_binf_signature_present'):
            return self._m_binf_signature_present if hasattr(self, '_m_binf_signature_present') else None

        self._m_binf_signature_present =  ((KaitaiStream.byte_array_index(self.optional_binf_signature, 0) == 98) and (KaitaiStream.byte_array_index(self.optional_binf_signature, 1) == 105) and (KaitaiStream.byte_array_index(self.optional_binf_signature, 2) == 110) and (KaitaiStream.byte_array_index(self.optional_binf_signature, 3) == 102)) 
        return self._m_binf_signature_present if hasattr(self, '_m_binf_signature_present') else None

    @property
    def optional_binf_signature(self):
        if hasattr(self, '_m_optional_binf_signature'):
            return self._m_optional_binf_signature if hasattr(self, '_m_optional_binf_signature') else None

        _pos = self._io.pos()
        self._io.seek(0)
        self._m_optional_binf_signature = self._io.read_bytes(4)
        self._io.seek(_pos)
        return self._m_optional_binf_signature if hasattr(self, '_m_optional_binf_signature') else None

    @property
    def max_delta_step(self):
        """maximum delta update we can add in weight estimation
        this parameter can be used to stabilize update
        default=0 means no constraint on weight delta
        
        .. seealso::
           param.h
        """
        if hasattr(self, '_m_max_delta_step'):
            return self._m_max_delta_step if hasattr(self, '_m_max_delta_step') else None

        if self.name_obj_.str == u"count:poisson":
            self._m_max_delta_step = int(self.max_delta_step_str.str)

        return self._m_max_delta_step if hasattr(self, '_m_max_delta_step') else None


