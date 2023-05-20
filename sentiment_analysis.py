import pandas as pd

from sentiment_results import settings

class SentimentAnalysis:
    """"""
    def __init__(self, twitter_train=settings.TWITTER_TRAINING, twitter_val=settings.TWITTER_VALIDATION):
        self.twitter_train = pd.read_csv(twitter_train)
        self.twitter_val = pd.read_csv(twitter_val)
        
    def fn(self):
        pass
