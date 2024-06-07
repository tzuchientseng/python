"""
import os 
import csv
NVDA = os.path.join(os.path.dirname(__file__), 'csv/NVDA.csv')
TSMC =  os.path.join(os.path.dirname(__file__), 'csv/2320TSMC.csv')
QUANTA = os.path.join(os.path.dirname(__file__), 'csv/2382QUANTA.csv')

with open(NVDA, encoding='utf-8') as fobj1:
    content1 = csv.reader(fobj1)
    list_NVDA = list(content1)
    print('-'*40,"NVDA",'-'*40)
for row in list_NVDA:
    print(row)

with open(TSMC, encoding='utf-8') as fobj2:
    content2 = csv.reader(fobj2)
    list_TSMC = list(content2)
    print('-'*40,"TSMC",'-'*40)
for row in list_TSMC:
    print(row)

with open(QUANTA, encoding='utf-8') as fobj3:
    content3 = csv.reader(fobj3)
    list_QUANTA = list(content3)
    print('-'*40,"QUANTA",'-'*40)
for row in list_QUANTA:
    print(row)
"""

import os
import pandas as pd #Panel Data(面板控制)

# 定義 CSV 文件路徑
NVDA = os.path.join(os.path.dirname(__file__), 'csv/NVDA.csv')
TSMC = os.path.join(os.path.dirname(__file__), 'csv/2320TSMC.csv')
QUANTA = os.path.join(os.path.dirname(__file__), 'csv/2382QUANTA.csv')

# 讀取 NVDA CSV 文件並打印內容
df_NVDA = pd.read_csv(NVDA, encoding='utf-8')
print('-'*40, "NVDA", '-'*40)
print(df_NVDA)

# 讀取 TSMC CSV 文件並打印內容
df_TSMC = pd.read_csv(TSMC, encoding='utf-8')
print('-'*40, "TSMC", '-'*40)
print(df_TSMC)

# 讀取 QUANTA CSV 文件並打印內容
df_QUANTA = pd.read_csv(QUANTA, encoding='utf-8')
print('-'*40, "QUANTA", '-'*40)
print(df_QUANTA)
