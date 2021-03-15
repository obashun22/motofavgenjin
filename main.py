import tweepy

consumer_key = 'GIWsX69vEJKFhSWDcrLY42nfN'
consumer_secret = '2UlvfJDRyjhPr3tFRck8BmxIrXSGGeNGrbFAjCs58IrTIULYpi'
access_token = '2741307938-PSB4fMuoJesPPHrYPnCrZudzRuJcWM54HcBej9D'
access_token_secret = 'SZisTjWDRWrQntGyjkaREvDD1a0OFz5XHg0AMcGio60Qs'

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