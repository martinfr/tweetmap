#Properties 
import ConfigParser

#command line tools
import click

from analytics import TweetAnalytics

@click.command()
@click.option('--max', default=1000, help='maximu number of tweets')
@click.argument('hashtag')
def search(hashtag, max):
	hashtag = hashtag if hashtag.startswith('#') else '#%s' % hashtag 
	config = ConfigParser.RawConfigParser()
	import os.path
	properties_file = 'local.properties' if os.path.isfile('local.properties') else 'analytics.properties'
	config.read(properties_file)
	analytics = TweetAnalytics(config)
	data = analytics.search(hashtag, max)
	data.to_csv('data.csv', sep='\t', encoding = 'utf-8')
	print data

#main
if __name__ == '__main__':
	search()
	
