import os
import asyncio
import sys
import tweepy
import pybotters
from discordwebhook import Discord
from dotenv import load_dotenv
load_dotenv()

# 環境変数
#Twitter
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET_KEY')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

#FTX
ftx_api_key = os.getenv('FTX_API_KEY')
ftx_api_secret = os.getenv('FTX_API_SECRET')

#Discord
discord_webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

FTX_API_KEY = os.getenv('FTX_API_KEY')
FTX_API_SECRET = os.getenv('FTX_API_SECRET')

api = {
    'ftx':[FTX_API_KEY , FTX_API_SECRET],
}

parameters = {
  "market": "DOGE-USD",
  "side": "buy",
  "price": None,
  "type": "market",
  "size": 10,
  "reduceOnly": False
}

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#discordのウェブフック
discord = Discord(url=discord_webhook_url)
class MyStreamListener(tweepy.StreamListener):
    async def on_status(self, status):
        if 44196397 == status.user.id and "DOGE" in status.text:
            if discord is not None:
                discord.post(content="Elon Musk mentioned DOGE!! \n" + status.text)
            else:
                pass
            if FTX_API_KEY == None or FTX_API_SECRET == None:
                    print('no env')
                    sys.exit(1)
            
            else:
                async with pybotters.Client(apis=api, base_url='https://ftx.com/api') as client:
                    resp = await client.post('/orders', data=parameters)
                    print(resp)
        else:
            pass

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# filter word
# user_idは、https://idtwi.com/ で調べた
myStream.filter(follow=['44196397'])