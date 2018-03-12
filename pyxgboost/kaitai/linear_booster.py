# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import pas_str
from . import f4_arr
class LinearBooster(KaitaiStruct):
    """gradient boosted linear model.
    
    .. seealso::
       Source - https://github.com/dmlc/xgboost/blob/master/src/gbm/gblinear_model.h#L49L58
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.param = LinearBooster.Param(self._io, self, self._root)
        self.weight = f4_arr.F4Arr(self._io)

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
                self.zero.append(LinearBooster.Reserved.ZeroFill(self._io, self, self._root))
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



    class Param(KaitaiStruct):
        """model parameter.
        
        .. seealso::
           Source - https://github.com/dmlc/xgboost/blob/master/src/gbm/gblinear_model.h#L15L33
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_feature = self._io.read_u4le()
            self.num_output_group = self._io.read_u4le()
            self._raw_reserved = self._io.read_bytes((32 * 4))
            _io__raw_reserved = KaitaiStream(BytesIO(self._raw_reserved))
            self.reserved = LinearBooster.Reserved(_io__raw_reserved, self, self._root)


    class TrainParam(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/dmlc/xgboost/blob/master/src/gbm/gblinear.cc#L25L46
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.updater = pas_str.PasStr(self._io)
            self.debug_verbose = self._io.read_s4le()
            self.tolerance = self._io.read_f4le()



