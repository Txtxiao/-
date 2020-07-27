import json
import time
import datetime


# 时间轴转化
def time_transform(timeStamp):
    timeStamp = timeStamp / 1000
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
result = {}
# result包含类型，题目提交次数，最终得分，该题平均得分，第一次提交与最后一次提交间隔时间（单位：分钟）
f1 = open('average.json', encoding='utf-8')  # 每道题平均分
x = f1.read()
data1 = json.loads(x)
for key in data:
    user_id = data[key]['user_id']
    cases = data[key]['cases']
    result[user_id] = {}
    for case in cases:
        case_id = case['case_id']
        final_score = case['final_score']
        upload_records = case['upload_records']
        result[user_id][case_id] = {}
        result[user_id][case_id]['case_type'] = case['case_type']
        result[user_id][case_id]['commit_num'] = len(upload_records)
        result[user_id][case_id]['score'] = final_score
        result[user_id][case_id]['average_score'] = data1[case_id]
        result[user_id][case_id]['time'] = 0

        if len(upload_records) == 0:
            result[user_id][case_id]['time'] = -1  # 数据中有一个异常，没有提交次数却有最终成绩
        elif upload_records[0]['score'] == 100:  # 一开始提交就是满分，默认时间差为0
            result[user_id][case_id]['time'] = 0
        else:
            start = time_transform(upload_records[0]['upload_time'])
            end = time_transform(upload_records[-1]['upload_time'])
            d1 = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
            d2 = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
            day = (d2 - d1).days  # 天
            seconds = (d2 - d1).seconds  # 秒
            minutes = day * 1440 + round(seconds / 60, 1)
            result[user_id][case_id]['time'] = minutes

filename = 'result.json'
with open(filename, 'w', encoding='utf-8') as file_obj:
    json.dump(result, file_obj, ensure_ascii=False, indent=4)
