import pickle

from sklearn.datasets import load_boston
import seaborn as sns
import pylab as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

display=pd.options.display
display.max_columns=None
display.max_rows=None
display.width=None
display.max_colwidth=None
datas=load_boston()
df=pd.DataFrame(data=datas.data, columns=datas.feature_names)
df.insert(0, column='PRICE', value=datas.target)
data=np.c_[df['LSTAT'],df['RM']]
x=pd.DataFrame(data=data, columns=['LSTA','RM'])
y=df['PRICE']

#分割資料, 80%訓練, 20%測試
#使用 scikit learn 的 train_test_split
#random_state=5 種下種子，每次分割的索引都一樣，方便開發時驗証用，等開發完成，把種子拿掉
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2, random_state=5)
#scikit learn 已建立好的模型
model=LinearRegression()
print("開始訓練(fit)....")
#有的資料太多，訓練的時間會很久(一整天，一整個月)
model.fit(x_train, y_train)

#模型儲存，有時可以 model.save, 若沒這個功能，則用 pickle
pickle.dump(model, open("house.model", "wb"))