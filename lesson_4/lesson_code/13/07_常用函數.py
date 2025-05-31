import torch as tc
a = tc.linspace(0,10,10)

print(a)

b = tc.arange(1,10,2.5)
print(b)

# 計算平均數，每個值必需是小數
c = tc.tensor([1,2,3,4,5], dtype=tc.float32)

# 類別方法

print(tc.mean(c)) # (1+2+3+4+5)/5
print(tc.std(c))
print(tc.sum(c))

# 物件方法
print(c.mean())
print(c.std())
print(c.sum())

