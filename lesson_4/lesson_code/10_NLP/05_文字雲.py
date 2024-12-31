# pip install jieba wordcloud matplotlib opencv-python 
# 不用 Pillow 用 opencv
# 英業達 仁寶
# 2013年開始改組，想加入其它產業，智慧城市
# 耗時約 2年
# 1. 建模，開發演算法，修正
# 人力 : 10~30人
# 20人 : 200萬台幣(7000美金)/年 *20 = 4000萬台幣
# 機器設備 : 1000萬台幣
# total 5000萬以上 *2 = 1 億

from collections import Counter
import pylab as plt
import jieba
import numpy as np
from PIL import Image
import cv2
from wordcloud import WordCloud

with open('stops.txt','r', encoding='utf-8') as f:
    stops = set(f.read().split("\n")) # 針對 \n 切割
    # set的效能比 list 高很多，且能去除重複值

with open("wc.txt", 'r', encoding='utf-8')as f:
    txt = " ".join(f.read().split("\n"))
    txt = txt.replace(" ", "").replace("/","").replace('"','')

jieba.set_dictionary('dict.txt')
terms = [t for t in jieba.cut(txt, cut_all=True) if t not in stops]

# 透過遮罩去描繪形狀
mask = cv2.imdecode(np.fromfile('heart.png', dtype=np.uint8), cv2.IMREAD_UNCHANGED)
wordcloud = WordCloud(font_path='mingliu.ttc', background_color='white', mask=mask)

print(Counter(terms)) # 每一個斷詞出現的次數
img = wordcloud.generate_from_frequencies(frequencies=Counter(terms))
plt.imshow(img)
plt.show()
