import tweepy
import os

#Consumer_Key_and_secret: Think of these as the user name and password that represents your App when making API requests.
#Access_token_and_secret: An Access Token and Secret are user-specific credentials used to authenticate OAuth 1.0a API requests. 
#                         They specify the Twitter account the request is made on behalf of.

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_KEY_SECRET = os.environ.get('CONSUMER_KEY_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


#Authenticating to Twitter for API v2 using CLient class
client = tweepy.Client(consumer_key= CONSUMER_KEY, consumer_secret= CONSUMER_KEY_SECRET, access_token= ACCESS_TOKEN,
        access_token_secret= ACCESS_TOKEN_SECRET)

#Making a Tweet to launch off
# client.create_tweet(text='Bot dev testing')

client.get_bookmarks()