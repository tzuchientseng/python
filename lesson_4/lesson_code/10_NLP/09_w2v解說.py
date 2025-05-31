from gensim.models import Word2Vec

w2v_model = Word2Vec.load("w2v_model")
print(w2v_model.wv['taiwan']) # 列出 taiwan 的權重
