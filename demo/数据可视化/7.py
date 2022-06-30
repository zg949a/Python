from random import choice
import matplotlib.pyplot as plt

class randomwalk:
    #生成随机漫步数据的类
    def __init__(self,num_points=5000):
        #初始化随机漫步
        self.num_points = num_points
        #所有随机数都是于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        #计算随机漫步包含的所有点
        #不断漫步，知道列表达到指定的长度
        while len(self.x_values) < self.num_points:
            #绝对前进方向以及言这个方向前进指定的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

while True:
    # 创建一个实例
    rw = randomwalk(50000)
    rw.fill_walk()
    # 将所有的点都会指出来
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    #突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none', s=15)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('是否继续:')
    if keep_running == 'n' or keep_running == 'no':
        break