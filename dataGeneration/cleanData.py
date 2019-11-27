import pandas as pd
import re

def cleanTheTweets(topic):
    result = pd.read_csv(topic+'.csv')

    tweets = result.iloc[:, 1].tolist()

    finaltweets = []
    data = []
    for tweet in tweets:
        if 'RT' not in tweet:
            data.append(tweet)

    for i in data:
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
    # return list


    list_ans = list
    with open(topic+'.txt', 'w') as f:
        for item in list_ans:
            f.write("%s\n" % item)
    return list
