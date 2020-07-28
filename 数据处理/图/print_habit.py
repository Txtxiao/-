import json
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
def time_transform(timeStamp):
    timeStamp = timeStamp / 1000
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    detime=otherStyleTime[otherStyleTime.find(" ")+1:otherStyleTime.rfind(":")]
    retime=detime[0:detime.find(":")]+str(int(detime[detime.find(":")+1:len(detime)])/60*1)[1:]
    return float(retime)
res = open('test_data.json', encoding='utf-8').read()
data = json.loads(res)
score=[]
timestamp=[]
for key in data["58778"]["cases"]:
    for key1 in key["upload_records"]:
        score.append(key1["score"])
        timestamp.append(time_transform(key1["upload_time"]))
plt.scatter(timestamp,score,s = 15,c = 'c',marker='D')#实现标记样式和图标样式的编辑：大小s，形状marker，颜色c
plt.title("时间和分数关系",size=15)
plt.xlabel("时刻",size=10)
plt.ylabel("分数",size=10)
plt.grid(True)#设置网格线
plt.xticks(range(0,25,1))
plt.show()