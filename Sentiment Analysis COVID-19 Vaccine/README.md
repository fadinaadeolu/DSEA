# COVID-19 Vaccine Sentiment Analysis

**Goal** 
The aim of this project is to determine people's sentiment toward covid-19 vaccines using tweets.

**Procedure**

- *Step 1:* Scrape tweets that contains (covid-19 vaccine) OR #vaccine for particular period (scrape_covid_vaccine_tweets.py). Over 1.2 million tweets were scraped
- *Step 2:* Perform sentiment analysis on tweets. Tweets Sentiment Extraction dataset [https://www.kaggle.com/c/tweet-sentiment-extraction/data] was used for building the sentiment predition model using Bidirectional Recurrent Neural Networks.

## TODO:
1. Increase data size i.e number of tweets scraped by increasing keywords.
2. Use larger training dataset [https://www.kaggle.com/kazanova/sentiment140].
