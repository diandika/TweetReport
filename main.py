import tkinter

from tweetAnalysis import TweetAnalysis

account = TweetAnalysis()

# account.connect()
account.get_tweet(count=200, screen_name='aimi_sound')
account.get_liked_tweet()

'''
top = tkinter.Tk()

b = tkinter.Button(top, text="button")

b.pack()
top.mainloop()
'''