#tensorflow 為一台強大的計算機，將指令送入 cudnn, 再送cuda ，再交由 GPU 計算
#是神經網路的框架，另一個常用的是 Pytorch
#pip install tensorflow==2.10.1
#使用 2.11.0/2.12.0 有 bug
#pip install tensorflow-gpu 測試，2.12.0跟 cuda 11.8/12.0還沒搭好
import tensorflow as tf
gpus=tf.config.list_physical_devices(device_type="GPU")
cpus=tf.config.list_physical_devices(device_type="CPU")
print(gpus, cpus)
print(tf.version.VERSION)
# colab 使用 tf 2.12.0 卻可以顯示 GPU,
# 表示 colab 可能不是用 cuda，但也有可能是因為 linux 的關係