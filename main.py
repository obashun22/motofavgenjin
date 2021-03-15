import os
import tweepy

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status("Hello World via Tweepy!!\nby Heroku")

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#   print('-------------------')
#   print(tweet.text)

# tweets = [tweet for tweet in tweepy.Cursor(api.search, q="#春から名大").items(10) if list(tweet.text[:2]) != ['R', 'T']]
# for tweet in tweets:
#   print('-------------------')
#   print(tweet.text)