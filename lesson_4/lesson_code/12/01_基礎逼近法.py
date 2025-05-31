# 動畫製作
# animation.FuncAnimation :某此梯度法無法製作
# threading : 無法儲存動畫
# 最佳解 : 在主執行緒中，使用 plt.pause(秒數)
# 使用 celluloid (賽璐珞) 儲存動畫

# 假設這個世界上沒有微分，是否有其它方法求極值
# pip install matplotlib celluloid
# import threading
# import time

import numpy as np
import pylab as plt
from celluloid import Camera
def f(x):
    return np.square(x)
def df(x): # 一次微分
    return 2*x
def bias(a, x): # 偏移量
    # f(x) = a * x + b
    return f(x)-a*x

epochs = 200
lr = 0.2 # learning rate 學習率，x軸每次步進的值
xs = np.linspace(-5, 5, 100)
ys = f(xs)
x = -5
points = [x]
# plt.pause(0.01) 讓 plt 暫停 10 ms，讓主執行能夠處理視窗的更新及事件的偵測
# 1 秒 = 1,000,000,000ns  10ms=10,000,000 ns
fig = plt.figure(figsize=(9,6))
# ax = plt.subplot()
ax = plt.axes()
camera = Camera(fig)
for i in range(epochs):
    # ax.clear()#儲存動畫時，不能清除
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,30)

    # 畫曲線，及經過的點
    plt.plot(xs, ys,'g')
    print(f(points))
    plt.plot(points, f(points), 'ro')

    # 求微分，畫斜率線
    a = df(x) # y 對 x 的 微分，取得 x 點的斜率
    b = bias(a, x)
    x_l = x - 3
    x_r = x + 3
    line_x = [x_l, x_r]
    line_y = [a * (x_l) + b, a * (x_r) + b]
    plt.plot(line_x, line_y)

    # x往右逼近一點點
    x = x - a * lr
    points.append(x)
    plt.pause(0.1)
    camera.snap()
animation = camera.animate()

# MovieWriter ffmpeg unavailable; using Pillow instead.不用理會
animation.save("reg_basic.gif", writer='PillowWriter', fps=10)
# a = input('請輸入"q" 退出....')
# 網站架設 : Apache + PHP + MySQL + Wordpress
