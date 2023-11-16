import re
import requests
import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler
import pyodide_http
import json
import config

'''After importing the required dependencies, the patch_all() function is called early
to patch the Requests library to function with the pyscript environment.
More info on: https://docs.pyscript.net/latest/tutorials/requests.html'''
pyodide_http.patch_all()

#An object 'twitter_client' is constructed with web parsing methods and sentiment analysis functions
class twitter_client():

    def __init__(self):
        consumer_key = config.twitter_consumer_key
        consumer_secret = config.twitter_consumer_secret
        access_token = config.twitter_access_token
        access_token_secret = config.twitter_access_token_secret

        #Attempts authentication whether the user-specific keys above are validated by Twitter servers.
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error, Authentication Failed")

    #Utility function to remove links and other special characters from tweet text to filter words into textblob
    def filter_tweets(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())



    def sentiment_analyzer(self, tweet):
        #receives TextBlob object with the filtered tweets passed into as argument
        result = TextBlob(self.filter_tweets(tweet))
        
        #Filters unimportant words and sets sentiment from scale of -1.0 to 1.0
        if result.sentiment.polarity >= 0:
            return 'Positive'
        elif result.sentiment.polarity < 0:
            return 'Negative'

    def get_tweets(self, query, count):
        tweets = []
        iterator = 0

        #request method which concatenates the generic urls with headers and the query string from user input
        url = "https://twitter154.p.rapidapi.com/search/search"

        querystring = {"query": query, "limit": str(count),"section":"top"}

        headers = {
	        "X-RapidAPI-Key": config.Rapid_api_key,
	        "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = json.loads(response.text)
        iterator = 0
        #iterates through all the tweet texts from the json data and sets sentiment for each
        while iterator < len(data["results"]):
            parsed_tweet = {}
            parsed_tweet['word'] = data["results"][iterator]["text"]
            parsed_tweet['sentiment'] = self.sentiment_analyzer(data["results"][iterator]["text"])

            #Filters unwanted retweets to ensure each tweet entry in list tweets is unique
            if data["results"][iterator]["retweet_count"] > 0:
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)
            iterator += 1
        return tweets


