# 假設這個世界上沒有微分，是否有其它方法求極值
import threading
import time

import numpy as np
import pylab as plt

def f(x):
    return np.square(x)

def df(x): # 一次微分
    return 2*x

def bias(a, x): # 偏移量
    return f(x)-a*x

def run(): # 製作動畫的地方
    xs = np.linspace(-5, 5, 100)
    ys = f(xs)
    x = -5
    points = [x]
    for i in range(epochs):
        ax.clear()
        ax.set_xlim(-10,10)
        ax.set_ylim(-10,30)
        plt.plot(xs, ys)
        print(f(points))
        plt.scatter(points, f(points), c='r')
        plt.draw() # 重新渲染
        time.sleep(0.1)

plt.figure(figsize=(10,6))
epochs = 200
lr = 0.2 # learning rate 學習率，x軸每次步進的值
ax = plt.subplot()
# 不懂執行緒，沒有任何專案作的出來
t = threading.Thread(target=run)
t.start()
plt.show()
