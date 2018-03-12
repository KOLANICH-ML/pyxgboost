# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import pas_str
class StrPair(KaitaiStruct):
    """It's a pair of strings serialized by dmlc-core.
    
    .. seealso::
       Source - https://github.com/dmlc/dmlc-core/blob/a6c5701219e635fea808d264aefc5b03c3aec314/include/dmlc/serializer.h#L178L188
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.pair = [None] * (2)
        for i in range(2):
            self.pair[i] = pas_str.PasStr(self._io)



