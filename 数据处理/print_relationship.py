import matplotlib.pyplot as plt
import json
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
data = json.loads(open('result.json', encoding='utf-8').read())
user=data["3544"]#以3544为例
case_id = []
y=[]
y1=[]
for i in user:
    case_id.append(i)
    y.append(user[i]["score"])
    y1.append(user[i]["average_score"])
x = range(len(case_id))
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')

plt.ylim(-1, 101)  # 限定纵轴的范围
plt.plot(x, y, marker='o', mec='r', mfc='w',label=u'个人得分')
plt.plot(x, y1, marker='*', ms=10,label=u'均分')
plt.legend()  # 让图例生效
plt.xticks(x, case_id, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"题目ID") #X轴标签
plt.ylabel("分数") #Y轴标签
plt.title("个人分数与该题均分对比") #标题

plt.show()
