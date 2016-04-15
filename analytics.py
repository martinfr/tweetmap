#twitter api
import tweepy
from tweepy import OAuthHandler

#Dataframe
import pandas as pd

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

		for tweet in tweepy.Cursor(self.api.search, q = query).items(max):
		    
		    if tweet.user and tweet.user.location:
		      user_location = tweet.user.location 
		      user_timezone = tweet.user.time_zone
		      tweets_data.append({'text': tweet.text, 'lang': tweet.lang, 'user_location': user_location ,'user_timezone':user_timezone})

		return pd.DataFrame(data=tweets_data)
