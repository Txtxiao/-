import ast
import copy


def trans_code_into_tree(file):
    func_def = file.read()
    r_node = ast.parse(func_def)
    return r_node


# 计算树的高度(最多剪枝次数)
def cal_node_height(node):
    if is_empty(node):
        return 0
    if is_leaf(node):
        return 1
    return 1 + max([cal_node_height(x) for x in node.body])


# 计算非空节点个数
def cal_nonempty_node_num(node):
    if is_empty(node):
        return 0
    if is_leaf(node):
        return 1
    else:
        s = 1
        for sub_node in node.body:
            s += cal_nonempty_node_num(sub_node)
        return s


# 剪枝
def cut_leaves(node):
    cp_node = copy.deepcopy(node)
    if not is_empty(node):
        if is_leaf(cp_node):
            # 置为空节点
            cp_node.is_empty = True
        else:
            for n in cp_node.body:
                _cut_leaves(n)
    return cp_node


def _cut_leaves(node):
    if not is_empty(node):
        if is_leaf(node):
            # 置为空节点
            node.is_empty = True
        else:
            for n in node.body:
                _cut_leaves(n)


# 生成节点的hash值
def node_hash(node):
    if is_empty(node):
        return 0
    if is_leaf(node):
        # 叶子节点
        return hash_leaf(node)
    else:
        # 非叶子节点
        hash_value = 0
        for sub_node in node.body:
            # 父节点哈希值为子结点哈希值之和
            hash_value += node_hash(sub_node)
        hash_value += hash_self(node)
        return hash_value


def hash_self(node):
    hash_value = hash_method(str(type(node)), 10)
    # print(hash_value)
    return hash_value


def hash_leaf(node):
    """
    :param node:
    :return:
    raw_attr:
    @_attributes
    @_fields
    @col_offset
    @end_col_offset
    @level
    @lineno
    @module
    @names

    """
    hash_value = hash_method(str(type(node)), 10)
    # print(hash_value)
    return hash_value


def hash_method(s, length):
    v = 0
    c_list = list(s)
    for c in c_list:
        v *= 10
        v += ord(c)
    base = pow(10, length - 1)
    return v % base


def is_leaf(node):
    if not hasattr(node, 'body'):
        return True
    flag = True
    for n in node.body:
        if not is_empty(n):
            flag = False
    return flag


def is_empty(node):
    return hasattr(node, 'is_empty')
