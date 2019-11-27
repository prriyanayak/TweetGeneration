import tweepy
import csv
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

today = datetime.date.today()
actualDate = today - relativedelta(months=3)

####input your credentials here
consumer_key = "***"
consumer_secret = "***"
access_token_key = "***"
access_token_secret = "***"   

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


def getTrending(topic):
    csvFile = open(topic+'.csv', 'w')
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search,q=topic,count=100, lang="en", since=actualDate).items():
        # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        csvWriter.writerow([tweet.created_at, tweet.text.encode('ascii', 'ignore')])
    return topic
