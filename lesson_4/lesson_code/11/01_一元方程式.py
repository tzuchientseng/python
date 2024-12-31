# pip install matplotlib
# 任何一條曲線，都可以用一元多階方程式表示
# 上下凹凸點更多也可以，但公式會變很得猙獰，也很長很複雜

import numpy as np
import pylab as plt

# 定義數據範圍
x = np.linspace(0, 100, 1_000_000)

# 定義函數
y = 0.001 * (x ** 6) - 0.1 * (x ** 5) - 0.68 * (x ** 4) + 10000 * (x ** 2) + 2

# 繪製圖形
plt.plot(x, y)
plt.title("Polynomial Function Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)  # 添加網格線以便於觀察
plt.show()
