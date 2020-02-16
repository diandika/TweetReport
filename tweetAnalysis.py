import twitter
import json

import operator

class TweetAnalysis:
    def __init__(self, username="diandika99"):
        file = open("api_key.json", "r")
        api_json = json.load(file)
        self.twitter = twitter.Api(consumer_key=api_json["CONSUMER_KEY"],
                                   consumer_secret=api_json["CONSUMER_SECRET_KEY"],
                                   access_token_key=api_json["ACCESS_TOKEN"],
                                   access_token_secret=api_json["ACCESS_SECRET_TOKEN"])
        self.username = username

    def connect(self):
        print(self.twitter.VerifyCredentials())

    def get_tweet(self, count=200, screen_name=None):
        if screen_name is None:
            username = self.username
        else:
            username = screen_name
        print(count, username)
        tweets = self.twitter.GetListTimeline(slug=username, owner_screen_name=username, count=count, return_json=True)
        count = 0
        tweet_list = []
        for tweet in tweets:
            if "RT" in tweet["text"]:
                tweet_list.append(tweet["text"])
                count = count + 1
        print("retweeted tweet count:", count)

    def get_liked_tweet(self, count=200, screen_name=None):
        if screen_name is None:
            username = self.username
        else:
            username = screen_name
        print(count, username)
        tweets = self.twitter.GetFavorites(screen_name=username, count=count, return_json=True)
        user_list = {}
        for tweet in tweets:
            screen_name = tweet["user"]["screen_name"]
            if screen_name in user_list:
                user_list[screen_name] += 1
            else:
                user_list[screen_name] = 1
            # print(tweet["user"]["screen_name"])

        user_list = sorted(user_list.items(), key=operator.itemgetter(1), reverse=True)

        for user, count in user_list:
            print(user, ':', count)

    # def activity_frequency(self):

    # def top_5_retweeted_tweet(self):

    # def top_5_liked_tweet(self):

    # def top_5_retweeted_account(self):

    # def top_5_liked_account(self):
