import numpy as np
import pylab as plt
x = np.linspace(-10,10, 100)
y = -x**2+5
plt.plot(x, y)
plt.show()
# 找極值(x多少，有最小的 y 值)
# y'=2x =0 ，所以 x=0, 所以 y=0**2+5 = 5

# 極大或極小?
# y''= 2 , >0時有極小值
# y''=-2 , <0時有極大值

# loss 損失函數(迴歸線)，實際與預測的差平方總和，愈小愈好，所以要求損失函數的極小值
# 有鞍點時，微分求極小值就失效了