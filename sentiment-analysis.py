import praw
from praw.objects import MoreComments
from textblob import TextBlob

user_agent = "Soccer Sentiment Analysis bot 1.0 by /u/slack101"
r = praw.Reddit(user_agent=user_agent)
subreddits = ["liverpoolfc", "reddevils", "gunners", "chelseafc", "mcfc", "coys"]
commentsData = {}
for subreddit in subreddits:
    subredditObj = r.get_subreddit(subreddit)
    comments = subredditObj.get_comments(limit=None)
    commentsData[subreddit] = comments

for subreddit in subreddits:
    pol = 0
    i = 0
    mostNegativeComment = ""
    mostPositiveComment = ""
    mostNegativePol = 2
    mostPositivePol = -2
    for comment in commentsData[subreddit]:
        sentence = comment.body    
        wiki = TextBlob(sentence)
        thisPolarity = wiki.sentiment.polarity        
        pol += thisPolarity
        i+=1
        if(thisPolarity > mostPositivePol):
            mostPositivePol = thisPolarity
            mostPositiveComment = sentence
        elif(thisPolarity < mostNegativePol):
            mostNegativePol = thisPolarity
            mostNegativeComment = sentence
        
    print subreddit
    print "most positive comment (" + str(mostPositivePol)  + ") : " + mostPositiveComment
    print "most negative comment (" + str(mostNegativePol)  + ") : " + mostNegativeComment
    print pol/i
    print i
