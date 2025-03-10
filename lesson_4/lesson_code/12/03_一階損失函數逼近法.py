import pylab as plt
import numpy as np
from celluloid import Camera

fig = plt.figure(figsize=(9,6))
ax = plt.axes()
np.random.seed(1)
n = 20
x = np.linspace(-10,10 ,n)
y = 0.5*x+3 + np.random.randint(-5,5, n)

camera = Camera(fig)
epochs = 200
a = 0
b = 0
lr = 2.5e-3

for i in range(epochs):
    # ax.clear()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-8, 15)
    ax.plot([-15,15], [0,0], c='k', linewidth=0.5)
    ax.plot([0,0], [-8,15], c='k', linewidth=0.5)
    ax.scatter(x, y, c='r')
    f = np.poly1d(np.polyfit(x, y, 1))
    ax.plot(x, f(x), c="b", linewidth=5)

    # 開始梯度下降
    # 一階迴歸線的公式 y = ax + b
    y_pred = a * x + b
    da = ((y_pred - y) * (x ** 1)).sum()
    db = ((y_pred - y)).sum()

    a = a - da * lr
    b = b - db * lr

    # 計算損失的值
    y_pred = a * x + b
    loss = np.square((y-y_pred)).sum()
    print(loss)

    ax.plot(x, a * x + b, c='g', linewidth=1)

    plt.pause(0.1)
    camera.snap()

animation = camera.animate()
animation.save("loss_1.gif", writer='PillowWriter', fps=10)
plt.show()
