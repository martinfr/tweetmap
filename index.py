#Properties 
import ConfigParser

#command line tools
import click

from analytics import TweetAnalytics

@click.command()
@click.option('--max', default=10, help='maximum number of tweets')
@click.argument('hashtag')
def index(hashtag, max):
	hashtag = hashtag if hashtag.startswith('#') else '#%s' % hashtag 
	config = ConfigParser.RawConfigParser()
	import os.path
	properties_file = 'local.properties' if os.path.isfile('local.properties') else 'analytics.properties'
	config.read(properties_file)
	analytics = TweetAnalytics(config)
	data = analytics.index(hashtag, max)
	print data

#main
if __name__ == '__main__':
	index()
	
