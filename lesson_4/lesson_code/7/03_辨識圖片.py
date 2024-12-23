import os
import keras.models
import numpy as np
import pylab as plt
import cv2
from keras.applications.vgg19 import preprocess_input

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 載入模型
model = keras.models.load_model("./flower_17_model")

# 取得17種花卉的名稱
flowers = []

with open('label.txt')as file:
    for line in file:
        cols = line.split()
        flowers.append(cols[2])
img_path = './images'
plt.Figure(figsize=(12,6))

# 一次辨識10張。因為載入模型會比較久，但辨識時，蠻快的
for i, file in enumerate(os.listdir(img_path)):
    img = cv2.imdecode(
        np.fromfile(os.path.join(img_path, file), dtype=np.uint8),
        cv2.IMREAD_UNCHANGED)
    x = cv2.resize(img, (224, 224), interpolation=cv2.INTER_LINEAR)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
    x = np.expand_dims(x, axis=0) # 變成四維
    x = preprocess_input(x)
    out = model.predict(x)
    idx = out[0].argmax()
    score = out[0][idx]
    name = flowers[idx]
    txt = f'{name}\n{score*100:.2f}%'
    plt.subplot(2,5, i+1)
    plt.title(txt)
    plt.axis("off")
    plt.imshow(img[:,:,::-1].copy())
plt.show()
