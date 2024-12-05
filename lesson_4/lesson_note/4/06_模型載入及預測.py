import pickle
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

datas=load_boston()
df=pd.DataFrame(data=datas.data, columns=datas.feature_names)
df.insert(0, column='PRICE', value=datas.target)
data=np.c_[df['LSTAT'],df['RM']]
x=pd.DataFrame(data=data, columns=['LSTA','RM'])
y=df['PRICE']
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2, random_state=5)

#模型載入及預測
model=pickle.load(open("house.model",'rb'))
score=model.score(x_test, y_test)
print(score)#不是精準度，而是信心度
#predict : 開始預測
pre_price=model.predict(x_test)
for i in zip(pre_price, y_test):
    print(i)