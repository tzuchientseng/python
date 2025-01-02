# copy training.1600000.processed.noemoticon.csv
# pip install scikit-learn nltk gensim tensorflow==2.10.1 pandas

import os
import pickle
import re
import shutil
import time
import nltk
import pandas as pd
from gensim.models import Word2Vec
from keras import Sequential
from keras.callbacks import ReduceLROnPlateau, EarlyStopping
from keras.layers import Embedding, Dropout, LSTM, Dense
from keras.utils import pad_sequences
from keras_preprocessing.text import Tokenizer
from nltk import SnowballStemmer # 詞幹提取
from nltk.corpus import stopwords # 停用詞
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder

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

# 製作字典統計單字並編號
decode_map = {0:"負面的", 2:"中立的", 4:"正面的"}
# decode_map = {0:"Negative", 2:"Neutral", 4:"positive"}
# decode_map={0:"罵民進黨", 2:"罵國民黨", 4:"罵蔡英文",6:"罵馬英久"}

print("讀取csv檔案.....", end="")
t1=time.time()
df = pd.read_csv('training.1600000.processed.noemoticon.csv',
                 encoding="ISO-8859-1",
                 names=DATASET_COLUMNS)

t2=time.time()
print(f'花費時間 : {t2-t1:.4f}秒')

"""
datas = []
for line in df.text:
    line = preprocess(line)
    date = append(line)
"""
print("預處理字串.....", end="")
t1 = time.time()
df.text = df.text.apply(lambda x: preprocess(x))
df.target = df.target.apply(lambda x: decode_sentiment(x)) # 將數字轉換成文字(mapping)
print('df:', df)
t2 = time.time()
print(f'花費時間 : {t2-t1:.4f}秒')

#載入字典
with open("eng_dictionary.pkl", 'rb') as file:
    tok = pickle.load(file)
vocab_size = len(tok.word_index)

df_train, df_test, = train_test_split(df, test_size=0.2, random_state=1)
print("製作字典中....")
t1 = time.time()
toz = Tokenizer()
# toz.fit_on_texts(df_train.text)
toz.fit_on_texts(df.text)
vocab_size = len(toz.word_index) + 1 # 因為編號從 1 開始

t2 = time.time()
print(f'製作字典共花費 : {t2 - t1}秒, 共有 {vocab_size} 個單字')

# fit_on_texts 很多花時間，所以先把字典儲存起來
pickle.dump(toz, open("eng_dictionary.pkl", "wb"), protocol=0)

# 取得每個字的 100個 權重，首先要知道共有幾個字
weight = np.zeros([vocab_size, 100])

# Word2Vec: 同義詞的向量值比較接近，不同義詞向量值比較遠，每個字有 100 個向量(權重)
w2v_model = Word2Vec.load("w2v_model")

for word, i in toz.word_index.items():
    if word in w2v_model.wv:
        weight[i] = w2v_model.wv[word]

"""
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
"""

# x_train/x_test 送進去的句子
x_train = pad_sequences(toz.texts_to_sequences(df_train.text), maxlen=300)
x_test = pad_sequences(toz.texts_to_sequences(df_test.text), maxlen=300)
labels = df_train.target.unique().tolist()
labels.append("中立的")
# print("labels:", labels)

"""
# LabelEncoder
LabelEncoder 是 scikit-learn 裡的功能，主要是將字串轉成數字。如下一各個星球會依字串先排序再轉成 0~5 之間的數字。encoder.fit(planet) 會將字串排序並過濾重覆的單字，然後再用 encoder.transform(planet) 傳出每個單字出現的次數。
亦可直接使用 encoder.fit_transform(planet) 一步完成。
最後的 Counter 是 collections（集合的功能），主要是算出每個單字出現的次數。
from collections import Counter
from sklearn.preprocessing import LabelEncoder
planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "saturn", "Earth"]

encoder = LabelEncoder()
encoder.fit(planet)
x = encoder.transform(planet)
x = encoder.fit_transform(planet)
print(x)

c = Counter(planet)
print(c)

# output:
[3 4 0 2 1 5 0]
Counter({'Earth': 2, 'Mercury': 1, 'Venus': 1, 'Mars': 1, 'Jupiter': 1, 'saturn': 1})
"""

# y_train / y_test : 正向的，負面的，也就是判讀後的結果
encoder = LabelEncoder()
encoder.fit(df_train.target.tolist())
y_train = encoder.transform(df_train.target.tolist())
y_test = encoder.transform((df_test.target.tolist()))
# 轉成 n*1維度
# [[0]
# [0]
# [1]
# ]
y_train = y_train.reshape(-1, 1) # 轉成 n * 1的維度
y_test = y_test.reshape(-1, 1)

"""
建立模型
"""
model = Sequential()

# 第一層 Embedding(嵌入層) : 將文字轉換成向量 語意相近的字會有相近的向量
# keras 規定, Embedding 層只能作為模型的第一層
model.add( 
    Embedding(
        vocab_size,
        100, # Word2Vec每個字都有100個權重
        weights = [weight],
        input_length = 300,
        trainable = False
    )
)
# 第二層
model.add(Dropout(0.5)) # 故意去除一部份資料，怕過度擬合
# 第三層 LSTM(Long short-term memory) 情緒偵測
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
# 第四層
model.add(Dense(1, activation='sigmoid'))
# 編譯模型
model.compile( # 指定損失函數，那種梯度下降(BGD/SGD/MBGD...)，那一種優化器
    loss = 'binary_crossentropy', # 損失函數必需作梯度下降逼近法，裏面有一個學習率
    optimizer = 'adam', # 優化器就是在自動調整學習率
    metrics = ['accuracy']
)


# ReduceLROnPlateau : Reduce Learinig Rate : 模型訓練時，模型逐漸接近全局最小值，適度降低學習率，助於找到最佳解
# EarlyStopping : 當訓練集上的 loss 不再減少，就提早停止訓練
callbacks = [ReduceLROnPlateau(monitor='val_loss', patience=5, cooldown=0), 
             EarlyStopping(monitor='val_acc', min_delta=1e-4, patience=5)
             ]

"""
開始訓練模型
""" 
print("開始訓練模型......約需三小時")
t1 = time.time()
BATCH_SIZE = 1024 # 如果發生 OOM, 請調整這裏
# verbose : 0: 不輸出訊息, 1: 輸出進度條, 2: 為每個 epoch 輸出一行記錄
history = model.fit(
    x_train, y_train,
    batch_size=BATCH_SIZE,
    epochs=8,
    validation_split=0.1,
    verbose=1, # 提示的訊息
    validation_data=(x_test, y_test),
    callbacks=callbacks
)

t2 = time.time()
print(f"模型訓練共花費 {t2-t1}秒")

if os.path.exists("sentiment_model"):
    shutil.rmtree("sentiment_model")
model.save("sentiment_model")

import pylab as plt

score = model.evaluate(x_test, y_test, batch_size=BATCH_SIZE)
print(f"Loss : {score[0]}")
print(f"Accuracy : {score[1]}")

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']
x = range(len(acc))

plt.plot(x, acc, 'b', label='Training Acc')
plt.plot(x, val_acc, 'g', label='Validation Acc')
plt.plot(x, loss, 'r', label='Train loss')
plt.plot(x, val_loss, 'y', label='Validation loss')
plt.legend() # 顯示圖例
plt.show()
