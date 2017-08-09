from django.shortcuts import render

from twitter import Twitter, OAuth
from HTMLParser import HTMLParser

# Variables that contain the user credentials to access Twitter API
ACCESS_TOKEN = '160055720-0WR63cF8OvhAbkjEePf3ZT83hI1MkL7FCVrvFHxR'
ACCESS_SECRET = 'BrPJQxMFjfwL6DSZwOe3sGV3sikPjsZ7s4slQQTkYzVb7'
CONSUMER_KEY = 'E8McWg4korwxzw5g7SelDtN1D'
CONSUMER_SECRET = 'pZawz4825aDZ3ZFInlpwIO6Bpc8ZMmNhT9a7BQgK4QUEFTggMS'

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
