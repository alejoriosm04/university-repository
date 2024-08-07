# Execute this script to train the model with Tensorflow

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def training():
    # Training Data to convert Celcius to Fahrenheit
    celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype = float)
    fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype = float)

    layer = tf.keras.layers.Dense(units = 1, input_shape = [1])
    model = tf.keras.Sequential([layer])

    model.compile(
        optimizer = tf.keras.optimizers.Adam(0.1),
        loss = 'mean_squared_error'
    )

    print("Start Training")
    historial = model.fit(celsius, fahrenheit, epochs = 1000, verbose = False)
    print("Training Completed")

    plt.xlabel("# of workouts")
    plt.ylabel("Magnitude of loss")
    plt.plot(historial.history["loss"])
    plt.show()

    print("=" * 20)
    print("Saving the model...")
    model.save('saved_model/my_model')
    print("Model saved")

    print("=" * 20)
    print("Internal variables of the model:")
    print(layer.get_weights())

    return model


def main():
    training()


if __name__ == '__main__':
    main()