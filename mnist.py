# import tensorflow as tf
# import tensorflow.keras as keras
# import pandas as pd
# import matplotlib.pyplot as plt
# from tensorflow.python.client import device_lib

# def get_available_gpus():
#     local_device_protos = device_lib.list_local_devices()
#     return [x.name for x in local_device_protos if x.device_type == 'GPU']

# print(get_available_gpus())
# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# print(x_train[0])
# plt.imshow(x_train[0])
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
