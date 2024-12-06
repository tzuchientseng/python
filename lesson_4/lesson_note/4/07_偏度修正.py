import pickle
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
import pylab as plt
datas = load_boston()
df = pd.DataFrame(data=datas.data, columns=datas.feature_names)
df.insert(0, column='PRICE', value=datas.target)
# skewness[ˋskjunɪs] : 偏度
lstat = df['LSTAT']**(1/3) # 負相關 : 開根號接近距離
# skew 為正值，重心偏左邊
# skew 為負值，重心偏右邊
# skew 愈接近 0 愈好
skew = lstat.skew()
sns.histplot(lstat, kde=True)
print(skew)
# plt.show()

# rm = df['RM']**(1/2) # skew 接近0，分數反而降低(0.71 -> 0.69)
rm = df['RM']**(2) # 房間數愈多愈貴，是正相關，接開距離
data = np.c_[lstat,rm]


x = pd.DataFrame(data=data, columns=['LSTA','RM'])
y = df['PRICE']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=5)
model = LinearRegression()
print("開始訓練(fit)....")
model.fit(x_train, y_train)
score = model.score(x_test, y_test)
print(score) # 不是精準度，而是信心度
pre_price = model.predict(x_test)
for i in zip(pre_price, y_test):
    print(i)
