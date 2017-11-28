from credentials import app_key, app_secret, oauth_token, oauth_token_secret
import oauth2
import csv 
import json
import tweepy
import time
import os

consumer_key = app_key
consumer_secret = app_secret
access_token = oauth_token
access_token_secret = oauth_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#query_params = api.search, q='egypt, terror'

filename = "data_collected"

script_dir = os.path.dirname(__file__)
rel_path = filename + ".txt"
file_path = os.path.join(script_dir, rel_path)

TwitterData = tweepy.Cursor(api.search, q='egypt, terror', lang='en').items()

with open(file_path, 'w') as out:
  for tweet in TwitterData:
    data = str(tweet.created_at) + tweet.text
    out.write(data + '\n')
