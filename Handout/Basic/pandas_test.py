import numpy as np
import pandas as pd

print("----------------------------------------", 'Test', "-"*40)
data_dict = {
    'name': ['David', 'Tim', 'Alice'],
    'age': [19, 23, 22]
}

pandas_df = pd.DataFrame(data_dict)

df = pd.DataFrame(columns=['age', 'score'])
df['score'] = np.random.randint(100, size=(10)) #0~99
df['age'] = np.random.randint(25, size=(10)) #0~24
print(df)

import matplotlib.pyplot as plt
df.plot(x='age', y='score', kind='scatter')
# plt.show()
# plt.savefig('scatter_plot.png')

sorted_df = df.sort_values(by = ['age'])
print(sorted_df)

print("----------------------------------------", 'Test', "-"*40)
data_url = 'https://raw.githubusercontent.com/turingplanet/pandas-intro/main/public-datasets/iris.csv'
iris_data_df = pd.read_csv(data_url)
iris_data_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].plot()
iris_data_df.info()
iris_data_df.describe(include='all')
iris_data_df['sepal_length'] = np.nan
iris_data_df['sepal_length'].max()
# print(iris_data_df)
# plt.show()

print("----------------------------------------", 'Test', "-"*40)
