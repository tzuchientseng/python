from gensim.models import Word2Vec

# 載入模型
model = Word2Vec.load("w2v_model")
rs = model.wv.most_similar("Love".lower())
for r in rs:
    print(r)
'''
# colab使用如下
from google.colab import drive
from gensim.models import Word2Vec
drive.mount('/data')
model = Word2Vec.load("/data/MyDrive/w2v_model")
rs = model.wv.most_similar("Computer".lower())
for r in rs:
    print(r)
'''
