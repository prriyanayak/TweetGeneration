import pandas as pd
import re

def cleanTheTweets(topic):
    result = pd.read_csv(topic+'.csv')

    tweets = result.iloc[:, 1].tolist()

    finaltweets = []

    for i in tweets:
        # get only text
        i = i.replace("b\'", "")
        i = i.replace("\'", "")
        i = i.replace("\\n", "")
        
        finaltweets.append(i)

    df = pd.DataFrame({'col':finaltweets})


    df = df['col'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])

    list = []

    for i in df: 
        list.append(i)




    return list


