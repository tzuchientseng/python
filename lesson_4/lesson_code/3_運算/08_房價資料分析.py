#pip install scikit-learn==1.1.3 seaborn
#請注意，不能安裝最新版本，因為1.2已把波士頓房價資料拿掉了
from sklearn.datasets import load_boston
import pandas as pd
#DataFrame 完美列印
display=pd.options.display
display.max_columns=None
display.max_rows=None
display.width=None
display.max_colwidth=None

datas=load_boston()
#有13個特徵，影響房價的因素
df=pd.DataFrame(data=datas.data, columns=datas.feature_names)
df.insert(0, column="PRICE", value=datas.target)
print(df)
#print(datas.DESCR)#列出每個欄位的說明
#LSTAT : 中低收入戶人口比例
#RM : 每棟房子的房間數

#EDA(Explorator Data Analysis)資料分析探索
#了解每個房價的分佈, 那些特徵(因素)最會影響房價，那些特徵對房價沒影響

#海生圖，在海量的資料中取得相關素，比如線性回歸，數量分佈
#底下的圖偏向左邊，右邊住豪宅的人比較少，會影響預測準度
#為啥? 郭台銘一個人就拉高很多國民平均所得，會不准
import seaborn as sns
import pylab as plt
sns.histplot(df['PRICE'],kde=True)

#皮爾森積差 : 計算那些特徵對房價影響最大
#學習方式 :
#1. 先記公式 :
#   是將每個特徵與其它特徵進行計算
#   公式為 : 共變異數(協方差)/(x標準差 * y標準差(不除以n))，值介於 -1~1之間
#2. 了解圖型
#3. 深入數學

# plt.show()
