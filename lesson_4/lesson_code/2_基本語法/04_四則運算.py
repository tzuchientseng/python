import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
a=tf.constant(10.)
b=tf.Variable(3.)
#不用人家教，就可以自已學會的特質，請仔細觀查底下的結果
#print(a%b)
print(10.% 3.2)
#1. 常數跟變數可以作四則運算
#2. 運算後，全部變成 tf.Tensor格式
#3. 型態不一樣，不能作運算
#4. 整數作 +-* 運算，結果為整數
#5. 整數作 / : 結果為小數 : 跟 python一樣，但傳統語言是整數
#6. // 結果為整數 : 求商數
#7. % :求餘數
#8. 浮點數不可以求餘數，否則會出現例外錯誤。但 python 可以

#tf 與 python數字運算
#+-*/% 如果tf 是整數，會把 python 整數轉成 tf 整數，再進行運算，/後的結果，同樣變成小數
a=tf.constant(10)
print(a/2)

#如果tf 是浮點數，會把 python 整數轉成 tf浮點數，所以有點小聰明
a=tf.constant(10.)
print(a*2)

#tf 是整數，python是浮點數，因浮點數無法轉成整數，所以無法運算
a=tf.constant(10)
#print(a*2.5)#此段會發生錯誤
print(10 * 2.)#python 會將所有數轉成最大位數再運算，10為 int64, 2.0為float64
print(type(10), type(10.0))

#java
# 10/3=3