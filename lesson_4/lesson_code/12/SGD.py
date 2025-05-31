from BGD import BGD
import numpy as np
class SGD(BGD):
    def __init__(self, a, b, x, y, lr):
        super().__init__(a,b,x,y,lr)
    def gradient(self):
        i=np.random.randint(len(self.x))
        grad_a = 2 * (self.a * self.x[i] + self.b - self.y[i]) * (self.x[i])
        grad_b = 2 * (self.a * self.x[i] + self.b - self.y[i])
        return grad_a, grad_b