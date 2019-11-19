from twitter import *
import csv
import random
from getTweetsInTrending import getTrending

consumer_key = "UDcWtz23Pqj8fZ2ynPoP0rvNl"
consumer_secret = "Ms9hyFReK13kHcpcbGYknkZZCUEVUWSfFadGzR9j9ncodbueHn"
access_token_key = "2456487102-r2SpnynWDvvRrbtQ42K45qKBbcDrvQiBS0kTX9C"
access_token_secret = "wqWWy50LOhTZsf9ayYxDarI8Kf8nbwgUDBTto5NA9vsEF"   

# csv_columns = ['ID', 'Name']
# api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)

api = Twitter(auth = OAuth("2456487102-r2SpnynWDvvRrbtQ42K45qKBbcDrvQiBS0kTX9C", 
                "wqWWy50LOhTZsf9ayYxDarI8Kf8nbwgUDBTto5NA9vsEF", "UDcWtz23Pqj8fZ2ynPoP0rvNl", "Ms9hyFReK13kHcpcbGYknkZZCUEVUWSfFadGzR9j9ncodbueHn"))


woeid_india = 2282863
results = api.trends.place(_id = woeid_india)

print("India Trends")
trends = []
for location in results:
    for trend in location["trends"]:
        trends.append(trend["name"])

trend = random.choice(trends)
print(trend)
print(getTrending(trend))

