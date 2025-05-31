# f(x,y) = x^5+y^6-0.8x^4.....
# 任何一個曲面，都可以用二元方程式來表示
# 所以地型圖也可以用二元方程式表示
# pip install plotly pandas
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# 配置 Pandas 顯示選項
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.width = None
pd.options.display.max_colwidth = None

# 定義網格大小
n = 100

# 初始化 z 為二維陣列
z = np.zeros([n, n])

# 填充 z 陣列
for x in range(n):
    for y in range(n):
        z[x, y] = (0.0006 * x ** 6 - 0.005 * y ** 6 + 0.5 * x ** 5 
                   - 0.1 * y ** 5 + 0.005 * x ** 4 + 0.003 * y ** 4) / 10000000

# 繪製 3D 曲面
trace = go.Surface(z=z)
data = [trace]
layout = go.Layout(
    title='3D Surface Plot',
    autosize=True,
    margin=dict(l=0, r=0, b=0, t=0)  # 設置圖形邊距
)

# 創建圖形並顯示
# 顯示在 http://127.0.0.1:4771/
fig = go.Figure(data=data, layout=layout)
fig.show()
