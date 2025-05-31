import torch as tc
a = tc.tensor([1.,2.,3.]) # float32
print(a.dtype)
print(a.char()) # int8 有正負值 -128~127
print(a.byte()) # uint8, 0-255
print(a.short()) # int16 -32768~32767
print(a.int()) # int32 -21億~21億 (-2^31~2^31-1)
print(a.long()) # int64
print(a.float()) # float32
print(a.double()) # float64
print(pow(2,5)) # 32
print(pow(2,8)) # 256
print(pow(2,10)) # 1024
print(pow(2,16)) # 65535
print(pow(2,24)) # 1677萬
print(pow(2,32)) # 4096M/4G/42億
