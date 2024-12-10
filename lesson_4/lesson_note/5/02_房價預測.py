"""
pip uninstall scikit-learn 
# boston 房價 由於道德問題 scikit-learn維護者 強烈反對使用
pip install scikit-learn==1.1.3
"""
from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor as LOF

display = pd.options.display
display.max_columns = None
display.max_rows = None
display.width = None
display.max_colwidth = None

boston_dataset = load_boston()
df = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
df.insert(0, column="PRICE", value=boston_dataset.target)
df = df[['PRICE','LSTAT','RM']]

x = df[['LSTAT','RM']]
y = df['PRICE']

# lof = LOF(n_neighbors=20, contamination=auto) # 太過鬆散
lof = LOF(n_neighbors=20, contamination=0.1) # 嚴謹
data = np.c_[x, y]
y_pred = lof.fit_predict(data)

# df.loc : 列
df = pd.DataFrame(data=df.loc[np.where(y_pred==1)].values, columns=['PRICE','LSTAT','RM'])
data = np.c_[df['LSTAT']**(1/3),df['RM']]

x = pd.DataFrame(data=data, columns=['LSTAT','RM'])
y = df['PRICE']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)
model = LinearRegression() # 線性迴歸模型
model.fit(x_train, y_train)
print(f'分數 : {model.score(x_test, y_test)}')
y_pred = model.predict(x_test)
for i in zip(y_pred, y_test):
    print(i)
