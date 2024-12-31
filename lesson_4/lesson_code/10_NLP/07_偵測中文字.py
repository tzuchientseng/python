from gensim.models import Word2Vec

model = Word2Vec.load("w2v_model_chinese")

while True:
    voc = input("請輸入要查詢的字詞 : ")
    if voc == 'quit': break
    try:
        rs = model.wv.most_similar(voc)
        for r in rs:
            print(r)
    except:
        print("不在字詞中")
