import pylab as plt
import numpy as np
t = np.linspace(0,10,100)
a = 9.8
v = a*t
s = (1 / 2) * a * (t ** 2)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].plot(t, s)
axes[1].plot(t, v)
plt.show()

#微分，就是求曲線(面，超平面)的斜率
