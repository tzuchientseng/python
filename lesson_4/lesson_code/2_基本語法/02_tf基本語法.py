import os
import tensorflow as tf
#environment 環境設定，設定輸出等級
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
pi=tf.constant(3.1415926)
r=tf.Variable(10, dtype=tf.float32)
#底下的計算，會交由GPU執行，若沒有GPU則自動切換到 CPU執行
print(pi*r*r)
#tf的輸出機制
'''
0 : Info (通知)
1 : Warning (警告)
2 : Error (錯誤)
3 : Fatal (穩死的)
早期的版本，os.environ['TF_CPP_MIN_LOG_LEVEL']='2'必需寫在 import tensorflow as tf 之前
現在不需要了

tf基本格式 : tf.Tensor(張量, 常數), tf.Variable(變數)二種，都是類別
class Tensor():
    pass
class Variable():
    pass

class Pokemon():神奇寶貝，是一個統稱，就抽像類別
    pass
a=Pokemon()
class Pikachu(Pokemon):皮卡丘
    pass
b=Pikachu()
皮卡丘是神奇寶貝，但神奇寶貝不是皮卡丘

a=Tensor()產生物件，但Tensor()是抽像類別，不可以直接使用, 
要用 a=tf.constant()這個方法來產生Tensor物件, constant是一個方法，所以是小寫
'''
a=tf.constant(128, dtype=tf.int32)#此時會溢位而不正確
print(a)
'''
01111111 : 127
10000000 : 溢位(128)
第一位為 0 是正數，1為負數
dtype : 資料型態 (電子計算機概論)
整數 : tf.int8(-128~127), tf.int16(-32768~32767), tf.int32(-21億~21億), tf.int64(-2^63~2^63-1)
整數預設是 tf.int32
無號整數 : tf.uint8(0~255), tf.uint16(0~65535), tf.uint32(0~42億), tf.uint64(0~2^64-1) (unsigned)
浮點數 : tf.float16, tf.float32(單精度浮點數，準確到小數第7位), tf.float64(雙精度浮點數, 準確到小數第15位)
浮點數預設是 tf.float32
等功力到了再看下文
http://mahaljsp.asuscomm.com/index.php/2019/09/11/binary_float/

tf.constant(128, dtype=tf.float32)會將整數轉成小數
tf.constant(128., dtype=tf.int32)無法將小數轉成整數, 會發生例外
'''