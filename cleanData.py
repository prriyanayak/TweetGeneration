import pandas
import re

def cleanTheTweets(topic):
    result = pandas.read_csv(topic+'.csv')

    tweets = result.iloc[:, 1].tolist()

    finaltweets = []

    for i in tweets:
        # get only text
        i = i.replace("b\'", "")
        i = i.replace("\'", "")
        i = i.replace("\\n", "")
        
        finaltweets.append(i)
    return finaltweets
