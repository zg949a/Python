import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues, s=10)
plt.show()