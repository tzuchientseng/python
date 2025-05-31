import torch as tc

b=tc.randint(0,10,[100])#不含10，[1*100]

print(b)

# pip install matplotlib
c = tc.rand([2,1000]) # 平均分佈，介於0~1之間

print(c)
print(c[0,:]) # 等同 c[0]

import pylab as plt

plt.subplot(1,3, 1)
plt.scatter(c[0], c[1], c='b', s=5)
plt.title('rand')

plt.subplot(1,3,2)
d = tc.randn(2,1000) # 常態分佈，接近0的機率較大

plt.scatter(d[0], d[1], s=5)
plt.title('randn')

plt.subplot(1,3,3)
e = tc.normal(200,100,[2,1000]) # 也是常態分佈，但中心點可以改變
plt.scatter(e[0], e[1], s=5)
plt.title('normal')
plt.show()

