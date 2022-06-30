import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(1,1,s=200)
ax.scatter(2,4,s=200)
ax.scatter(3,9,s=200)
ax.scatter(4,16,s=200)
ax.scatter(5,25,s=200)
plt.show()