import twitter
import json


class TweetAnalysis:
    def __init__(self, username="diandika99"):
        file = open("api_key.json", "r")
        api_json = json.load(file)
        self.consumer_key = api_json["CONSUMER_KEY"]
        self.consumer_secret_key = api_json["CONSUMER_SECRET_KEY"]
        self.acces_token = api_json["ACCESS_TOKEN"]
        self.acces_secret_token = api_json["ACCESS_SECRET_TOKEN"]
        self.username = username

    def connect(self):
        twitter_connection = twitter.Api(consumer_key=self.consumer_key,
                              consumer_secret=self.consumer_secret_key,
                              access_token_key=self.acces_token,
                              access_token_secret=self.acces_secret_token)
        print(twitter_connection.VerifyCredentials())

    # def activity_frequency(self):

    # def top_5_retweeted_tweet(self):

    # def top_5_liked_tweet(self):

    # def top_5_retweeted_account(self):

    # def top_5_liked_account(self):
