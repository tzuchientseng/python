import os
import cv2
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
flowers = []
dirs = []

with open('label.txt','r')as file:
    for line in file:
        line = line.strip() # 去除 \n
        cols = line.split()
        s = int(cols[0])
        e = int(cols[1])
        flower = cols[2]
        flowers.append(flower)
        dirs += [flower] * (e - s + 1) # 此寫法會比上面陣列的效能高很多
dirs = np.array(dirs)

train_imgs = []
train_labels = []
test_imgs = []
test_labels = []
train_path = "train_images"
test_path = "test_images"

for flower in flowers:
    for file in os.listdir(os.path.join(train_path, flower)):
        full = os.path.join(train_path, flower, file)
        img = cv2.imdecode(np.fromfile(full, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        img = cv2.resize(img, (224,224), interpolation=cv2.INTER_LINEAR)
        train_imgs.append(img)
        train_labels.append(flower)
train_imgs=np.array(train_imgs)

#測試資料

#建模

#訓練
