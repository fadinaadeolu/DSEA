import pandas as pd
import numpy as np
import re, pickle
from gensim.parsing.preprocessing import preprocess_string
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.preprocessing import strip_tags
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from gensim.parsing.preprocessing import strip_numeric
from gensim.parsing.preprocessing import strip_short
from gensim.parsing.preprocessing import stem_text
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

# Import COVID-19 and vaccine tweets
tweets_covid_df = pd.read_csv("data/tweets_covid_19.csv", encoding="UTF-8")
tweets_covid_df = tweets_covid_df.iloc[:,:]
tweets_covid = tweets_covid_df[["tweet"]]

# Clean up tweets
CUSTOM_FILTERS = [lambda x: re.compile(r"https?://\S+|www\.\S+").sub(r"", x),
                  remove_stopwords,
                  strip_tags,
                  strip_multiple_whitespaces,
                  strip_numeric]

tweets_covid_df["clean_tweet"] = [" ".join(preprocess_string(twt, CUSTOM_FILTERS))
                              for twt in tweets_covid["tweet"]]

# Load the best model obtained during training
model = load_model("./model/model.hdf5")

# loading tokenizer
with open("./model/tokenizer.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)
    
sentiment = ['Neutral','Negative','Positive']

counter = 0
sentiments = []

for twt in tweets_covid_df["clean_tweet"]:
    try:
        sequence = tokenizer.texts_to_sequences(twt)
        test = pad_sequences(sequence, maxlen=200)
        s = sentiment[np.around(model.predict(test), decimals=0).argmax(axis=1)[0]]
        sentiments.append(s)
        print(s)
    except:
        sentiments.append(np.nan)
        
    counter = counter + 1
    print(counter)
    
tweets_covid_df["sentiment"] = sentiments
tweets_covid_df.to_csv("./data/covid_tweets_with_sentiment.csv", header=True, index=False)
