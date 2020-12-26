import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.layers import SpatialDropout1D, Embedding, Bidirectional
from tensorflow.keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
import pickle
from gensim.parsing.preprocessing import preprocess_string

# Tweet for model building as already been preprocess. hence no need for text cleanup
tweets_df = pd.read_csv("data/dataset.csv", encoding="UTF-8")
tweets_df = tweets_df.dropna()
tweets_df = tweets_df.rename(columns={"selected_text":"text", "sentiment":"label"})
#tweets_df["text"] = [" ".join(preprocess_string(twt)) for twt in tweets_df["text"]]

# Data processing
## Tokenize tweets and label
tweet = tweets_df.text.values
tokenizer = Tokenizer(num_words=25000)
tokenizer.fit_on_texts(tweet)

# Save tokenizer
with open("./model/tokenizer.pickle", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

vocab_size = len(tokenizer.word_index) + 1
encoded_docs = tokenizer.texts_to_sequences(tweet)
tweets = pad_sequences(encoded_docs, maxlen=200)

## Labels
labels = to_categorical(tweets_df["label"].values, 3, dtype="float32")

#Split dataset
X_train, X_test, y_train, y_test = train_test_split(tweets,labels, test_size=0.25, random_state=0)
print (len(X_train),len(X_test),len(y_train),len(y_test))

model = Sequential()
model.add(Embedding(vocab_size, 32, input_length=200))
model.add(Bidirectional(LSTM(50,dropout=0.2)))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer='rmsprop',loss='categorical_crossentropy', metrics=['accuracy'])

# model.add(Embedding(vocab_size, 32, input_length=200))
# model.add(SpatialDropout1D(0.25))
# model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
# model.add(Dropout(0.2))
# model.add(Dense(3, activation="softmax"))
# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

#Implementing model checkpoints to save the best metric and do not lose it on training.
checkpoint = ModelCheckpoint("./model/model.hdf5", 
                             monitor='val_accuracy', 
                             verbose=1,
                             save_best_only=True, 
                             mode='auto',
                             save_weights_only=False,
                             period=1)

history = model.fit(X_train, y_train, 
                    epochs=70,
                    validation_data=(X_test, y_test),
                    callbacks=[checkpoint])
                    
print(model.summary())
