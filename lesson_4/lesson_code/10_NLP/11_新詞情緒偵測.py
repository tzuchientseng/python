import os
import pickle
import keras
from keras.utils import pad_sequences

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def getLabel(score):
    label = "中立的"
    if score <= 0.4:
        label = "負面的"
    elif score >= 0.7:
        label = "正向的"
    return label

#載入字典
with open("eng_dictionary.pkl",'rb') as file:
    toz = pickle.load(file)

model = keras.models.load_model("sentiment_model_sunny")
# text = "I will kill somebody in Taipei train station"
text = """
Philippians 4:13 (NIV)
"I can do all this through him who gives me strength."

Psalm 23:1-3 (NIV)
"The Lord is my shepherd, I lack nothing. He makes me lie down in green pastures, he leads me beside quiet waters, he refreshes my soul."

Isaiah 41:10 (NIV)
"So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand."

Proverbs 3:5-6 (NIV)
"Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight."

Matthew 11:28-30 (NIV)
"Come to me, all you who are weary and burdened, and I will give you rest. Take my yoke upon you and learn from me, for I am gentle and humble in heart, and you will find rest for your souls. For my yoke is easy and my burden is light."

Romans 8:28 (NIV)
"And we know that in all things God works for the good of those who love him, who have been called according to his purpose."

John 3:16 (NIV)
"For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."

Psalm 46:1 (NIV)
"God is our refuge and strength, an ever-present help in trouble."

Verses of Encouragement:
Jeremiah 29:11
"For I know the plans I have for you,” declares the Lord, “plans to prosper you and not to harm you, plans to give you hope and a future."

Philippians 4:13
"I can do all things through Christ who strengthens me."

Isaiah 41:10
"So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand."

Verses about Joy and Hope:
Psalm 37:4
"Take delight in the Lord, and He will give you the desires of your heart."

Romans 15:13
"May the God of hope fill you with all joy and peace as you trust in Him, so that you may overflow with hope by the power of the Holy Spirit."

Nehemiah 8:10
"Do not grieve, for the joy of the Lord is your strength."

Verses about Love and Peace:
1 Corinthians 13:13
"And now these three remain: faith, hope, and love. But the greatest of these is love."

John 14:27
"Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid."

1 John 4:19
"We love because He first loved us."

Verses about Strength:
Isaiah 40:31
"But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint."

Psalm 46:1-2
"God is our refuge and strength, an ever-present help in trouble. Therefore we will not fear, though the earth give way and the mountains fall into the heart of the sea."

Verses about God's Faithfulness:
Lamentations 3:22-23
"Because of the Lord’s great love we are not consumed, for His compassions never fail. They are new every morning; great is Your faithfulness."

Proverbs 3:5-6
"Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to Him, and He will make your paths straight."
"""
x_test = pad_sequences(toz.texts_to_sequences([text]), maxlen=300)
score = model.predict([x_test])[0]
label = getLabel(score)
print(score, label)
