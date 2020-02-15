import twitter

CONSUMER_KEY = '2FNkTi5ORWCvMmHy9gmuay3x4'
CONSUMER_SECRET_KEY = 'IUv0UF7NeQ1c1LZYvDwZs1SYRJ8o3cWIeSrBEdLUP4ZFjF7oPe'
ACCESS_TOKEN = '845123262-Iyq1hogBBYMlw8QfupmI3PPsycz0Sf43mUgCA4Q1'
ACCESS_SECRET_TOKEN = 'D4N2ZpjK85ieXYumpQcsCCJSGKZmJniTayFC7QYYuADrd'


class TweetAnalysis:
    def __init__(self, username="diandika99"):
        self.consumer_key = CONSUMER_KEY
        self.consumer_secret_key = CONSUMER_SECRET_KEY
        self.acces_token = ACCESS_TOKEN
        self.acces_secret_token = ACCESS_SECRET_TOKEN
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
