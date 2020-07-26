import  json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   # 正确显示中文字体
data_labels = np.array(['个人分数', '总体分数'])
n = 8
radar_labels = np.array(['字符串','查找算法',"排序算法","数组","线性表","图结构","树结构","数组操作"])
data = json.loads(open('type_average.json', encoding='utf-8').read())
user=data["60587"]#以60587为例
values = []
values1 = []
for i in user:
    values.append(user[i]["score"])
    values1.append(user[i]["average_score"])
data=np.array(list(zip(values,values1)))
angles=np.linspace(0, 2*np.pi, n, endpoint=False)       # 将360度平均分为n个部分
data=np.concatenate((data, [data[0]]))
angles=np.concatenate((angles, [angles[0]]))

fig = plt.figure(facecolor='white', figsize=(10,8))    # 绘制全局绘图区域
plt.subplot(111, polar=True)    # 绘制一个1行1列极坐标系子图，当前位置为1

plt.figtext(0.52,0.95,'某学生各类型题目平均分对比',ha='center',size=20)   #放置标题 ，ha是horizontalalignment（水平对齐方式）的缩写
plt.thetagrids(angles*180/np.pi, radar_labels)       # 放置属性（radar_labels）
plt.plot(angles, data, 'o-', linewidth=1.5, alpha=0.2)      # 连线
plt.fill(angles, data,alpha=0.5)        # 填充，alpha是透明度
legend=plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)    # 放置图注（右上角）
plt.setp(legend.get_texts(), fontsize='medium')
plt.grid(True)    # 打开坐标网格
plt.show()       # 显示