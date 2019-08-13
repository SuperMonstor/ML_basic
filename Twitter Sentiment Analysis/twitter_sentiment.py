#script to check the sentiment of users on a particular topic using ML
#dependancy: tweepy - for accessing api
#dependancy: textblob - For sentiment analysis

import tweepy
from textblob import TextBlob
import csv

consumer_key = 'vFMleeho2492KhtARDnVHqKLL'
consumer_secret = 'kDPjMnIFxGxU0njna1FLGDt3DiDUidqool9ksambsV6JLJSO49'

access_token = '780320587-QclLsAgkgoJnOdKsPCy8ldnRjNercTRJ0NNOKsCY'
access_token_secret = 'FJ1Ow1en3FCDua4d0QmUOwsh65rprw0hqRRMxeWfO3kIY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Tinder') #List of all tweets with keyword 'Tinder'

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    with open('people.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(['This is just a test'])

writeFile.close()

'''
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
'''
