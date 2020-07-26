import json
from datetime import datetime
import matplotlib.dates as dt
import pandas as pd
import matplotlib.dates as mdate
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
def time_transform(timeStamp):
    timeStamp = timeStamp / 1000
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime[0:otherStyleTime.rfind(" ")]

res = open('test_data.json', encoding='utf-8').read()
data = json.loads(res)
score=[]
timestamp=[]
for key in data["60671"]["cases"]:
    for key1 in key["upload_records"]:
        score.append(key1["score"])
        timestamp.append(time_transform(key1["upload_time"]))
timestamp=[datetime.datetime.strptime(x, '%Y-%m-%d').date() for x in timestamp]
plt.scatter(timestamp,score,s = 15,c = 'c',marker='D')#实现标记样式和图标样式的编辑：大小s，形状marker，颜色c
plt.title("日期和分数关系",size=15)
plt.xlabel("日期",size=10)
plt.ylabel("分数",size=10)
plt.grid(True)#设置网格线
ax = plt.gca()#表明设置图片的各个轴plt.gcf()表示图片本身
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))
plt.xticks(pd.date_range('2020-2-17','2020-4-1',freq='7d'),rotation=30)
plt.yticks(range(0, 101, 10))
plt.show()