import numpy as np
import pylab as plt
y1=np.random.randint(-10,50, 100)
count=len(y1)
x=list(range(count))
plt.plot(x, y1, 'bo', markersize=1)
mean=np.mean(y1)
plt.plot([0, count],[mean, mean],c='g')

std=np.std(y1)
std1=mean+std
plt.plot([0, count],[std1, std1],c='r')

std2=mean-std
plt.plot([0, count],[std2, std2],c='r')
plt.show()