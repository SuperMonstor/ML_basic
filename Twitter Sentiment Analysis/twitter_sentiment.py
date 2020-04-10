#script to check the sentiment of users on a particular topic using ML
#dependancy: tweepy - for accessing api
#dependancy: textblob - For sentiment analysis

import tweepy
from textblob import TextBlob
import csv

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

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
