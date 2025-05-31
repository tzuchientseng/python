import torch as tc
epochs = 10000
lr = 0.01
x=tc.tensor([-5.], requires_grad=True)
#y = tc.square(x)#公式不可以寫在這張
for i in range(epochs):
    y=tc.square(x)#當每次 x 軸有變, 公式就要建立一次
    y.backward()
    #x 每次微分，都會被追蹤，x 會被重建, requires_grad 就會消失
    # tc.no_grad()告知當 x 有變時，不要追蹤，只改裏面的值
    with tc.no_grad():
        x -= lr * x.grad
        print(x)
        x.grad.zero_()#清除，不然會被累加