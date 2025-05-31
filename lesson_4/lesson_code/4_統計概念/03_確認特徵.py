#確認RM/LSTAT是否有正相關或負相關
from sklearn.datasets import load_boston
import seaborn as sns
import pylab as plt
import pandas as pd

display = pd.options.display
display.max_columns = None
display.max_rows = None
display.width = None
display.max_colwidth = None
datas = load_boston()

df = pd.DataFrame(data=datas.data, columns=datas.feature_names)
df.insert(0, column='PRICE', value=datas.target)
features = ['LSTAT','RM']

for i , col in enumerate(features):
    # 子繪圖區 :
    plt.subplot(1, len(features), i+1)
    x = df[col]
    y = df['PRICE']
    plt.scatter(x,y)
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('PRICE')

plt.show()