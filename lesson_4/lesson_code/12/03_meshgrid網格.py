import numpy as np
import pylab as plt
# x = [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]
# y = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
x, y = np.meshgrid(range(5), range(5))
print(x)
plt.scatter(x, y, c='b') # x, y 也吃二維的資料
plt.show()