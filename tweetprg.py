import tweepy
from textblob import TextBlob

consumer_key = '2hbRH7jbhgZjDvVAgQk6y6BiI'
consumer_secret = '2nyJ1nEOjtqMlpvN0IItAoAOixbWe50LXQKh8qzI9NPZM8eFMB'

access_token = '33869382-iKWf4SA3Yb7TUPfUqF1MXoAIq45puCTfw09WQOKof'
access_token_secret = 'efJtnpHKnO63skY3wFWOpzG3CPlUXXNPhiOpTZseOAi89'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search("Datascience")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
