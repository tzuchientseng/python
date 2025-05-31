#損失函數 : 實際值與預測值的差平方總合
#預測值如果是迴歸線產生出來的，當然是計算迴歸線
#如果預測值是由 pca 產生的，那就是計算 pca 線
import pylab as plt
import numpy as np
from celluloid import Camera
fig=plt.figure(figsize=(9,6))
ax=plt.axes()
np.random.seed(1)
n=20
x=np.linspace(-10,10 ,n)
y=0.5*x+3 + np.random.randint(-5,5, n)

camera=Camera(fig)
epochs=500
a=0
b=0
c=0
d=0
e=0
lr=2.5e-3
y_pred = a * (x ** 4) + b * (x ** 3) + c * (x ** 2) + d * x + e
first_loss=10000
loss=0
for i in range(epochs):
# i=1
# while first_loss-loss>0.001:
    ax.clear()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-8, 15)
    ax.plot([-15,15], [0,0], c='k', linewidth=0.5)
    ax.plot([0,0], [-8,15], c='k', linewidth=0.5)
    ax.scatter(x, y, c='g')
    f=np.poly1d(np.polyfit(x, y, 4))
    ax.plot(x, f(x), c="b", linewidth=5)

    #開始逼近
    da = ((y_pred - y) * (x ** 4)).sum()
    db = ((y_pred - y) * (x ** 3)).sum()
    dc = ((y_pred - y) * (x ** 2)).sum()
    dd = ((y_pred - y) * x).sum()
    de = ((y_pred - y)).sum()

    a = a - da * lr / 1e6
    b = b - db * lr / 1e4
    c = c - dc * lr / 1e3
    d = d - dd * lr / 2
    e = e - de * lr / 1e0

    y_pred=a * (x ** 4) + b * (x ** 3)+ c * (x ** 2) +d * x + e
    ax.plot(x, y_pred, c='r', linewidth=1)
    loss=np.square(y_pred-y).sum()
    print(f'epochs : {i} : loss : {loss}')
    #i+=1
    plt.pause(0.01)

plt.show()