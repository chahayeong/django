import datetime
from twitterscraper import query_tweets

list_of_tweets = query_tweets('코로나', begindate=datetime.date(2021,5,1), enddate=datetime.date(2021,5,28), limit=10)

for tweet in list_of_tweets:
    print("screen_name: "+tweet.screen_name)
    print("username: " +tweet.username)
    print("timestamp: "+str(tweet.timestamp))
    print("text: "+tweet.text)