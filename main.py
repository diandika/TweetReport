import datetime
import tkinter

from dateutil import relativedelta

from tweetAnalysis import TweetAnalysis

account = TweetAnalysis()

now = datetime.datetime.now()
oldest_date_search = now - relativedelta.relativedelta(months=1)

# account.connect()
account.get_tweet(count=200, screen_name='diandika99', page=1, oldest=oldest_date_search)
# account.top_5_liked_account(page=5)

'''
top = tkinter.Tk()

b = tkinter.Button(top, text="button")

b.pack()
top.mainloop()
'''