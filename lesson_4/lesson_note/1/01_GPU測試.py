#每次開新專案時，Pycharm 的 download-pre build，千萬別下載，否則會變成簡体中文
#New Project : 新項目，是大陸用語
#CUDA : 11.8最穩定。
#CUDA : 12.1版本，cusolver64_12.dll, 但 tensorflow 最新版還是去找 cusolver64_11.dll, 結果找不到
#tensorflow : 還是只能裝 2.10.1，2.11.1/2.12.1都有問題，抓不到 GPU
#pip install tensorflow==2.10.1
import tensorflow as tf
gpus=tf.config.list_physical_devices(device_type="GPU")
cpus=tf.config.list_physical_devices(device_type="CPU")
print(gpus, cpus)