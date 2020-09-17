

import numpy as np
import pandas as pd
import tweepy
import pandas as pd
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


creds = {}
creds['key'] = "consumer_key"
creds['secret'] = "consumer_secret"
creds['token'] = "access_token"
creds['token secret'] = "access_token_secret"


with open("twitter_credentials.json", "w") as file:
    creds = json.dump(creds,file)

# Set access info to credentials


auth = tweepy.OAuthHandler('key', 'secret')
auth.set_access_token('token', 'token secret')
api = tweepy.API(auth, wait_on_rate_limit=True)

#search_words = "'covid' -filter:retweets"
#date_since = "2020-03-01"
#result_type = "mixed"

tweets = tweepy.Cursor(api.search,
                       q="'covid' -filter:retweets",
                       lang="en",
                       since="2020-03-01",
                       result_type="mixed",
#                        since_id=since_id
                      ).items(500)
tweets

tweets_json = [[
                tweet.user.screen_name,
                tweet.id_str,
                tweet.created_at,
                tweet.coordinates,
                tweet.place,
                tweet.text,
                tweet.geo
                ] for tweet in tweets]

df = pd.DataFrame(tweets_json, columns = [
                                        'screen_name',
                                        'id_str',
                                        'created_at',
                                        'coordinates',
                                        'place',
                                        'text',
                                        'geo_location'
                                               ])

df.head(5)
