import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
a = tf.ones([2,3], dtype=tf.int32)
# a 是 tf.Tensor格式, 裏面的值不可以更改
# a[1,2] = 50

x = 10
x = x + 20 # 指定運算子, 右邊的值放到左邊，也是程式的原點
x += 20
# pikachu.level = pikachu.level+10
# pikachu.level += 10

# tf陣列改值方式如下
# 先把b的空間撐開
b = tf.Variable(tf.ones([2,3],dtype=tf.int32))
# 再用 assign指定其值
b[1,2].assign(50) # 不能這樣寫 b[1][2]
print(b)