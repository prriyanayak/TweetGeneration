from twitter import *
import csv
import random
from getTweetsInTrending import getTrending
from cleanData import cleanTheTweets

consumer_key = "***"
consumer_secret = "***"
access_token_key = "***"
access_token_secret = "***"   

# csv_columns = ['ID', 'Name']
# api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)

api = Twitter(auth = OAuth(accessTokenKey, 
                accessTokenSecret, consumerKey, consumerSecret))


woeid_india = 2282863
results = api.trends.place(_id = woeid_india)

print("India Trends")
trends = []
for location in results:
    for trend in location["trends"]:
        trends.append(trend["name"])

print(trends)
print("Selected Trend: ")
trend = random.choice(trends)
print(trend)
# print(getTrending(trend))
csvFileName = getTrending(trend)
finalSet = cleanTheTweets(csvFileName)
print(len(finalSet))

