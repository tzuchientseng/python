import plotly.graph_objs as go
import numpy as np
import pandas as pd
import plotly
z=np.zeros([100,100])
for x in range(0,100):
    for y in range(0, 100):
        z[x, y]=(0.0006*x**6-0.005*y**6+0.5*x**5-0.1*y**5+0.005*x**4+0.003*y**4)/10000000
df=pd.DataFrame(data=z)
trace1=go.Surface(z=df.values) # 將dataframe所有的值以list列出
# 三維回歸面為 f(x,y)=ax+by+c
# 多階時，求取公式，如 ax^6+by^5+cx^4+dy^4+ex^3+.......
a = 0.9
b = 1.8
c = -200
for x in range(100):
    for y in range(100):
        z[x,y]=a*x+b*y+c

trace2 = go.Surface(z=z, coloraxis='coloraxis')
data = [trace1, trace2]
layout = go.Layout(title='3D', autosize=True,
                  margin=dict(l=50, r=50, b=50, t=50))

fig = go.Figure(data=data, layout=layout)
fig.show()
