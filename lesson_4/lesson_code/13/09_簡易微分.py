import torch as tc
#1. 要微分的變數要加 requires_grad=True
#2. y.backward()微分後，如果值不是標量，就要用 tc.ones([])產生可以讓微分暫存的地方
#3. 切記不要輕信網路上所用的 Vaiable
#4. x 必需是小數，才可以微分

x = tc.tensor([1., 2., 3., 4.], requires_grad=True)#告知 x 要進行微分
y = tc.square(x)
print(x)
print(y)
#底下會產生只允計標量輸出的錯誤
#grad can be implicitly created only for scalar outputs
#scalar 標量，也就是純量，0 維數組
#y.backward()#開始計算微分

a=tc.tensor(5)#此為標量
b=tc.tensor([1])#不是標量

#網路上寫說要用
#from torch.autograd import Variable
#x=tc.Variable(tc.tensor([1.,2.,3.,4.]))
#但 Variable 要被淘汰了，不要用

#底下要產生跟 x 同大小的空間，裏面都是 1，當微分時，會和 1 相乘
#所以一定要用 ones
y.backward(tc.ones([x.shape[0]]))
print(x.grad)#取得 x 的微分值，此處沒有計算