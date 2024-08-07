import tensorflow as tf
from model import *


def neural_network(data_services):
    try:
        model = tf.keras.models.load_model('saved_model/my_model')
    except:
        model = training()

    results = []
    for data in data_services:
        result = model.predict([data])
        results.append(result)

    return results
