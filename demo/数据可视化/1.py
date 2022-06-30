import matplotlib.pyplot as plt
plt.style.available

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(1,1,s=200)
ax.scatter(2,4,s=200)
ax.scatter(3,9,s=200)
ax.scatter(4,16,s=200)
ax.scatter(5,25,s=200)
ax.plot(input_values,squares,linewidth=3)#线条的粗细
#设置图标 标题以及给坐标轴加上标签
ax.set_title('平方数',fontsize=24)
ax.set_xlabel('值',fontsize=14)
ax.set_ylabel('平方的值',fontsize=24)
#设置刻度标记的大小
ax.tick_params(axis='both',which='major',labelsize=14)
#绘制图片
plt.show()