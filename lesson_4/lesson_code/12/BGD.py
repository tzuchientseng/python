import numpy as np
class BGD():
    def __init__(self, a, b, x, y, lr):
        self.a=a
        self.b=b
        self.x=x
        self.y=y
        self.a_old=a
        self.b_old=b
        self.lr=lr
        self.loss=None
    #底下的偏微分，必需自已手動算一遍才看得懂
    def gradient(self):
        #底下使用 np.mean計算每個點的殘差平方總和再平均，如果有 10 億個點，就會算的要死
        #也就是損失函數要改良的地方
        #底下的方法稱為批次梯度下降法-BGD
        grad_a = 2 * np.mean((self.a * self.x + self.b - self.y) * (self.x))
        grad_b = 2 * np.mean(self.a * self.x + self.b - self.y)
        return grad_a, grad_b
    def update(self):#開始逼近
        grad_a, grad_b=self.gradient()
        self.a_old = self.a
        self.b_old = self.b
        self.a = self.a - self.lr * grad_a
        self.b = self.b - self.lr * grad_b
        print(self.a, self.b)
        self.loss = np.mean(((self.a * self.x + self.b) - self.y) ** 2)