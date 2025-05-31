#pip install matplotlib pandas plotly
import numpy as np
import pylab as plt
x = np.linspace(0,100, 10000000)
y = 0.001*(x**6)-0.1*(x**5)-0.68*(x**4)+10000*(x**2)+2
plt.plot(x,y)
# 損失函數的梯度下降逼近法，就是求回歸線的 a, b值
# args = np.polyfit(x ,y, 5)
# a = args[0]
# b = args[1]
# c = args[2]
# d = args[3]
# e = args[4]
# f = args[5]
# r = a*x**5+b*x**4+c*x**3+d*x**2+e*x+f
# print(args)
args = np.polyfit(x, y, 4)#超過6後，就過渡擬合，浪費時間計算
f = np.poly1d(args)
print(args)
# r = ax+b
# r = -258285.54*x+8838090.57
plt.plot(x,f(x))
plt.show()
