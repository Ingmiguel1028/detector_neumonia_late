import tensorflow as tf
from tensorflow.keras import models
#Cargando el modelo de deteccion de neumonia
def model():
    model_cnn = tf.keras.models.load_model('WilhemNet_86.h5')
    return model_cnn