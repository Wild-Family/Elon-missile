import os
import tweepy
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET_KEY')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
    
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("name : %s, screen_name : %s" % (status.user.name,status.user.screen_name))
        print("text : %s " % status.text)
        print("-"*50)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
# filter word
# user_idは、https://idtwi.com/ で調べた
myStream.filter(track=['DOGE'], follow=['44196397'])