from django.core.management.base import BaseCommand
from twitter import TwitterStream, OAuth
from twitter_scrape.models import TwitterLocation
from server.settings import DBNAME
import mongoengine as mongo
import datetime
import time


OAUTH_TOKEN = '1373732868-rJSi4IAzTh5ruvimgs4NxsrZUtOOgKT8LLceeU'
OAUTH_SECRET = 'LtPxpNbsiy5tWgMd1SfEaEvt0NPlkXvRH3ky1hkovw'
CONSUMER_KEY = 'A7R0OmDF2kJvdIwHkYaSaA'
CONSUMER_SECRET = 'FDFfHcKyr2vxa33qMghDPETi2CfztsxC9LPVNyJe0'

LON1, LAT1, LON2, LAT2 = (-122.23, 37.32, -122.09, 37.49)

locations_args = "%f,%f,%f,%f" % (LON1, LAT1, LON2, LAT2)

def write_to_db(tweet):
    taken_time = datetime.datetime.fromtimestamp(int(time.mktime(time.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y"))))
    location = TwitterLocation(
        coordinates = tweet['coordinates'],
        timestamp = taken_time,
        time_added_to_db = datetime.datetime.now(),
        source = "twitter",
        tweet_text = tweet['text'],
        retweet_count = tweet['retweet_count'],
        favorite_count = tweet['favorite_count'],
        hashtags = tweet['entities']['hashtags'],
        user_id = tweet['user']['id']
    )
    print "saving location"
    location.save()

def main():
    twitter_stream = TwitterStream(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )
    iterator = twitter_stream.statuses.filter(locations=locations_args)
    for tweet in iterator:
        print tweet
        try:
            write_to_db(tweet)
        except:
            pass


class Command(BaseCommand):
    def handle(self, *args, **options):
        mongo.connect(DBNAME)
        main()

