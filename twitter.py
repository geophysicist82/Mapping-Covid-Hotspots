

import numpy as np
import pandas as pd
import tweepy
import pandas as pd
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


creds = {}
creds['M7ws0JOoEuadpQyrRBKj6C6RJ'] = "consumer_key"
creds['Cm5I6VX8jVQkCwoPniufImbuyNrLEUdDCfS79JGCRrVK7vshgk'] = "consumer_secret"
creds['1303427067573399552-3W6sslbYwQGFdDnLlW78CJCSF69oOP'] = "access_token"
creds['y981jEcBHW4MNhMCl6MtfmeOdeI9VWVm03ygFug46QaU8'] = "access_token_secret"

#consumer_key= creds['M7ws0JOoEuadpQyrRBKj6C6RJ']
#consumer_secret= creds['Cm5I6VX8jVQkCwoPniufImbuyNrLEUdDCfS79JGCRrVK7vshgk']
#access_token= creds['1303427067573399552-3W6sslbYwQGFdDnLlW78CJCSF69oOP']
#access_token_secret= creds['y981jEcBHW4MNhMCl6MtfmeOdeI9VWVm03ygFug46QaU8']

with open("twitter_credentials.json", "w") as file:
    creds = json.dump(creds,file)

# Set access info to credentials


auth = tweepy.OAuthHandler('M7ws0JOoEuadpQyrRBKj6C6RJ', 'Cm5I6VX8jVQkCwoPniufImbuyNrLEUdDCfS79JGCRrVK7vshgk')
auth.set_access_token('1303427067573399552-3W6sslbYwQGFdDnLlW78CJCSF69oOP', 'y981jEcBHW4MNhMCl6MtfmeOdeI9VWVm03ygFug46QaU8')
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
