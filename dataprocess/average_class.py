import json
res = open('score.json', encoding='utf-8').read()
data = json.loads(res)
count=[0 for x in range(8)]
score=[0 for x in range(8)]
users={}
for key in data:
    if(key["case_type"]=="字符串"):
        count[0]+=1
        score[0]+=key["score"]
    elif(key["case_type"]=="查找算法"):
        count[1] += 1
        score[1] += key["score"]
    elif(key["case_type"]=="排序算法"):
        count[2] += 1
        score[2] += key["score"]
    elif(key["case_type"]=="数组"):
        count[3] += 1
        score[3] += key["score"]
    elif (key["case_type"] == "线性表"):
        count[4] += 1
        score[4] += key["score"]
    elif (key["case_type"] == "图结构"):
        count[5] += 1
        score[5] += key["score"]
    elif (key["case_type"] == "树结构"):
        count[6] += 1
        score[6] += key["score"]
    else:
        count[7] += 1
        score[7] += key["score"]
users["字符串"]=score[0]/count[0]
users["查找算法"]=score[1]/count[1]
users["排序算法"]=score[2]/count[2]
users["数组"]=score[3]/count[3]
users["线性表"]=score[4]/count[4]
users["图结构"]=score[5]/count[5]
users["树结构"]=score[6]/count[6]
users["数字操作"]=score[7]/count[7]
filename = 'average_class.json'
with open(filename, 'w', encoding='utf-8') as file_obj:
    json.dump(users, file_obj, ensure_ascii=False, indent=4)
