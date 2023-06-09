import os

import tweepy
from dotenv import load_dotenv
from twitter.account import Account

load_dotenv()

TWITTER_API_KEY = os.environ["TWITTER_API_KEY"]
TWITTER_API_SECRET = os.environ["TWITTER_API_SECRET"]
TWITTER_ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
TWITTER_ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
EMAIL = os.environ["EMAIL"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

def setup_tweepy_client():
    return tweepy.Client(
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    )

def setup_account():
    return Account(EMAIL, USERNAME, PASSWORD, debug=2, save=True)
