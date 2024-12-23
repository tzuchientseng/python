import random
random.seed(1)
a = [1, 2, 3, 4, 5]
b = ['a','b','c','d','e']
c = list(zip(a,b))
random.shuffle(c)
print(c)
print(*c)
# 經過第二次 zip, 又組合成 a 及 b , 但順序混淆了
a, b = zip(*c)
print(a)
print(b)
