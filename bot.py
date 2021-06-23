#import tweepy

consumer_key = ''
consumer_secret = ''
key = ''
secret = ''

# using twitter authentication sys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

# api obj 
api = tweepy.API(auth)
api.update_status('tweepy + oauth!')
