import ConfigParser
import tweepy
from tweepy import OAuthHandler
import json
import pandas as pd


class TweetAnalytics:

	def __init__(self, properties):
		self.properties = properties
		#This handles Twitter authetification
		consumer_key = config.get('Twitter', 'auth.consumer_key')
		consumer_secret = config.get('Twitter', 'auth.consumer_secret')
	    	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	    	self.api = tweepy.API(auth)

	def search(self, query, max=1000):

		tweets_data = []

		for tweet in tweepy.Cursor(self.api.search, q = query).items(max):
		    
		    if tweet.user and tweet.user.location:
		      user_location = tweet.user.location 
		      user_timezone = tweet.user.time_zone
		      tweets_data.append({'text': tweet.text, 'lang': tweet.lang, 'user_location': user_location ,'user_timezone':user_timezone})
	
		tweets = pd.DataFrame(data=tweets_data)

		return tweets

if __name__ == '__main__':
	config = ConfigParser.RawConfigParser()
	config.read('analytics.properties')
	analytics = TweetAnalytics(config)
	data = analytics.search("#SuperRugby", 1000)
	data.to_csv('data.csv', sep='\t', encoding = 'utf-8')
	print data
	
