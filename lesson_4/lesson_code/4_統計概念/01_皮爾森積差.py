#pip numpy as np
#1. 平均數及標準差的計算
#2. 皮爾森積差計算那些特徵對房價的影響較大
#3. 列出影響較大的特徵，進行模型訓練，最後再預測
#4. 修正Skewness(偏度)，將特徵的重心移到中心，再重新訓練及預測
#5. 計算 LOF(局部離群因子)，將二個特徵(RM/LSTAT)裏面的異常值刪除，再重新訓練及預測
#6. 想想看有啥辦法(演算法)將訓練後的預測分數加大
import numpy as np
np.random.seed(1)
x = np.random.randint(1,100,10)
y = np.random.randint(1,100,10)
xmean = x.mean()
ymean = y.mean()
print(x) # [38 13 73 10 76  6 80 65 17  2]
print(y) # [77 72  7 26 51 21 19 85 12 29]
print(xmean)
# x-xmean : [  0. -25.  35. -28.  38. -32.  42.  27. -21. -36.]
# y-ymean : [ 37.1  32.1 -32.9 -13.9  11.1 -18.9 -20.9  45.1 -27.9 -10.9]
# convariance : 0*37.1+-25*32.1+......
convariance = np.sum((x - xmean) * (x - xmean)) # 共變數
print(x - xmean)
print(y - ymean)
print(convariance)

# 計算x及y的 標準差
xd = np.sqrt(np.square(x - xmean).sum())
yd = np.sqrt(np.square(y - ymean).sum())
print(xd, yd)
p = convariance / (xd * xd)
print("手動計算:",p)
import pandas as pd
df = pd.DataFrame(data={"x":x, "y":y})
# numpy : 難pi
# Django : 尖狗，不是jungle
# kotlin : ka
p = df.corr() # 讀音[ˋkɔrnɚ] correlation
print(p)

# 公式 :https://latex.codecogs.com/eqneditor/editor.php
# \sum_{i=1}^{n}({x_{i}-\bar{x}})({x_{i}-\bar{x}}) = {\sqrt{\sum_{i=1}^{n}(x_i-\overline{x})^2}\sqrt{\sum_{i=1}^{n}(x_i-\overline{x})^2}}
# \sum_{i=1}^{n}({x_{i}-\bar{x}})({y_{i}-\bar{y}}) = {\sqrt{\sum_{i=1}^{n}(x_i-\overline{x})^2}\sqrt{\sum_{i=1}^{n}(y_i-\overline{y})^2}}
"""
[38 13 73 10 76  6 80 65 17  2]
[77 72  7 26 51 21 19 85 12 29]
38.0
[  0. -25.  35. -28.  38. -32.  42.  27. -21. -36.]
[ 37.1  32.1 -32.9 -13.9  11.1 -18.9 -20.9  45.1 -27.9 -10.9]
9332.0
96.60227740586657 86.78075823591311
手動計算: 1.0
          x         y
x  1.000000  0.093043
y  0.093043  1.000000
"""