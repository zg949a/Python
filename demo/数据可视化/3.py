import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(2,4,s=200)
#设置图标 标题以及给坐标轴加上标签
ax.set_title('平方数',fontsize=24)
ax.set_xlabel('值',fontsize=14)
ax.set_ylabel('平方的值',fontsize=14)
#设置刻度标记的大小
ax.tick_params(axis='both',which='major',labelsize=14)
plt.show()