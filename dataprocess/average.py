import json

f = open('score.json', encoding='utf-8')
cases = []
count = []
score = []
users = {}
res = f.read()
data = json.loads(res)
for key in data:
    if key["case_id"] in cases:
        i = cases.index(key["case_id"])
        score[i] += key["score"]
        count[i] += 1
    else:
        cases.append(key["case_id"])
        count.append(1)
        score.append(key["score"])
for i in range(0, len(cases)):
    users[cases[i]] = score[i] / count[i]
filename = 'average.json'
with open(filename, 'w', encoding='utf-8') as file_obj:
    json.dump(users, file_obj, ensure_ascii=False, indent=4)
