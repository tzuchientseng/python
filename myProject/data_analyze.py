import os
import subprocess
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
from statistic import * #My Module

# 呼叫爬蟲腳本
def run_scraper(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    try:
        result = subprocess.run(['python', script_path], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e.stderr}")

# # 執行爬蟲腳本
# run_scraper('Scraper_NVDA.py')
# run_scraper('Scraper_QUANTA.py')

# 定義 CSV 文件路徑
NVDA = os.path.join(os.path.dirname(__file__), 'csv/NVDA.csv')
QUANTA = os.path.join(os.path.dirname(__file__), 'csv/QUANTA.csv')

# 讀取 CSV 文件並打印內容
df_NVDA = pd.read_csv(NVDA, encoding='utf-8')
df_QUANTA = pd.read_csv(QUANTA, encoding='utf-8')

# 轉換日期列為日期格式
df_NVDA['日期'] = pd.to_datetime(df_NVDA['日期'])

# 將民國年格式轉換成西元年格式
def convert_taiwan_year(date_str):
    year, month, day = date_str.split('/')
    year = str(int(year) + 1911)
    return f"{year}-{month}-{day}"

df_QUANTA['日期'] = df_QUANTA['日期'].apply(convert_taiwan_year)
df_QUANTA['日期'] = pd.to_datetime(df_QUANTA['日期'])

# 確保數據是字串，移除數字中的逗號並轉換為浮點數
df_NVDA['收市'] = df_NVDA['收市'].astype(str).str.replace(',', '').astype(float)
df_QUANTA['收盤價'] = df_QUANTA['收盤價'].astype(str).str.replace(',', '').astype(float)

# print('-'*40, "NVDA-<class 'pandas.core.frame.DataFrame'>", '-'*40)
# print(df_NVDA)

# print('-'*40, "QUANTA-<class 'pandas.core.frame.DataFrame'>", '-'*40)
# print(df_QUANTA)

# # 基本統計分析
# print('-'*40, "NVDA-Describe() statitic", '-'*40)
# print(df_NVDA.describe())
# print('-'*40, "QUANTA-Describe() statitic", '-'*40)
# print(df_QUANTA.describe())

# # NVDA 收市價走勢圖
# plt.figure(figsize=(10, 5))
# plt.plot(df_NVDA['日期'], df_NVDA['收市'], label='NVDA')
# plt.xlabel('Day')
# plt.ylabel('Price')
# plt.title('NVDA closing price trend')
# plt.legend()
# plt.show()

# # QUANTA 收盤價走勢圖
# plt.figure(figsize=(10, 5))
# plt.plot(df_QUANTA['日期'], df_QUANTA['收盤價'], label='QUANTA')
# plt.xlabel('Day')
# plt.ylabel('Price')
# plt.title('QUANTA closing price trend')
# plt.legend()
# plt.show()

print("----------------------------------------", '使用 scipy 計算 95% 信賴區間(著重運算速度模組各樣運算模組)', "-"*40)
def mean_confidence_interval_scipy(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    sem = stats.sem(data)
    h = sem * stats.t.ppf((1 + confidence) / 2, n - 1)
    return mean, mean - h, mean + h
nvda_mean_scipy, nvda_ci_low_scipy, nvda_ci_high_scipy = mean_confidence_interval_scipy(df_NVDA['收市'])
quanta_mean_scipy, quanta_ci_low_scipy, quanta_ci_high_scipy = mean_confidence_interval_scipy(df_QUANTA['收盤價'])
print(f"NVDA 平均收市價 (scipy): {nvda_mean_scipy}, 95% 信賴區間: [{nvda_ci_low_scipy}, {nvda_ci_high_scipy}]")
print(f"QUANTA 平均收盤價 (scipy): {quanta_mean_scipy}, 95% 信賴區間: [{quanta_ci_low_scipy}, {quanta_ci_high_scipy}]")


print("\n----------------------------------------", '使用 statsmodels 計算 95% 信賴區間(著重統計模組)', "-"*40)
def mean_confidence_interval_statsmodels(data, confidence=0.95):
    mean = np.mean(data)
    ci = sm.stats.DescrStatsW(data).tconfint_mean(alpha=1-confidence)
    return mean, ci
nvda_mean_statsmodels, nvda_ci_statsmodels = mean_confidence_interval_statsmodels(df_NVDA['收市'])
quanta_mean_statsmodels, quanta_ci_statsmodels = mean_confidence_interval_statsmodels(df_QUANTA['收盤價'])
print(f"NVDA 平均收市價 (statsmodels): {nvda_mean_statsmodels}, 95% 信賴區間: [{nvda_ci_statsmodels[0]}, {nvda_ci_statsmodels[1]}]")
print(f"QUANTA 平均收盤價 (statsmodels): {quanta_mean_statsmodels}, 95% 信賴區間: [{quanta_ci_statsmodels[0]}, {quanta_ci_statsmodels[1]}]")

print("\n----------------------------------------", '使用自己的module 計算 95% 信賴區間', "-"*40)
confidence_level = 95  # 95% confidence level
Descriptive_stats = DesData(df_NVDA['收市'])
print("\n----------------------------------------", "NVIDIA", "-"*40)
print(Descriptive_stats.strBound(confidence_level))
Descriptive_stats2 = DesData(df_QUANTA['收盤價'])

print("\n----------------------------------------", "QUANTA", "-"*40)
print(Descriptive_stats2.strBound(confidence_level))

Inferential_two_stats = Infer2Data(df_NVDA['收市'], df_QUANTA['收盤價'])
print()
print("\n----------------------------------------", "推論統計: NVIDIA/QUANTA", "-"*40)
print(Inferential_two_stats.two_sample_t_test())

print("\n----------------------------------------", '透過Scipy計算 f統計量 及 p-值', "-"*40)
df_NVDA['日漲跌幅'] = df_NVDA['收市'].pct_change() * 100
df_QUANTA['日漲跌幅'] = df_QUANTA['收盤價'].pct_change() * 100
# print(df_NVDA[['日期', '日漲跌幅']])
# print(df_QUANTA[['日期', '日漲跌幅']])
z1, z2 = stats.f_oneway(df_NVDA['日漲跌幅'].dropna(), df_QUANTA['日漲跌幅'].dropna()) #dropna()丟掉Nan缺失值
print("f-統計量:", z1)
print("p-value:", z2)
if z2 < 0.05:
    print("有個別主效應或交互作用")
else:
    print("無個別主效應及交互作用")

print("\n----------------------------------------", '透過panda計算f統計量及p-值再透過pyplot畫圖', "-"*40)
# 計算兩家公司收盤價的相關係數
df_combined = pd.merge(df_NVDA[['日期', '收市']], df_QUANTA[['日期', '收盤價']], on='日期', how='inner')
correlation = df_combined['收市'].corr(df_combined['收盤價'])

print(f"兩家公司收盤價的相關係數: {correlation}")

plt.figure(figsize=(10, 5))
plt.plot(df_combined['日期'], df_combined['收市'], label='NVDA closing price')
plt.plot(df_combined['日期'], df_combined['收盤價'], label='QUANTA closing price')
plt.xlabel('Day')
plt.ylabel('Price')
plt.title('Comparison of closing price trends between NVDA and QUANTA')
plt.legend()
plt.show()


"""
# 計算移動平均線
df_NVDA['5日移動平均'] = df_NVDA['收市'].rolling(window=5).mean()
df_QUANTA['5日移動平均'] = df_QUANTA['收盤價'].rolling(window=5).mean()

plt.figure(figsize=(10, 5))
plt.plot(df_NVDA['日期'], df_NVDA['收市'], label='NVDA 收市價')
plt.plot(df_NVDA['日期'], df_NVDA['5日移動平均'], label='NVDA 5日移動平均')
plt.xlabel('Day')
plt.ylabel('Price')
plt.title('NVDA closing price and 5-day moving average')
plt.legend()
plt.show()

# 計算成交量變化
df_NVDA['成交量變化'] = df_NVDA['成交量'].str.replace('M', '').str.replace(',', '').astype(float).pct_change() * 100
df_QUANTA['成交量變化'] = df_QUANTA['成交量'].str.replace(',', '').astype(float).pct_change() * 100
print(df_NVDA[['日期', '成交量變化']])
print(df_QUANTA[['日期', '成交量變化']])
"""

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

with open(QUANTA, encoding='utf-8') as fobj3:
    content3 = csv.reader(fobj3)
    list_QUANTA = list(content3)
    print('-'*40,"QUANTA",'-'*40)
for row in list_QUANTA:
    print(row)
"""