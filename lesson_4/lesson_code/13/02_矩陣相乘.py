import torch as tc
a = tc.tensor([[1,2],[3,4],[5,6]])
b = tc.tensor([[1,2,3],[4,5,6]])
print(tc.mm(a,b)) # 類別方法
print(a.mm(b)) # 物件方法，會偏重此法

