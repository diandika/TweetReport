import tkinter

from tweetAnalysis import TweetAnalysis

account = TweetAnalysis()

# account.connect()
# account.get_tweet(count=200, screen_name='diandika99', page=5)
account.get_liked_tweet(page=4)

'''
top = tkinter.Tk()

b = tkinter.Button(top, text="button")

b.pack()
top.mainloop()
'''