import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys

consumer_key = "QRlsnKykFrDHIK76iK3nKgiU8"
consumer_secret = "SyKDL2vfCUJEY9tK4lUOzP5GW625CufBvW2yIdyh4CwFmFAaAH"
access_token = "2498124625-ph9rCPCb2GselZoSEGlELqYEhArTc2y0JUQ4vBB"
access_secret = "jLJJ5BW9JNGa3POI2mNpOoUdSn3wccP0cVKDBsJuozplZ"

print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_secret)

try:
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(self.auth)
except:
        print("Error: Authentication Failed")
