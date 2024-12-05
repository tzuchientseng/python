"""
pip install scikit-learn
pip install seaborn
"""
from sklearn.datasets import fetch_california_housing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DataFrame 完美列印
display = pd.options.display
display.max_columns = None
display.max_rows = None
display.width = None
display.max_colwidth = None

# 讀取 California Housing Dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame
p = df.corr()

# 對 MEDV 欄位，由大而小排序（California Housing 可能使用 `MedInc` 表示收入）
p = p.nlargest(len(p), columns='MedInc')

# 繪製熱度圖
sns.heatmap(p, annot=True, fmt='.2f', annot_kws={'size': 6})
plt.show()

from sklearn.datasets import fetch_openml
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DataFrame 完美列印
display = pd.options.display
display.max_columns = None
display.max_rows = None
display.width = None
display.max_colwidth = None

# 讀取 Ames Housing Dataset
housing = fetch_openml(name="house_prices", as_frame=True, parser='auto')
df = housing.frame

# 排除非數值欄位
numeric_df = df.select_dtypes(include=['number'])

# 計算相關係數
p = numeric_df.corr()

# 對目標欄位 SalePrice，由大而小排序
p = p[['SalePrice']].sort_values(by='SalePrice', ascending=False)

# 繪製熱度圖
plt.figure(figsize=(10, 8))
sns.heatmap(p, annot=True, fmt='.2f', annot_kws={'size': 6}, cmap="coolwarm")
plt.title("Correlation with SalePrice")
plt.show()

# # 涉及種族問題 無法使用 data
# from sklearn.datasets import load_boston
# import seaborn as sns
# import pylab as plt
# import pandas as pd

# # DataFrame 完美列印
# display = pd.options.display
# display.max_columns = None
# display.max_rows = None
# display.width = None
# display.max_colwidth = None

# datas = load_boston()
# df = pd.DataFrame(data=datas.data, columns=datas.feature_names)
# df.insert(0, column='PRICE', value=datas.target)
# # print(df)
# p = df.corr()

# # 對 price 欄位，由大而小排序
# p = p.nlargest(len(p), columns='PRICE')

# # annotation : 註釋，通知
# sns.heatmap(p, annot=True,fmt='.2f',annot_kws={'size':6})
# # 由上可知 price 與 RM(房子的房間數)及LSTAT(中低收入戶在此處的人口比例)有極強的關係

# print(p)
# plt.show()