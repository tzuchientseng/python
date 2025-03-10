#mesh[mɛʃ] 篩孔, 網線
import numpy as np
a = range(5)
b = range(5)
x, y = np.meshgrid(a,b)
print(x) # 列出每列的 x 軸座標
print(y) # 列出每列的 y 軸座標

mesh = np.meshgrid(a,b)
print(mesh)