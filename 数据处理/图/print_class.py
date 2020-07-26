#类型题目平均分比较雷达图
import json
import numpy as np
import matplotlib.pyplot as plt

#print (matplotlib.matplotlib_fname())
# 中文和负号的正常显示
font = {'family': 'SimHei','weight': 'bold','size' : '16'}
plt.rc('font', **font)
plt.rc('axes', unicode_minus=False)

#使用ggplot的风格绘图
plt.style.use('ggplot')

#构造数据
values = []
res = open('average_class.json', encoding='utf-8').read()
data = json.loads(res)
for key in data:
    values.append(data[key])
feature = ['字符串','查找算法',"排序算法","数组","线性表","图结构","树结构","数组操作"]

N = len(values)
#设置雷达图的角度，用于平分切开一个平面
angles = np.linspace(0,2*np.pi,N,endpoint=False)

#使雷达图封闭起来
values = np.concatenate((values,[values[0]]))
angles = np.concatenate((angles,[angles[0]]))

#绘图
fig = plt.figure()
#设置为极坐标格式
ax = fig.add_subplot(111, polar=True)
#绘制折线图填充颜色
ax.plot(angles,values,'o-',linewidth=2,label='活动前')
ax.fill(angles,values,'r',alpha=0.5)

#添加每个特质的标签
ax.set_thetagrids(angles*180/np.pi,feature)
#设置极轴范围
ax.set_ylim(95,100)
#添加标题
plt.title('类型题目平均分比较')
#增加网格纸
ax.grid(True)
plt.show()