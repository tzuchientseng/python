# LOF (Local Outlier Factor 局部離群因子) 檔名不要用 LOF 不然會被蓋掉
# pip install scikit-learn matplotlib seaborn
import numpy as np
import pylab as plt
import seaborn as sns
from sklearn.neighbors import LocalOutlierFactor as LOF

np.random.seed(1)

# 產生二組100個標準常態分佈亂數，接近 0 的機率最大
inliners = np.random.randn(100, 2) # 100列 2欄
inliners = np.random.normal(size=[100, 2])
print(inliners)
ax1 = plt.subplot(1, 2, 1)
ax1.set_xlim(-5, 5)
ax1.set_ylim(0, 30)
sns.histplot(inliners[:, 0], kde=True) 

# 直方圖 : 表示選取所有行列 0 表示是第 0 列。
# kde表示是否要繪製核密度估計（KDE, Kernel Density Estimation）曲線
ax2 = plt.subplot(1, 2, 2)
ax2.set_xlim(-5, 5)
ax2.set_ylim(0, 30)
sns.histplot(inliners[:, 0], kde=True)
plt.show()
inliners = np.r_[inliners + 3, inliners - 3]
print(inliners.shape)

# 加入離群的點
outliners = np.random.uniform(low=-6, high=6, size=(20,2))
data = np.r_[inliners, outliners]

# x = data[:, 0]
# y = data[:, 1]
# plt.scatter(x, y, s=5, c='k') # k 表示黑色
# plt.show()

# 底下產生離群因子偵測器
# n_neighbors : k-distance(第 k 距離)，可以分群，預設值為 20
# contamination : 污染，異常值比例
lof = LOF(n_neighbors=20, contamination='auto')
# lof.fit() : 訓練
# lof.predict() : 偵測
# y_pred : 1代表沒有離群，-1代表為異常點
y_pred = lof.fit_predict(data)
print(y_pred)
# 印出分數
# 負值愈大，離群的機會就愈大
# print(lof.negative_outlier_factor_)
r = np.ones(len(y_pred))
r -= y_pred # 1->0, -1->2
print(r)
x = data[:, 0]
y = data[:, 1]
plt.scatter(x, y, s=3, c='k')
# 畫出異常點
# edgecolors : 外框線
# facecolors : 填滿色
# 切記 : c 不能指定
# plt.scatter(x, y, s=r*20, c='r')
plt.scatter(x, y, s=r*20, edgecolors='r', facecolors='none')
plt.show()
