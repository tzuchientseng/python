import time
#time stamp : 1970/01/01 0:0:0 到現在所經過的秒數
print(time.time())
#pip install matplotlib
import pylab as plt
import numpy as np
x=np.random.uniform(0,1,1000)#平均份佈
y=np.random.uniform(0,1,1000)
# x=np.random.normal(size=1000)#標準常態分佈
# y=np.random.normal(size=1000)
plt.scatter(x,y)

x=np.random.uniform(0,1,100)#平均份佈
y=np.random.uniform(0,1,100)
plt.scatter(x,y,c='r')
plt.show()