import torch as tc
a = tc.tensor([[1., 2., 3.], [4., 5., 6.]])
print(a)

# torch 轉 numpy
b = a.numpy()
print(b)

# numpy 轉 torch
c = tc.from_numpy(b)
print(c)

