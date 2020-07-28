import json

from utils.tree.astprocess import *


# 抽象语法树信息摘要
def mk_summary(r_node):
    pass


# 计算语法树相似度
# 根节点相似程度 各子树相似程度
def mk_comp(r_node1, r_node2):
    # 规定两个空节点相似度为0
    if is_empty(r_node1) or is_empty(r_node2):
        return 0
    # 如果有一个是叶节点
    if is_leaf(r_node1) or is_leaf(r_node2):
        node_hash1 = node_hash(r_node1)
        node_hash2 = node_hash(r_node2)
        return 100 * min(node_hash1, node_hash2) / max(node_hash1, node_hash2) / max(cal_nonempty_node_num(r_node1),
                                                                                     cal_nonempty_node_num(r_node2))
    hash_list1 = []
    hash_list2 = []

    index = 0
    for sub_node in r_node1.body:
        if not is_empty(sub_node):
            hash_list1.append((index, node_hash(sub_node)))
        index += 1

    index = 0
    for sub_node in r_node2.body:
        if not is_empty(sub_node):
            hash_list2.append((index, node_hash(sub_node)))
        index += 1

    # 按照哈希值由大到小进行排序匹配
    hash_list1.sort(key=lambda x: x[1])
    hash_list2.sort(key=lambda x: x[1])

    max_len = max(len(hash_list1), len(hash_list2))
    min_len = min(len(hash_list1), len(hash_list2))
    similarities = []

    for i in range(0, min_len):
        n1 = r_node1.body[hash_list1[i][0]]
        n2 = r_node2.body[hash_list2[i][0]]
        similarity = mk_comp(n1, n2)
        similarities.append(similarity)

    for i in range(min_len, max_len):
        similarities.append(0)

    # 根节点相似度
    h1 = node_hash(r_node1)
    h2 = node_hash(r_node2)
    root_similarity = 100 * min(h1, h2) / max(h1, h2)

    total_nodes_num = len(similarities) + 1
    return (sum(similarities) + root_similarity) / total_nodes_num


# 基于剪枝的动态树相似度算法判别代码是否同源
# 规定如果相似节点占总节点数50%以上为同源
def is_same_source(r_node1, r_node2):
    # 原节点数量
    s1 = cal_nonempty_node_num(r_node1)
    s2 = cal_nonempty_node_num(r_node2)

    # 最大剪枝次数
    max_cut_times = min(cal_node_height(r_node1), cal_node_height(r_node2))

    # 阈值
    v = 100
    with open('../../dataprocess/tree_train.json', 'r') as f:
        json_reader = json.load(f)
        v = json_reader['value']

    t1 = copy.deepcopy(r_node1)
    t2 = copy.deepcopy(r_node2)

    flag = False
    for i in range(max_cut_times):
        if mk_comp(t1, t2) >= v:
            flag = True
            break
        t1 = cut_leaves(t1)
        t2 = cut_leaves(t2)

    if mk_comp(t1, t2) >= v:
        flag = True

    if not flag:
        return False

    # todo 多剪的节点应该尝试逐一放回
    if cal_nonempty_node_num(t1) > s1 / 2 or cal_nonempty_node_num(t2) > s2 / 2:
        print("代码1相似度节点数量%d 总结点数量%d" % (cal_nonempty_node_num(t1), s1))
        print("代码2相似度节点数量%d 总结点数量%d" % (cal_nonempty_node_num(t2), s2))
        return True

    return False


if __name__ == '__main__':
    file_path1 = "../../data/code/test1.py"
    file_path2 = "../../data/code/test1.py"
    node1 = trans_code_into_tree(open(file_path1))
    node2 = trans_code_into_tree(open(file_path2))
    print(is_same_source(node1, node2))
