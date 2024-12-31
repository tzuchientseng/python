# copy training.1600000.processed.noemoticon.csv
# pip install scikit-learn nltk gensim tensorflow==2.10.1 pandas
# LSTM(Long short-term memory) 情緒偵測

import pickle
import re
import time
import nltk
import pandas as pd
from gensim.models import Word2Vec
from keras_preprocessing.text import Tokenizer
from nltk import SnowballStemmer # 詞幹提取
from nltk.corpus import stopwords # 停用詞
from sklearn.model_selection import train_test_split
import numpy as np

def preprocess(text, stem=False):
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if token not in stop_words:
            if stem:
                tokens.append(stemmer.stem(token))
            else:
                tokens.append(token)
    return " ".join(tokens)

def decode_sentiment(label):
    return decode_map[int(label)]

DATASET_COLUMNS = ["target", "ids", "date", "flag", "user", "text"]
TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

nltk.download('stopwords')
stop_words = stopwords.words("english")
stemmer = SnowballStemmer("english")

df = pd.read_csv('training.1600000.processed.noemoticon.csv',
                 encoding="ISO-8859-1",
                 names=DATASET_COLUMNS)

"""
datas = []
for line in df.text:
    line = preprocess(line)
    date = append(line)
"""
df.text = df.text.apply(lambda x: preprocess(x))

df_train, df_test, = train_test_split(df, test_size=0.2, random_state=1)

# 製作字典統計單字並編號
print("製作字典中....")
t1 = time.time()

toz = Tokenizer()
toz.fit_on_texts(df_train.text)
vocab_size = len(toz.word_index) + 1 # 因為編號從 1 開始

t2 = time.time()
print(f'製作字典共花費 : {t2 - t1}秒, 共有 {vocab_size} 個單字')

# fit_on_texts 很多花時間，所以先把字典儲存起來
pickle.dump(toz, open("eng_dictionary.pkl","wb"),protocol=0)
decode_map = {0:"負面的", 2:"中立的", 4:"正面的"}
# decode_map = {0:"Negative", 2:"Neutral", 4:"positive"}
# decode_map={0:"罵民進黨", 2:"罵國民黨", 4:"罵蔡英文",6:"罵馬英久"}

df.target = df.target.apply(lambda x: decode_sentiment(x)) # 將數字轉換成文字(mapping)

# 取得每個字的 100個 權重，首先要知道共有幾個字
weight = np.zeros([vocab_size, 100])

# Word2Vec: 同義詞的向量值比較接近，　不同義詞向量值比較遠，每個字有 100 個向量(權重)
w2v_model = Word2Vec.load("w2v_model")

for word, i in toz.word_index.items():
    if word in w2v_model.wv:
        weight[i] = w2v_model.wv[word]

'''
# 向量概念
天氣狀況
星期 1 : 最低 20度, 最高 30度, 下雨 .83
星期 2 : 最低 22度, 最高 29度, 下雨 .39
星期 3 : 最低 25度, 最高 28度, 下雨 .20

[1
20
30
0.83
]
[
2
22
29
.39
]
[
3
25
28
.20
]
'''
