from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import pylab as plt
datas = load_boston()
df = pd.DataFrame(data=datas.data, columns=datas.feature_names)
df.insert(0, column='PRICE', value=datas.target)

#開根號讓 skew 接近 0
rm = df['RM']**2

skew = rm.skew()
sns.histplot(rm, kde=True)
print(skew)
plt.show()