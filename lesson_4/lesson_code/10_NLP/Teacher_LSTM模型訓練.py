#copy training.1600000.processed.noemoticon.csv
#pip install scikit-learn nltk gensim tensorflow==2.10.1 pandas
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
from nltk import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pylab as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
def preprocess(text, stem=False):
    text = re.sub(text_cleaning_re, ' ', str(text).lower()).strip()
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
columns = ["target", "ids", "date", "flag", "user", "text"]
text_cleaning_re = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
nltk.download('stopwords')
stop_words = stopwords.words("english")
stemmer = SnowballStemmer("english")
decode_map={0: "NEGATIVE", 2: "NEUTRAL", 4: "POSITIVE"}
print("讀取csv檔案.....", end="")
t1=time.time()
df = pd.read_csv('training.1600000.processed.noemoticon.csv',
                 encoding = "ISO-8859-1",
                 names=columns)
t2=time.time()
print(f'花費時間 : {t2-t1:.4f}秒')

print("預處理字串.....", end="")
t1=time.time()
df.text=df.text.apply(lambda x:preprocess(x))
#底下這行其實可以不用作，結論維持在 0 及 4 二種
df.target=df.target.apply(lambda x:decode_sentiment(x))
t2=time.time()
print(f'花費時間 : {t2-t1:.4f}秒')

#載入字典
with open("eng_dictionary.pkl",'rb') as file:
    tok=pickle.load(file)
vocab_size = len(tok.word_index)

df_train, df_test,=train_test_split(df, test_size=0.2, random_state=1)
#取得 w2v 模型中每個字的 100個 權重，首先要知道共有幾個字
weights=np.zeros([vocab_size, 100])
w2v_model=Word2Vec.load("w2v_model")
for word, i in tok.word_index.items():
    #因為 w2v 設定如果單字出現次數小於10次就認定為錯字而刪除，所以會有一些字不在 w2v中
    if word in w2v_model.wv:
        weights[i]=w2v_model.wv[word]

#x_train/x_test 送進去的句子
x_train=pad_sequences(tok.texts_to_sequences(df_train.text), maxlen=300)
x_test=pad_sequences(tok.texts_to_sequences(df_test.text), maxlen=300)

#y_train/y_test : 正向的，負面的，也就是判讀後的結果
encoder=LabelEncoder()
encoder.fit(df_train.target.tolist())
y_train=encoder.transform(df_train.target.tolist())
y_test=encoder.transform((df_test.target.tolist()))

y_train=y_train.reshape(-1, 1)#轉成 n*1的維度
y_test=y_test.reshape(-1, 1)

model=Sequential()
model.add(
    Embedding(
        vocab_size,
        100,#Word2Vec每個字都有100個權重
        weights=[weights],
        input_length=300,
        trainable=False
    )
)
model.add(Dropout(0.5))#故意去除一部份資料，怕過度擬合
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(#指定損失函數，使用那種梯度下降(BGD/SGD/MBGD)，使用那種優化器
    loss='binary_crossentropy',#損失函數必需作梯度下降逼近法，裏面有一個學習率
    optimizer='adam',#優化器就是在自動調整學習率
    metrics=['accuracy']
)

#ReduceLROnPlateau : Reduce Learinig Rate : 模型訓練時，模型逐漸接近全局最小值，適度降低學習率，助於找到最佳解
#EarlyStopping : 當訓練集上的 loss 不再減少，就提早停止訓練
callbacks=[ReduceLROnPlateau(monitor='val_loss', patience=5, cooldown=0),
           EarlyStopping(monitor='val_acc', min_delta=1e-4, patience=5)
          ]
#開始訓練
print("LSTM 訓練模型....約需三小時")
t1=time.time()
BATCH_SIZE=1024#如果發生 OOM, 請調整這裏
#verbose : 0不輸出訊息, 1 :輸出進度條, 2:為每個 epoch 輸出一行記錄
history=model.fit(
    x_train, y_train,
    batch_size=BATCH_SIZE,
    epochs=8,
    validation_split=0.1,
    verbose=1,#輸出進度條
    validation_data=(x_test, y_test),
    callbacks=callbacks
)
t2=time.time()
print(f"模型訓練花費時間:{t2-t1:.4f}秒")

if os.path.exists("sentiment_model"):
    shutil.rmtree("sentiment_model")
model.save("sentiment_model")


score=model.evaluate(x_test, y_test, batch_size=BATCH_SIZE)
print(f"Loss : {score[0]}")
print(f"Accuracy : {score[1]}")
acc=history.history['accuracy']
val_acc=history.history['val_accuracy']
loss=history.history['loss']
val_loss=history.history['val_loss']
x=range(len(acc))
plt.plot(x, acc, 'b', label='Training Acc')
plt.plot(x, val_acc, 'g', label='Validation Acc')
plt.plot(x, loss, 'r', label='Train loss')
plt.plot(x, val_loss, 'y', label='Validation loss')
plt.legend()#顯示圖例
plt.show()