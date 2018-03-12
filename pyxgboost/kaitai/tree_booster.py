# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import f4_arr
class TreeBooster(KaitaiStruct):
    """Gradient boosting tree ensembles.
    
    .. seealso::
       Source - https://github.com/dmlc/xgboost/blob/master/src/gbm/gbtree_model.h#L82L98
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.param = TreeBooster.Param(self._io, self, self._root)
        self.trees = [None] * (self.param.num_trees)
        for i in range(self.param.num_trees):
            self.trees[i] = TreeBooster.RegTree(self._io, self, self._root)

        self.trees_infos = [None] * (self.param.num_trees)
        for i in range(self.param.num_trees):
            self.trees_infos[i] = self._io.read_u4le()


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
                self.zero.append(TreeBooster.Reserved.ZeroFill(self._io, self, self._root))
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



    class Placeholder(KaitaiStruct):
        """needed only to have _io."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._unnamed0 = self._io.read_bytes_full()


    class Param(KaitaiStruct):
        """model parameters.
        
        .. seealso::
           Source - https://github.com/dmlc/xgboost/blob/master/src/gbm/gbtree_model.h#L15L60
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_trees = self._io.read_u4le()
            self.num_roots = self._io.read_u4le()
            self.num_feature = self._io.read_u4le()
            self.pad_32bit = self._io.read_u4le()
            self.num_pbuffer_deprecated = self._io.read_u8le()
            self.num_output_group = self._io.read_u4le()
            self.size_leaf_vector = self._io.read_u4le()
            self._raw_reserved = self._io.read_bytes((32 * 4))
            _io__raw_reserved = KaitaiStream(BytesIO(self._raw_reserved))
            self.reserved = TreeBooster.Reserved(_io__raw_reserved, self, self._root)


    class RegTree(KaitaiStruct):
        """define regression tree to be the most common tree model.
        This is the data structure used in xgboost's major tree models.
        
        .. seealso::
           Source - https://github.com/dmlc/xgboost/blob/master/include/xgboost/tree_model.h#L308L343
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.param = TreeBooster.RegTree.Param(self._io, self, self._root)
            self.nodes = [None] * (self.param.num_nodes)
            for i in range(self.param.num_nodes):
                self.nodes[i] = TreeBooster.RegTree.Node(self._io, self, self._root)

            self.stats = [None] * (self.param.num_nodes)
            for i in range(self.param.num_nodes):
                self.stats[i] = TreeBooster.RegTree.NodeStat(self._io, self, self._root)

            if self.param.size_leaf_vector != 0:
                self._raw_leaf_vector = self._io.read_bytes(((self.param.num_nodes * self.param.size_leaf_vector) + 8))
                _io__raw_leaf_vector = KaitaiStream(BytesIO(self._raw_leaf_vector))
                self.leaf_vector = f4_arr.F4Arr(_io__raw_leaf_vector)


        class NodeStat(KaitaiStruct):
            """node statistics used in regression tree.
            
            .. seealso::
               Source - https://github.com/dmlc/xgboost/blob/master/include/xgboost/tree_model.h#L404L413
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.loss_chg = self._io.read_f4le()
                self.sum_hess = self._io.read_f4le()
                self.base_weight = self._io.read_f4le()
                self.leaf_child_cnt = self._io.read_u4le()


        class FeatureVector(KaitaiStruct):
            """dense feature vector that can be taken by RegTree and can be construct from sparse feature vector.
            
            .. seealso::
               Source - https://github.com/dmlc/xgboost/blob/master/include/xgboost/tree_model.h#L439L484
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.data = []
                i = 0
                while not self._io.is_eof():
                    self.data.append(TreeBooster.RegTree.FeatureVector.Entry(self._io, self, self._root))
                    i += 1


            class Entry(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._read()

                def _read(self):
                    self._raw_placeholder = self._io.read_bytes(4)
                    _io__raw_placeholder = KaitaiStream(BytesIO(self._raw_placeholder))
                    self.placeholder = TreeBooster.Placeholder(_io__raw_placeholder, self, self._root)

                @property
                def fvalue(self):
                    if hasattr(self, '_m_fvalue'):
                        return self._m_fvalue if hasattr(self, '_m_fvalue') else None

                    io = self.placeholder._io
                    _pos = io.pos()
                    io.seek(0)
                    self._m_fvalue = io.read_f4le()
                    io.seek(_pos)
                    return self._m_fvalue if hasattr(self, '_m_fvalue') else None

                @property
                def flag(self):
                    if hasattr(self, '_m_flag'):
                        return self._m_flag if hasattr(self, '_m_flag') else None

                    io = self.placeholder._io
                    _pos = io.pos()
                    io.seek(0)
                    self._m_flag = io.read_u4le()
                    io.seek(_pos)
                    return self._m_flag if hasattr(self, '_m_flag') else None



        class Param(KaitaiStruct):
            """model parameters.
            
            .. seealso::
               Source - https://github.com/dmlc/xgboost/blob/master/include/xgboost/tree_model.h#L26L63
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.num_roots = self._io.read_u4le()
                self.num_nodes = self._io.read_u4le()
                self.num_deleted = self._io.read_u4le()
                self.max_depth = self._io.read_u4le()
                self.num_feature = self._io.read_u4le()
                self.size_leaf_vector = self._io.read_u4le()
                self.reserved = self._io.read_bytes((31 * 4))


        class Node(KaitaiStruct):
            """tree node.
            
            .. seealso::
               Source - https://github.com/dmlc/xgboost/blob/master/include/xgboost/tree_model.h#L78L192
            """
            def __init__(self, _io, _parent=None, _root=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._read()

            def _read(self):
                self.parent_ = self._io.read_u4le()
                self.cleft_ = self._io.read_u4le()
                self.cright_ = self._io.read_u4le()
                self.sindex_ = self._io.read_u4le()
                self.info_ = self._io.read_f4le()

            @property
            def left(self):
                if hasattr(self, '_m_left'):
                    return self._m_left if hasattr(self, '_m_left') else None

                if not (self.is_leaf):
                    self._m_left = self._parent.nodes[self.cleft_]

                return self._m_left if hasattr(self, '_m_left') else None

            @property
            def split_cond(self):
                if hasattr(self, '_m_split_cond'):
                    return self._m_split_cond if hasattr(self, '_m_split_cond') else None

                if not (self.is_leaf):
                    self._m_split_cond = self.info_

                return self._m_split_cond if hasattr(self, '_m_split_cond') else None

            @property
            def split_index(self):
                """feature index of split condition."""
                if hasattr(self, '_m_split_index'):
                    return self._m_split_index if hasattr(self, '_m_split_index') else None

                self._m_split_index = (self.sindex_ & 2147483647)
                return self._m_split_index if hasattr(self, '_m_split_index') else None

            @property
            def is_left_child(self):
                """whether current node is left child."""
                if hasattr(self, '_m_is_left_child'):
                    return self._m_is_left_child if hasattr(self, '_m_is_left_child') else None

                self._m_is_left_child = (self.parent_ & 2147483648) != 0
                return self._m_is_left_child if hasattr(self, '_m_is_left_child') else None

            @property
            def is_deleted(self):
                """whether this node is deleted."""
                if hasattr(self, '_m_is_deleted'):
                    return self._m_is_deleted if hasattr(self, '_m_is_deleted') else None

                self._m_is_deleted = self.sindex_ == 4294967295
                return self._m_is_deleted if hasattr(self, '_m_is_deleted') else None

            @property
            def right(self):
                if hasattr(self, '_m_right'):
                    return self._m_right if hasattr(self, '_m_right') else None

                if not (self.is_leaf):
                    self._m_right = self._parent.nodes[self.cright_]

                return self._m_right if hasattr(self, '_m_right') else None

            @property
            def is_leaf(self):
                """whether current node is leaf node."""
                if hasattr(self, '_m_is_leaf'):
                    return self._m_is_leaf if hasattr(self, '_m_is_leaf') else None

                self._m_is_leaf = self.cleft_ == 4294967295
                return self._m_is_leaf if hasattr(self, '_m_is_leaf') else None

            @property
            def leaf_value(self):
                if hasattr(self, '_m_leaf_value'):
                    return self._m_leaf_value if hasattr(self, '_m_leaf_value') else None

                if self.is_leaf:
                    self._m_leaf_value = self.info_

                return self._m_leaf_value if hasattr(self, '_m_leaf_value') else None

            @property
            def parent(self):
                """get parent of the node."""
                if hasattr(self, '_m_parent'):
                    return self._m_parent if hasattr(self, '_m_parent') else None

                self._m_parent = (self.parent_ & 2147483647)
                return self._m_parent if hasattr(self, '_m_parent') else None

            @property
            def default_left(self):
                """when feature is unknown, whether goes to left child."""
                if hasattr(self, '_m_default_left'):
                    return self._m_default_left if hasattr(self, '_m_default_left') else None

                self._m_default_left = (self.sindex_ & 2147483648) != 0
                return self._m_default_left if hasattr(self, '_m_default_left') else None

            @property
            def is_root(self):
                """whether current node is root."""
                if hasattr(self, '_m_is_root'):
                    return self._m_is_root if hasattr(self, '_m_is_root') else None

                self._m_is_root = self.parent_ == 4294967295
                return self._m_is_root if hasattr(self, '_m_is_root') else None




