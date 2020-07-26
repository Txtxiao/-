import json
f = open('result.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
f1 = open('average_class.json', encoding='utf-8')
data1 = json.loads(f1.read())
result = {}
for key in data:
    user_id = key
    case=data[key]
    scorez=0
    scorec = 0
    scorep = 0
    scores = 0
    scorex = 0
    scoret = 0
    scoretree = 0
    scoreoper = 0 #分别为"字符串","查找算法","排序算法","数组","线性表","图结构","树结构","数字操作"
    countz = 0
    countc = 0
    countp = 0
    counts = 0
    countx = 0
    countt = 0
    counttree = 0
    countoper = 0  # 分别为"字符串","查找算法","排序算法","数组","线性表","图结构","树结构","数字操作"
    for i in case:
        if(data[key][i]["case_type"])=="字符串":
            scorez+=data[key][i]["score"]
            countz+=1
        if (data[key][i]["case_type"]) == "查找算法":
            scorec += data[key][i]["score"]
            countc += 1
        if (data[key][i]["case_type"]) == "排序算法":
            scorep += data[key][i]["score"]
            countp += 1
        if (data[key][i]["case_type"]) == "数组":
            scores += data[key][i]["score"]
            counts += 1
        if (data[key][i]["case_type"]) == "线性表":
            scorex += data[key][i]["score"]
            countx += 1
        if (data[key][i]["case_type"]) == "图结构":
            scoret += data[key][i]["score"]
            countt += 1
        if (data[key][i]["case_type"]) == "树结构":
            scoretree += data[key][i]["score"]
            counttree += 1
        if (data[key][i]["case_type"]) == "数字操作":
            scoreoper += data[key][i]["score"]
            countoper += 1
    if(countz==0):
        countz=1
    if (countc == 0):
        countc = 1
    if (countp == 0):
        countp = 1
    if (counts == 0):
        counts = 1
    if (countx == 0):
        countx = 1
    if (countt == 0):
        countt = 1
    if (counttree == 0):
        counttree = 1
    if (countoper == 0):
        countoper = 1
    result[user_id]={}
    result[user_id]['字符串']={}
    result[user_id]["查找算法"]={}
    result[user_id]["排序算法"]={}
    result[user_id]["数组"]={}
    result[user_id]["线性表"]={}
    result[user_id]["图结构"]={}
    result[user_id]["树结构"]={}
    result[user_id]["数字操作"]={}

    result[user_id]['字符串']["score"]=scorez/countz
    result[user_id]["查找算法"]["score"] = scorec/countc
    result[user_id]["排序算法"]["score"] = scorep/countp
    result[user_id]["数组"]["score"] = scores/counts
    result[user_id]["线性表"]["score"] = scorex/countx
    result[user_id]["图结构"]["score"] = scoret/countt
    result[user_id]["树结构"]["score"] = scoretree/counttree
    result[user_id]["数字操作"]["score"] = scoreoper/countoper
    result[user_id]["字符串"]["average_score"] = data1["字符串"]
    result[user_id]["查找算法"]["average_score"] = data1["查找算法"]
    result[user_id]["排序算法"]["average_score"] = data1["排序算法"]
    result[user_id]["数组"]["average_score"] = data1["数组"]
    result[user_id]["线性表"]["average_score"] = data1["线性表"]
    result[user_id]["图结构"]["average_score"] = data1["图结构"]
    result[user_id]["树结构"]["average_score"] = data1["树结构"]
    result[user_id]["数字操作"]["average_score"] = data1["数字操作"]
filename = 'type_average.json'
with open(filename, 'w', encoding='utf-8') as file_obj:
    json.dump(result, file_obj, ensure_ascii=False, indent=4)


