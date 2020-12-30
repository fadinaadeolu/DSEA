import snscrape.modules.twitter as sntwitter
import pandas as pd

start = input("Enter start date (YYYY-MM-DD): ")
def scrape_twitter(start):
    
    tweets_list = []
    for tweet in sntwitter.TwitterSearchScraper("(covid-19 vaccine) OR #vaccine since:{}".format(start)).get_items():
        tweets_list.append([tweet.id,
                            tweet.date,
                            tweet.content,
                            tweet.user.username,
                            tweet.user.id, 
                            tweet.user.location,
                            tweet.retweetCount,
                            tweet.likeCount,
                            tweet.replyCount])

    tweets_df = pd.DataFrame(tweets_list, 
                             columns=[
                                    "id", 
                                    "dt", 
                                    "tweet", 
                                    "username",
                                    "userId",
                                    "location",
                                    "retweetCount",
                                    "likeCount",
                                    "replyCount"
                            ])
    return tweets_df

tweets_df = scrape_twitter(start)
tweets_df.to_csv("./data/tweets_covid_19_{}.csv".format(start), index=False)

print(tweets_df.head(1))

# Reference
# https://medium.com/better-programming/how-to-scrape-tweets-with-snscrape-90124ed006af