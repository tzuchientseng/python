# 爬蟲自 Chrome 115 後就不能用
# 開啟專案 pip install --upgrade webdriver-manager selenium
# pip 更新版本 : python -m pip install --upgrade pip
# pip install nltk scikit-learn gensim

import codecs
import re
import time
import jieba
from gensim.models import Word2Vec

def preprocess(text):
    # 透過正規表達式清理文本
    text = re.sub(TEXT_CLEANING_RE,' ', str(text).lower()).strip()
    text = text.replace(" ","")
    return text

TEXT_CLEANING_RE = "[0-9a-zA-Z,:.?!\"\+\-*/_='()\[\]|<>$（）［］，｜、《》！？”%【】“　．…❤：]"
file = codecs.open('train_tc.csv','r','utf-8')
jieba.set_dictionary('dict.txt')

with open('stops.txt','r',encoding='utf-8') as f:
    stops = set(f.read().split("\n"))

vocabularies = []
print("處理斷詞中...")

for line in file.readlines():
    line = preprocess(line)
    terms = [t for t in jieba.cut(line, cut_all=True)if t not in stops]
    vocabularies.append(terms)

w2v_model = Word2Vec(
    window = 7, # 與前 7 後 7 個字產生關連
    min_count = 10,
    workers = 8
)

print("建立字典.....")
w2v_model.build_vocab(vocabularies)
print("開始向量化中.....")
t1 = time.time()
w2v_model.train(vocabularies, total_examples=len(vocabularies), epochs=32)
t2 = time.time()
w2v_model.save('w2v_model_chinese')
print(f'向量化共花費 : {t2 - t1}秒')
