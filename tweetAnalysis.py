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

    def get_tweet(self, count=200, screen_name=None, page=1):
        if screen_name is None:
            username = self.username
        else:
            username = screen_name
        if page > 16:
            page = 16

        max_id = None
        all_tweets = []

        for i in range(page):
            print('iteration #', i+1)
            tweets = self.twitter.GetListTimeline(slug=username, owner_screen_name=username, count=count,
                                                  return_json=True, max_id=max_id)
            latest_tweet = tweets[0]
            if max_id is not None:
                tweets.remove(latest_tweet)

            if len(tweets) == 0:
                print("search finished")
                break

            all_tweets.extend(tweets)
            oldest_tweet = tweets[-1]
            max_id = oldest_tweet["id"]
            print("get:", len(all_tweets), "tweets")

        if all_tweets is not None:
            print("found", len(all_tweets), "tweets")

    def get_liked_tweet(self, count=200, screen_name=None, page=1):
        if screen_name is None:
            username = self.username
        else:
            username = screen_name

        max_id = None
        all_tweets = []
        user_list = {}

        for i in range(page):
            print("iteration #", i+1)
            tweets = self.twitter.GetFavorites(screen_name=username, count=count, return_json=True, max_id=max_id)
            latest_tweet = tweets[0]
            if max_id is not None:
                tweets.remove(latest_tweet)

            if len(tweets) == 0:
                print("search finished")
                break

            oldest_tweet = tweets[-1]
            max_id = oldest_tweet["id"]
            all_tweets.extend(tweets)
            print("get:", len(all_tweets), "tweets")
            if len(tweets) == 0:
                print("search finished")
                break
            for tweet in tweets:
                screen_name = tweet["user"]["screen_name"]
                if screen_name in user_list:
                    user_list[screen_name] += 1
                else:
                    user_list[screen_name] = 1
                # print(tweet["user"]["screen_name"])

        user_list = sorted(user_list.items(), key=operator.itemgetter(1), reverse=True)

        return user_list

    # def activity_frequency(self):

    # def top_5_retweeted_tweet(self):

    # def top_5_liked_tweet(self):

    # def top_5_retweeted_account(self):

    def top_5_liked_account(self, count=200, screen_name=None, page=1):
        user_list = self.get_liked_tweet(count=count, screen_name=screen_name, page=page)
        top_5 = user_list[0:5]

        for user, count in top_5:
            print("liked", user, "'s tweet:", count, "times")