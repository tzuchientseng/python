# .\venv\Scripts\python D:\Coding\python\lesson_4\蒙地卡羅_CPU.py
# x=\frac{\pi}{4}   {\pi}=4x*4/7
#面積 = pi/4, pi=面積*4
#目前的任務 : 想辦法求出面積

import time
import numpy as np
batch = 100_000_000
epoch = 200
incircle = 0
for e in range(epoch):
    t1 = time.time()
    points = [np.random.uniform(0,1,batch), np.random.uniform(0,1,batch)] # uniform 表均勻分布, normal 為標準常態
    dist = np.sqrt(np.square(points[0]) + np.square(points[1])) # 與原點距離
    # 以下寫法會太慢
    # count=0
    # for d in dist:
    #     if d <= 1:count += 1
    #print(count/batch*4)
    incircle += np.where(dist<=1)[0].shape[0]
    t2 = time.time()
    print(f'epoch:{e+1} ,花費時間:{t2-t1:.4f}秒, pi={incircle/((e+1)*batch)*4}')
