import json
import os
import time

from utils.tree.postprocess import *


def train(d):
    dir_list = os.listdir(d)
    p = 1
    for sub_d in dir_list:
        sd = os.path.abspath(d) + "\\" + sub_d
        # print(sd)
        sub_dir_list = os.listdir(sd)
        # print(sub_dir_list)
        if len(sub_dir_list) < 2:
            print("训练样本%d不足" % p)
        else:
            _train(sd + "\\" + sub_dir_list[0], sd + "\\" + sub_dir_list[1])
        p += 1


def _train(d1, d2):
    f1 = open(d1, 'r')
    n1 = trans_code_into_tree(f1)
    f2 = open(d2, 'r')
    n2 = trans_code_into_tree(f2)
    similarity = mk_comp(n1, n2)

    result_json_path = "./tree_train.json"
    f = open(result_json_path, 'r')
    json_reader = json.load(f)
    print(json_reader)

    mode = json_reader['mode']
    train_times = json_reader['times']
    value = json_reader['value']
    output = {}

    if mode == 0:
        # 权重相同
        output['value'] = (value * train_times + similarity) / (train_times + 1)
        output['times'] = train_times + 1
        output['mode'] = mode
    output['lastTrain'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(result_json_path, 'w') as f:
        json.dump(output, f)


if __name__ == '__main__':
    fp = "../data/code/tree"
    train(fp)
