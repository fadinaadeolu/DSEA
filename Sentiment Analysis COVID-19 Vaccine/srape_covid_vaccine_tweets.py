import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime
#start = input("Enter start date (YYYY-MM-DD): ")

def scrape_twitter(start, stop):

    tweets_list = []
    for tweet in sntwitter.TwitterSearchScraper("""(covid-19 vaccine)
        OR #vaccine
        OR #Coronavirusvaccine
        OR #COVID19Vaccine since:{} until:{}""".format(start, stop)).get_items():
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

d = pd.date_range("2020-11-1", "2020-12-30", freq="D")
dt = [i.strftime("%Y-%m-%d") for i in d]

for i in range(0, len(dt)+1):
    try:
        start = dt[i]
        stop = dt[i+1]
    except IndexError:
        start = dt[-1]
        stop = datetime.datetime.now().strftime("%Y-%m-%d")

    tweets_df = scrape_twitter(start, stop)
    tweets_df.to_csv("./data/tweets_covid_2020-11-1.csv".format(start), mode="a", header=False, index=False)

    print(stop)

# Reference
# https://medium.com/better-programming/how-to-scrape-tweets-with-snscrape-90124ed006af
