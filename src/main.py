import os
import tweepy
from discordwebhook import Discord
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET_KEY')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

discord_webhook_url = 'https://discordapp.com/api/webhooks/839413656479203338/DxeFU641GxLeVRLZ-VoMBUos7TL8Dlc4JAqQ2u6qZvFpabZhIaHbj7mhasoW98c2ybRk'

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#discordのウェブフック
discord = Discord(url=discord_webhook_url)
    
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if "@" in status.text and not "DOGE" in status.text:
           pass
        else:
            print("name : %s, screen_name : %s" % (status.user.name,status.user.screen_name))
            print("text : %s " % status.text)
            print("-"*50)
            
            discord.post(content="Elon Musk mentioned DOGE!! \n" + status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# filter word
# user_idは、https://idtwi.com/ で調べた
myStream.filter(follow=['44196397'])