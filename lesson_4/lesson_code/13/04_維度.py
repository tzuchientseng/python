import torch as tc

a = tc.tensor([[1., 2., 3.], [4., 5., 6.]])

print(a.shape) # 物件屬性，直接把變數取出，效能較高
print(a.size()) # 物件方法，執行此方法才產生結果，效能較差
print(a.shape[1])
print(a.size(1))

