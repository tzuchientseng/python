"""
NLP : Natural Language Processing : 自然語言處理
ChatGPT 需十幾億美金的設備及極多的人力才能完成
讀入文章 => 去除停用詞 => (中文要加斷詞) => 建立 Word2vec 字典 => 向量化(訓練) => 偵測相關詞
# 結巴演算法
停用詞 : the, is, at, which, in......
Word2vec 向量化模型，目前亦出現 GloVe, fast text, ELMo, BERT等模型
請到 kaggle https://www.kaggle.com/ 下載 Sentiment140 文章
kaggle 是數據建模及數據分析競賽平台
Sentiment140 : https://www.kaggle.com/datasets/kazanova/sentiment140
pip install tensorflow==2.10.1 scikit-learn nltk gensim xlrd openpyxl pandas
// xlrd 與 openpyxl 是讀取 Excel 檔案的套件
# 起手式
- 物件向量化 : 一個字一個數字
- one-hot encoding : 一個字一個向量 // 使用對角線矩陣，很浪費記憶體
- Word2Vec : 將單字量化成二維陣列，相近的字會有相近的向量，

"""
import re
import time
import nltk
import pandas as pd
from gensim.models import Word2Vec
from nltk import SnowballStemmer
from nltk.corpus import stopwords

def preprocess(text, stem=False): # 預設不去除字尾
    # strip()去除 '\n'
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower()).strip()
    tokens = []
    for token in text.split():
        # 去除停用詞
        if token not in stop_words:
            if stem:
                tokens.append(stemmer.stem(token)) # 去除字尾
            else:
                tokens.append(token)
    return " ".join(tokens) # "where are you guys"

# 完美列印
display = pd.options.display
display.max_columns = None
display.max_rows = None
display.width = None
display.max_colwidth = None

"""
使用colab 的人，需加如下設定
from google.colab import drive
drive.mount('/data')
"""

DATASET_ENCODING = 'ISO-8859-1' # 資料集編碼
DATASET_COLUMNS = ['target', 'ids', 'date', 'flag', 'user', 'text']

df = pd.read_csv( # 主要還是靠 xlrd 與 openpyxl 去讀取 Excel 檔案 pd 只負責轉換成 DataFrame 格式
    'training.1600000.processed.noemoticon.csv',
    encoding = DATASET_ENCODING, # 解決 'utf-8' code can't decode byte 0xff in position 0: invalid start byte問題
    names = DATASET_COLUMNS,
)
"""
colab
df = pd.read_csv(
    '/data/MyDrive/training.1600000.processed.noemoticon.csv',
    encoding = DATASET_ENCODING,
    names = DATASET_COLUMNS,
)
"""

# 停用詞下載位置 : C:\Users\GOOD-PC\AppData\Roaming\nltk_data\corpora\stopwords
nltk.download('stopwords') # 下載停用詞 
stop_words = stopwords.words('english') # 不要做訓練
# print(stop_words)
# 斯攤ㄟmer主幹去除 去除字尾, 比如 tion, ly, ed
stemmer = SnowballStemmer('english') # 雪球去除器，一開始不會用到 

# 預處理資料-去除停用詞，字尾等
print("開始預處理.....")
t1 = time.time()
# lambda : 精簡寫法，有人說只是個蜜糖
# 底下是把 preprocess()函數丟給 apply()函數

TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+" # 正規表達式
df.text = df.text.apply(lambda x: preprocess(x))
t2 = time.time()
print(f'預處理時間 : {t2 - t1}秒')
# 建立詞彚vocabularies，必需是二維
# [["this","is","a","book"],
#  ["where","are","guys"],
#  ....
#  ]160萬列，每列的行不一定
print("將每篇文章拆開成單字陣列....")
vocabularies = [chapter.split() for chapter in df.text]

W2V_SIZE = 100
W2V_WINDOW = 7 # 與前7及後7個字產生關連
W2V_EPOCH = 32
W2V_MIN_COUNT = 10 # 總出現次數小於10次就去除掉(去除錯字)

w2v_model = Word2Vec(
    window = W2V_WINDOW,
    min_count = W2V_MIN_COUNT,
    workers = 8 # 啟用 8 個執行緒去執行
)

# 建立一部字典
w2v_model.build_vocab(vocabularies) # 如此Word2Vec才看得懂的格式
# 取得所有的單字
words = list(w2v_model.wv.key_to_index.keys())
# 舊版的 Word2Vec 是使用 w2v_model.wv.vocab.keys()
vocab_size = len(words)
print(f"Vocab size : {vocab_size}")
print("開始向量化.....")
t1 = time.time()
w2v_model.train(vocabularies, total_examples=len(vocabularies), epochs=W2V_EPOCH)
t2 = time.time()
w2v_model.save("w2v_model")
# 使用 colab 的人
# w2v_model.save("/data/MyDrive/w2v_model")
print(f"向量化時間 : {t2 - t1}秒")
