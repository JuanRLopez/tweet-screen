import os

from django.shortcuts import render
from twitter import Twitter, OAuth
from HTMLParser import HTMLParser

# Variables that contain the user credentials to access Twitter API
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


def tweet_screen(request):

    twitter = Twitter(auth=oauth)
    response = twitter.search.tweets(q='from:' + request.GET.get('screen_name', ''), result_type='recent', count=1)
    tweet = response['statuses'][0]
    h = HTMLParser()

    return render(request, 'screen_app/display.html', {'screen_name': h.unescape(tweet['user']['screen_name']),
                                                       'name': h.unescape(tweet['user']['name']),
                                                       'profile_pic': tweet['user']['profile_image_url'],
                                                       'tweet': h.unescape(tweet['text']),
                                                       'date_time': tweet['created_at'], })
