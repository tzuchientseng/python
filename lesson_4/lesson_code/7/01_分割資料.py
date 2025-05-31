#pip install tensorflow==2.10.1 matplotlib opencv-python
#Ctrl+C : 中斷安裝
#下載圖片資料 http://mahaljsp.asuscomm.com/files/vgg19/flowers_17.zip
#下載在專案後，解壓縮至此
import os
import random
import shutil

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
flowers=[]
#dirs=np.empty(0, dtype=object)
dirs=[]
with open('label.txt','r')as file:
    for line in file:
        line=line.strip()#去除 \n
        #print(line)
        cols=line.split()
        s=int(cols[0])
        e=int(cols[1])
        flower=cols[2]
        flowers.append(flower)
        #dirs=np.r_[dirs, [flower]*(e-s+1)]
        #dirs += flowers * (e - s + 1)  # 此寫法會比上面陣列的效能高很多
        dirs += [flower] * (e-s+1)#此寫法會比上面陣列的效能高很多
dirs=np.array(dirs)
for i, d in enumerate(dirs):
    print(i+1, d)
# 10天的專案，8天是撰寫程式，2天是改變數名稱，方便日後的維護
in_path="flowers_17"
train_path='train_images'
test_path='test_images'
if os.path.exists(train_path):
    shutil.rmtree(train_path)
os.mkdir(train_path)
if os.path.exists(test_path):
    shutil.rmtree(test_path)
os.mkdir(test_path)
for flower in flowers:
    os.mkdir(os.path.join(train_path, flower))
    os.mkdir(os.path.join(test_path, flower))
datas=list(zip(os.listdir(in_path), dirs))
random.seed(1)
random.shuffle(datas)
train=int(len(datas)*0.9)
for file, flower in datas[:train]:
    source=os.path.join(in_path, file)
    dest=os.path.join(train_path, flower, file)
    print(f'copy {source} => {dest}')
    shutil.copy(source, dest)
for file, flower in datas[train:]:
    source=os.path.join(in_path, file)
    dest=os.path.join(test_path, flower, file)
    print(f'copy {source} => {dest}')
    shutil.copy(source, dest)