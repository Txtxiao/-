import json
f = open('score.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
cases = []
count = []
score = []
average_num=[]
users = []
for key in data:
    if key["case_id"] in cases:
        i = cases.index(key["case_id"])
        score[i] += key["score"]
        count[i] += 1
        average_num[i]+=key["commit_num"]
    else:
        cases.append(key["case_id"])
        count.append(1)
        score.append(key["score"])
        average_num.append(key["commit_num"])
for i in range(0, len(cases)):
    dic={}
    dic['case_id']=cases[i]
    dic['score'] = score[i] / count[i]
    dic['average_num'] = average_num[i] / count[i]
    users.append(dic)
filename = 'average.json'
with open(filename, 'w', encoding='utf-8') as file_obj:
    json.dump(users, file_obj, ensure_ascii=False, indent=4)
