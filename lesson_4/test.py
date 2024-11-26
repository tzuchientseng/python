# .\venv\Scripts\activate
# python test.py
# .\venv\Scripts\python test.py

import tensorflow as tf

gpus = tf.config.list_physical_devices(device_type="GPU")
cpus = tf.config.list_physical_devices(device_type="CPU")

print("GPUs:", gpus)
print("CPUs:", cpus)
print("GPU Available:", tf.test.is_gpu_available())

# import tensorflow as tf

# # 顯示可用的 GPU
# gpus = tf.config.list_physical_devices('GPU')
# print("Available GPUs:", gpus)

# if gpus:
#     with tf.device('/GPU:0'):
#         a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
#         b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
#         c = tf.matmul(a, b)
#         print("GPU computation result:\n", c)
# else:
#     print("No GPUs found.")
