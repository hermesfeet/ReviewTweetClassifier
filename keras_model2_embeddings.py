from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras import layers
from baseline_model import *

#Maximum sequence length aftger padding is 100 - use 50 dimensions for embedding
maxlen = 100
embedding_dim = 50

#Tokenizer: the resulting vectors equal the length of each text, and the numbers don’t denote counts,
# but rather correspond to the word values from the dictionary tokenizer.word_index.
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(sentences_train)

X_train = tokenizer.texts_to_sequences(sentences_train)
X_test = tokenizer.texts_to_sequences(sentences_test)

vocab_size = len(tokenizer.word_index) + 1 #Add 1 because 0 is reserved for index

print(sentences_train[4])
print(X_train[4])

X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

#Sequential model with 3 hidden payers, one output
#Use the Embedding Layer of Keras which takes the previously calculated integers and maps them
# to a dense vector of the embedding. You will need the following parameters:
#input_dim: the size of the vocabulary
#output_dim: the size of the dense vector
#input_length: the length of the sequence
#We take the output of the embedding layer and plug it into a Dense layer.  So we need to add a Flatten layer
#  in between that prepares the sequential input for the Dense layer
#Also add a pool layer with global max/average pooling - takes the max value of all the features in the pool for each
#feature dimension - this is a way of reducing the size of incoming feature vectors (downsampling).

model = Sequential()
model.add(layers.Embedding(input_dim=vocab_size,
                           output_dim=embedding_dim,
                           input_length=maxlen))
model.add(layers.GlobalMaxPool1D())
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.summary()


#Fit the model over 20 epochs and run it again
history = model.fit(X_train, y_train,
                    epochs=20,
                    verbose=False,
                    validation_data=(X_test, y_test),
                    batch_size=10)
loss, accuracy = model.evaluate(X_train, y_train, verbose=False)
print("Training Accuracy: {:.4f}".format(accuracy))
loss, accuracy = model.evaluate(X_test, y_test, verbose=False)
print("Testing Accuracy:  {:.4f}".format(accuracy))
