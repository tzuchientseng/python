# 中文資料下載  https://www.kaggle.com/c/fake-news-pair-classification-challenge
# 下載 train, test, sample_submission
# 下載停用詞 : https://github.com/GoatWang/ithome_ironman/tree/master/day16_NLP_Chinese
# 下載字典 : https://github.com/APCLab/jieba-tw , 斷詞用的，使用結巴演算法
# pip install jieba wordcloud matplotlib
# wordcloud : 文字雲
import jieba # 結巴演算法
jieba.set_dictionary('dict.txt')
with open('stops.txt','r', encoding='utf8') as f:
    stops = f.read().split('\n')
print(stops)
j1 = [t for t in jieba.cut('下雨天留客天留我不留')]
print(j1)
j2 = [t for t in jieba.cut('下雨天留客天留我不留', cut_all=True)]
print(j2)
s = '為什麼要多了斷詞這個步驟? 原因是英文的一個單字代表一個意思，比如 “traditional” 這一個單字的意思就是中文的 “傳統的”。英文只要一個單字 “traditional”，中文卻要用三個字來表示 “傳統的”。'
j3 = [t for t in jieba.cut(s, cut_all=True)]
print(j3)
