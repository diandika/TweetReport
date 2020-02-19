import tkinter

from tweetAnalysis import TweetAnalysis

account = TweetAnalysis()

# account.connect()
# account.get_tweet(count=200, screen_name='diandika99', page=5)
account.top_5_liked_account(page=5)

'''
top = tkinter.Tk()

b = tkinter.Button(top, text="button")

b.pack()
top.mainloop()
'''