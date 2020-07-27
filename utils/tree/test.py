from utils.tree.astprocess import *

if __name__ == '__main__':
    file_path="../../data/code/main.py"
    file_path2 = "../../data/code/main_cp.py"
    node=trans_code_into_tree(open(file_path))
    v1=node_hash(node)
    node2=cut_leaves(node)
    v2=node_hash(node2)
    node3=cut_leaves(node2)
    v3=node_hash(node3)
    print(v1,v2,v3)

    node = trans_code_into_tree(open(file_path2))
    v1 = node_hash(node)
    node2 = cut_leaves(node)
    v2 = node_hash(node2)
    node3 = cut_leaves(node2)
    v3 = node_hash(node3)
    print(v1, v2, v3)