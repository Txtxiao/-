import json
import numpy as np
import matplotlib.pyplot as plt
#print (matplotlib.matplotlib_fname())
font = {'family': 'SimHei','weight': 'bold','size' : '16'}
plt.rc('font', **font)# 中文和负号的正常显示
plt.rc('axes', unicode_minus=False)
plt.style.use('ggplot')#使用ggplot的风格绘图
values = []#构造数据
res = open('average_class.json', encoding='utf-8').read()
data = json.loads(res)
for key in data:
    values.append(data[key])
feature = ['字符串','查找算法',"排序算法","数组","线性表","图结构","树结构","数组操作"]
N = len(values)
angles = np.linspace(0,2*np.pi,N,endpoint=False)#设置雷达图的角度，用于平分切开一个平面
values = np.concatenate((values,[values[0]]))#使雷达图封闭起来
angles = np.concatenate((angles,[angles[0]]))
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)#设置为极坐标格式
ax.plot(angles,values,'o-',linewidth=2,label='活动前')
ax.fill(angles,values,'r',alpha=0.5)
ax.set_thetagrids(angles*180/np.pi,feature)
ax.set_ylim(95,100)#设置极轴范围
plt.title('类型题目平均分比较')
ax.grid(True)#增加网格纸
plt.show()