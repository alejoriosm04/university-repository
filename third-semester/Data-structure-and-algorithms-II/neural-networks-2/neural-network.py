from keras.models import Sequential
from keras.layers import Dense

# Define the model
model = Sequential()
# 12 number of nodes
# 3 estimulos, 3 variables
# activation function
model.add(Dense(12, input_dim=3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])

# Define the training data
# Pollution grade, model and number of wheels
X = [[20, 2010, 4],
        [80, 2016, 10],
        [35, 2020, 4],
        [40, 2008, 6],
        [80, 1985, 2]]
Y = [1, 0, 1, 1, 0] # 1 = good, 0 = bad

# Train the model
model.fit(X, Y, epochs=150, batch_size=10, verbose=True)

# Evaluate the model
scores = model.evaluate(X, Y)

# Print the accuracy
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# Predict the pollution grade of a car with 20 pollution grade, 2010 model and 4 wheels
print(model.predict([[90, 2010, 4]]))
