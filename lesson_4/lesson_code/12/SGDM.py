from MBGD import MBGD
import numpy as np
#SGDM 是 MBGD 的改良，是繼承 MBGD, 而不是繼承 SGD
class SGDM(MBGD):
    def __init__(self, a, b, x, y, lr, batch_size, gamma):
        super().__init__(a, b, x, y, lr, batch_size)
        self.gamma=gamma
        self.ma=0
        self.mb=0
    def update(self):
        grad_a, grad_b = self.gradient()
        self.a_old=self.a
        self.b_old=self.b
        self.ma = self.gamma * self.ma + self.lr * grad_a
        self.mb = self.gamma * self.mb + self.lr * grad_b
        self.a -= self.ma
        self.b -= self.mb
        self.loss = np.mean(((self.a * self.x + self.b) - self.y) ** 2)

