#本站主要網址 : http://mahaljsp.asuscomm.com =>mahal(瑪哈)-jsp(Java Server Page)
#本站備份網址 : http://mahaljsp.ddns.net : 7/5日掛掉(停電，Windows+vmware+linux)
#pip install tensorflow==2.10.1
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
#a=np.zeros([10]) # [0, 0,....]
a=[1,2,3]
b=[4,5,6]
print(a+b) # [1,2,3,4,5,6]
c=np.array([1,2,3])
d=np.array([4,5,6])
print(c+d) # [5,7,9]
e=np.zeros([10])
print(e)
f=np.ones(shape=[10], dtype=np.int32)*50
print(f)
#在 tf1.0版把下面的陣列稱為 tf.placeholder
h=tf.zeros(shape=[10])
print(h)
i=tf.ones([10])*5
print(i)
j=tf.fill([2,3], 5.)
print(j)
k=tf.ones([2,3])*5
print(k)
l=tf.range(2, 10, 2)
print(l)
#m=np.arange(1,100000)#需400k
m=np.arange(1,10,0.1)#需400k, 支援浮點數
print(m)
n=range(1,10)#隋性求值, 要取得下一個值,都會調用 next, 只佔用幾 byte而以
o=list(range(1,10))#不支援浮點數
print(o)
p=tf.range(2, 10, 2.5)#支援浮點數
print(p)
q=tf.random.normal([10])
print(q)
r=tf.random.uniform([10])
print(r)