import matplotlib.pyplot as plt
labels = ['100','95-99','85-95','70-85','0-85']
x = [40.6,43.9,7.75,3.32,4.43]#显示百分比110/40.6，119/43.9，21/7.75，9/3.324，12/4.43（人数/占比）
explode = (0.1,0,0,0,0)#饼图分离
#设置阴影效果
#startangle,为起始角度，0表示从0开始逆时针旋转，为第一块。
#pctdistance,百分比的文本离圆心的距离为0.5
plt.pie(x,labels=labels,autopct='%3.2f%%',explode=explode,shadow=True,startangle=60,pctdistance=0.8)
#设置x,y的刻度一样，使其饼图为正圆
plt.axis('equal')
plt.legend()#保存到本地文件夹是plt.savefig('./饼图.png')
plt.show()