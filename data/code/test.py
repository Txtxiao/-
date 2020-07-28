from utils.tree.postprocess import *

if __name__ == '__main__':
    file_path = "./test6.py"
    with open(file_path) as f:
        node = trans_code_into_tree(open(file_path))
        print(mk_summary(node))
    exit(0)