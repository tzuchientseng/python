import torch as tc
#z=x^2+y^2
# x=tc.linspace(0,10, 11, requires_grad=True)
# y=tc.linspace(0,10, 11, requires_grad=True)
x=tc.tensor([1., 2., 3., 4.], requires_grad=True)
y=tc.tensor([3., 3., 3., 3.], requires_grad=True)
z=tc.square(x)+tc.square(y)
z.backward(gradient=tc.ones(x.shape[0]))
print(x.grad)
print(y.grad)