from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer

# Tokenizer統計共有幾個不重複的單字數，並將每個單字編號，編號由 1 開始
toz = Tokenizer()
text = ['I am Thomas','I am a programer', 'Python is a good language']
toz.fit_on_texts(text)

print('word_index', toz.word_index)
print('len', len(toz.word_counts))
print("轉數字 : ",toz.texts_to_sequences(text)) # 將單字轉換成數字
print("等長",pad_sequences(toz.texts_to_sequences(text), maxlen=50)) # pad_sequences : 將每個句子變成等長
