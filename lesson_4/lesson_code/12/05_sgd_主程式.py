#SGD : 隨機梯度下降(Stochastic Gradient Descent)
#偏微分時不作加總：亂數取一個數來計算，很不穩定
from Regression import *
import pylab as plt
from SGD import SGD

np.random.seed(1)
x,y=getData(100)
fig, ax=plt.subplots(nrows=1, ncols=2, figsize=(12,4))

mesh, contour=getContour(x,y)
a2=ax[1].contourf(mesh[0], mesh[1], contour, 15,cmap=plt.cm.Purples)#contour : 只有線條, contourf加填滿色
plt.colorbar(a2, ax=ax[1])
ax[1].set_xlabel("a")
ax[1].set_ylabel("b")

#SGD開始
init_a=-9;init_b=-9
epoch=100
ax[1].scatter(init_a, init_b, c='g')

#底下二行是跟 BGD不一樣的地方
#有時收斂但又時又跳出來，所以不穩
lr=0.01
gd = SGD(init_a, init_b, x, y, lr)

#底下跟 BGD 一樣
for i in range(epoch):
    gd.update()#開始逼近，產生a,b loss
    ax[1].set_xlim(-10, 15)
    ax[1].set_ylim(-10, 15)
    ax[1].set_title(f"Epoch:{i+1:03d} Loss:{gd.loss:.6f}")
    ax[1].plot([gd.a_old, gd.a], [gd.b_old, gd.b], c='r')
    ax[1].scatter(gd.a, gd.b, c='g')

    ax[0].clear()
    ax[0].set_xlim(-5, 5)
    ax[0].set_ylim(-30, 30)
    ax[0].scatter(x, y, c='b')
    f = np.poly1d(np.polyfit(x, y, 1))
    ax[0].plot(x, f(x), c='g', linewidth=3)
    ax[0].plot([x[0], x[-1]],[gd.a*x[0]+gd.b, gd.a*x[-1]+gd.b], c='orange')
    ax[0].set_title(f'{gd.a:.6f}x+{gd.b:.6f}')

    plt.pause(0.01)
plt.show()