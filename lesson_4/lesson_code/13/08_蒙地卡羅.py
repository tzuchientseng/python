import torch as tc
import time
def dist():
    #產生1000個點，然後計算多少個點是在圓內
    #底下是舊版的寫法, 在 cpu產生變數，再 copy 到 GPU
    #points=tc.rand([2,batch]).to("cuda")
    #points = tc.rand([2, batch]).cuda()# 跟上面一樣

    #底下是新版的寫法，直接在GPU產生變數
    #points = tc.rand([2, batch], device="cuda")

    #底下的寫法，只有填入亂數值，沒有產生空間的操作
    points = array.uniform_(0, 1)
    d = tc.sqrt(tc.square(points[0]) + tc.square(points[1]))#GPU 運算
    idx=tc.where(d<=1)#那幾個點是在圓內
    #print(idx)
    #print(idx[0].shape[0])
    return idx[0].shape[0]
batch=100_000_000
epoch=100
incircle=0

device=tc.device("cuda" if tc.cuda.is_available() else "cpu")
array=tc.zeros([2, batch], dtype=tc.float32, device=device)

for e in range(epoch):
    t1=time.time()
    incircle += dist()
    t2=time.time()

    area = incircle / ((e+1)*batch)
    pi = area * 4
    print(f'epoch:{e+1:07,d}, time:{t2-t1:.7f}秒, pi={pi}')
