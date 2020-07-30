import json
import matplotlib.ticker as mtick
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
data = json.loads(open('result.json', encoding='utf-8').read())
user=data["3544"]#以3544为例
info_list=[]
for i in user:
    tuple=(i,user[i]["score"],user[i]["average_score"],user[i]["commit_num"],user[i]['average_num'])
    info_list.append(tuple)
positions= np.arange(len(info_list))
case_id = [row[0] for row in info_list]
score = [row[1] for row in info_list]
average_score = [row[2] for row in info_list]
commit_num=[row[3] for row in info_list]
average_num=[row[4] for row in info_list]
x = range(len(case_id))
fig, ax1 = plt.subplots()#直方图
ax1.bar(positions, commit_num, width=0.6, align='center', color='r', label=u"提交次数")
ax1.bar(positions, average_num, width=0.6, align='center', color='y', label=u"平均提交次数")
ax1.set_xticks(positions)
ax1.set_xticklabels(case_id)
ax1.set_xlabel(u"题目id")
ax1.set_ylabel(u"提交次数")
ax1.set_ylim(0, int(max(commit_num) * 1.2))
for x,y in zip(positions, commit_num):
    ax1.text(x, y + max(commit_num) * 0.02, y, ha='center', va='center', fontsize=13)
ax2 = ax1.twinx()#折线图
ax2.plot(positions, score, marker='o', mec='r', mfc='w',label=u"个人得分")
ax2.plot(positions, average_score, marker='*', ms=10, label=u"均分")
#for x, y in zip(positions, score):#标签
#    ax2.text(x, y + max(score) * 0.02, ('%.1f' % y), ha='center', va='bottom', fontsize=13)
ax2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d'))#设置纵轴格式yticks
ax2.set_ylim(-1, 101)
ax2.set_ylabel(u"分数")
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
plt.legend(handles1 + handles2, labels1 + labels2, loc='upper right')
plt.subplots_adjust(bottom=0.15)
plt.show()
