import tweepy

consumer_key = 'tKO8QEjoehEMKmSiWQLE9vh8o'
consumer_secret = '9AbddZs2DyHy1CwP7mrJ7OypDHcK3APGg8LbT9pq2BEgTD5ikk'
access_token = '1371467095972585474-GB9VBsnzOArtcsXgt4VmaTyjBDrAbt'
access_token_secret = 'WCIMsdfaqGGkTN2I8gUPCsbajfDPVPCBxPYH1N4f1DUBZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status("Hello World via Tweepy!!")

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#   print('-------------------')
#   print(tweet.text)

# tweets = [tweet for tweet in tweepy.Cursor(api.search, q="#春から名大").items(10) if list(tweet.text[:2]) != ['R', 'T']]
# for tweet in tweets:
#   print('-------------------')
#   print(tweet.text)