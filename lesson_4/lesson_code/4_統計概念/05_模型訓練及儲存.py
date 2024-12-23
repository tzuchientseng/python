import pickle
from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load California Housing dataset
california_data = fetch_california_housing()
df = pd.DataFrame(data=california_data.data, columns=california_data.feature_names)
df.insert(0, column='PRICE', value=california_data.target)

# For simplicity, let's use the columns 'MedInc' and 'AveRooms' (similar concept to 'LSTAT' and 'RM')
data = np.c_[df['MedInc'], df['AveRooms']]
x = pd.DataFrame(data=data, columns=['MedInc', 'AveRooms'])
y = df['PRICE']

# Split the dataset: 80% for training, 20% for testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)

# Create a linear regression model
model = LinearRegression()
print("Starting training (fit)....")

# Train the model
model.fit(x_train, y_train)

# Save the trained model using pickle
pickle.dump(model, open("california_house.model", "wb"))

print("Model training completed and saved successfully.")

"""
import pickle
from sklearn.datasets import load_boston
import seaborn as sns
import pylab as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

display = pd.options.display
display.max_columns = None
display.max_rows = None
display.width = None
display.max_colwidth = None
datas = load_boston()
df = pd.DataFrame(data=datas.data, columns=datas.feature_names)
df.insert(0, column='PRICE', value=datas.target)
data = np.c_[df['LSTAT'],df['RM']]
x = pd.DataFrame(data=data, columns=['LSTA','RM'])
y = df['PRICE']

# 分割資料, 80%訓練, 20%測試
# 使用 scikit learn 的 train_test_split
# random_state = 5 種下種子，每次分割的索引都一樣，方便開發時驗証用，等開發完成，把種子拿掉
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=5)
# scikit learn 已建立好的模型
model = LinearRegression()
print("開始訓練(fit)....")
# 有的資料太多，訓練的時間會很久(一整天，一整個月)
model.fit(x_train, y_train)

# 模型儲存，有時可以 model.save, 若沒這個功能，則用 pickle
pickle.dump(model, open("house.model", "wb"))
"""
