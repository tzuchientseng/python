#pip install matplotlib
import numpy as np
np.random.seed(1)
def getData(n):
    x = np.arange(-5, 5.1, 10 / n)
    y = 3 * x + 2 + (np.random.rand(len(x)) - 0.5) * 20
    return x, y
def getContour(x,y):#等高線
    a = np.arange(-10, 16, 1)
    b = np.arange(-10, 16, 1)
    mesh=np.meshgrid(a,b)
    loss=np.zeros([len(a), len(b)])
    for p_x, p_y in zip(x,y):
        loss+=((mesh[0]*p_x+mesh[1])-p_y)**2
    loss/=len(x)
    return mesh, loss
