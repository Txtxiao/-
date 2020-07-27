import json
import os
f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
users=[]
for key in data:
    cases = data[key]['cases']
    user_id = str(data[key]['user_id'])
    for case in cases:
        Mycase={"case_id":case["case_id"],
                "score":case["final_score"],
                "case_type":case["case_type"]}
        users.append(Mycase)
filename = 'score.json'
with open(filename, 'w', encoding='utf-8') as file_obj:
    json.dump(users, file_obj, ensure_ascii=False, indent=4)