from random import randint
from plotly import offline
from plotly.graph_objs import Bar, Layout

class die:
    #一个骰子的类
    def __init__(self, num_sides=6):
        #骰子有六面
        self.num_sides = num_sides

    def roll(self):
        #返回一个位于1和骰子面熟 的随机值
        return  randint(1, self.num_sides)

die1 = die()
die2 = die()
results = []
for roll_num in range(100):
    result = die1.roll() + die2.roll()
    results.append(result)

print(results)
frequencies = []
for value in range(1, die1.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

x_values = list(range(1, die1.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'结果'}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='投掷一个D6和D10 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6和d10.html')