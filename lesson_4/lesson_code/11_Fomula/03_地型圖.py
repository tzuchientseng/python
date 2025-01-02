import plotly
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv',
    dtype='float')

trace1=go.Surface(z=df.values)

n=df.shape[0]
z=np.zeros([n, n])
a = 0.9
b = 1.8
c = 50

for x in range(n):
    for y in range(n):
        z[x,y]=a*x+b*y+c

trace2 = go.Surface(z=z, coloraxis='coloraxis')
data = [trace1, trace2]

layout = go.Layout(title=f'Regression : a*x+b*y+c', autosize=True, margin=dict(l=0, r=0, b=0, t=40))
fig = go.Figure(data=data, layout=layout)
fig.show()
