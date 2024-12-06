import pickle
from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # 分割 80% 訓練 20% 測試
from sklearn.linear_model import LinearRegression

# 載入加州房價數據集
california = fetch_california_housing()
df = pd.DataFrame(data=california.data, columns=california.feature_names)
df['PRICE'] = california.target  # 目標值

# 篩選我們感興趣的特徵 ('MedInc' 和 'AveRooms') 來模仿原始範例
data = np.c_[df['MedInc'], df['AveRooms']]  # 'MedInc': 中位收入, 'AveRooms': 平均房間數
x = pd.DataFrame(data=data, columns=['MedInc', 'AveRooms'])
y = df['PRICE']

# 拆分訓練集與測試集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)

# 建立與訓練模型
model = LinearRegression()
print("Start Training!")
model.fit(x_train, y_train)

# 儲存模型
pickle.dump(model, open("house.model", 'wb'))

# 載入模型及進行預測
loaded_model = pickle.load(open("house.model", 'rb'))
score = loaded_model.score(x_test, y_test)
print(f"Model Confidence Score: {score:.2f}")  # 信心度

# 開始預測
pre_price = loaded_model.predict(x_test)
for predicted, actual in zip(pre_price, y_test):
    print(f"Predicted: {predicted:.2f}, Actual: {actual:.2f}")

"""
import pickle
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

datas = load_boston()
df = pd.DataFrame(data=datas.data, columns=datas.feature_names)
df.insert(0, column='PRICE', value=datas.target)
data = np.c_[df['LSTAT'],df['RM']]
x = pd.DataFrame(data=data, columns=['LSTA','RM'])
y = df['PRICE']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=5)

# 模型載入及預測
model = pickle.load(open("house.model",'rb'))
score = model.score(x_test, y_test)
print(score) # 不是精準度，而是信心度
# predict : 開始預測
pre_price = model.predict(x_test)
for i in zip(pre_price, y_test):
    print(i)
print(np.c_[pre_price, y_test])
"""
