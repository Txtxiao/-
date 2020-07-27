# 抽象语法树信息摘要
from utils.tree.astprocess import *


def mk_summary(r_node):
    pass


# 计算语法树相似度
def mk_comp(r_node1, r_node2):
    if is_empty(r_node1) or is_empty(r_node2):
        return 0
    hash_list1 = []
    hash_list2 = []
    for sub_node in r_node1.body:
        if not is_empty(sub_node):
            hash_list1.append(node_hash(sub_node))
    for sub_node in r_node2.body:
        if not is_empty(sub_node):
            hash_list2.append(node_hash(sub_node))
    hash_list1.sort()
    hash_list2.sort()
    max_len = max(len(hash_list1), len(hash_list2))
    min_len = min(len(hash_list1), len(hash_list2))
    similarities = []
    for i in range(0, min_len):
        similarities.append(100 * min(hash_list1[i], hash_list2[i]) / max(hash_list1[i], hash_list2[i]))
    for i in range(min_len, max_len):
        similarities.append(0)

    # 根节点相似度
    h1 = node_hash(r_node1)
    h2 = node_hash(r_node2)
    root_similarity = 100 * min(h1, h2) / max(h1, h2)

    total_nodes_num = len(similarities) + 1
    return (sum(similarities) + root_similarity) / total_nodes_num


if __name__ == '__main__':
    file_path1 = "../../data/code/main.py"
    file_path2 = "../../data/code/test1.py"
    node1 = trans_code_into_tree(open(file_path1))
    node2 = trans_code_into_tree(open(file_path2))
    print(mk_comp(node1, node2))
