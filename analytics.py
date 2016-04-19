#twitter api
import tweepy
from tweepy import OAuthHandler

#Dataframe
import pandas as pd

#elasticsearch
from elasticsearch import Elasticsearch


class TweetAnalyzer:

	def analyze(self, tweet):		

		user_location = tweet.user.location 
		user_timezone = tweet.user.time_zone
		data = 	{
			'text': tweet.text, 
			'lang': tweet.lang, 
			'user_location': user_location ,
			'user_timezone':user_timezone, 
			'created_at': tweet.created_at
		}
		
		return data


class TweetAnalytics:

	def __init__(self, properties):
		self.properties = properties
		#This handles Twitter authetification
		consumer_key = properties.get('Twitter', 'auth.consumer_key')
		consumer_secret = properties.get('Twitter', 'auth.consumer_secret')
	    	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	    	self.api = tweepy.API(auth)

	def search(self, query, max=1000):

		tweets_data = []
		analyzer = TweetAnalyzer()

		for tweet in tweepy.Cursor(self.api.search, q = query).items(max):
		    
		    if tweet.user and tweet.user.location:
		      tweets_data.append(analyzer.analyze(tweet))

		return pd.DataFrame(data=tweets_data)

	def index(self, query, max=1000):
	
		es = Elasticsearch()
		analyzer = TweetAnalyzer()
		
		for tweet in tweepy.Cursor(self.api.search, q = query).items(max):
			document = analyzer.analyze(tweet)
            		es.create("tweets", "tweets", document)
 		
	
