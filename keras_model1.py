'''First Keras model using a linear stack of layers (sequential).'''

from keras.models import Sequential
from keras import layers
from baseline_model import *

input_dim = X_train.shape[1] #number of reatures

#Spin up a sequential model with two layers, one hidden, one output/sigmoid, train for 40 epochs
model = Sequential()
model.add(layers.Dense(10, input_dim=input_dim, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.summary()

history = model.fit(X_train, y_train,
                    epochs=40,
                    verbose=False,
                    validation_data=(X_test, y_test),
                    batch_size=10)

loss, accuracy = model.evaluate(X_train, y_train, verbose=False)
print('Training Accuracy:  {:.4f}'.format(accuracy))
loss, accuracy = model.evaluate(X_test, y_test, verbose=False)
print('Testing Accuracy:  {:.4f}'.format(accuracy))

