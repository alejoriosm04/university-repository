import tensorflow as tf
import model

def main():
    # layer, model = training()
    try:
        model = tf.keras.models.load_model('saved_model/my_model')
    except:
        model = model.training()
    
    training_data = float(input("Learning attempt: "))
    result = model.predict([training_data])
    print("=" * 20)
    print("The answer is: " + str(result) + " fahrenheit")


if __name__ == '__main__':
    main()