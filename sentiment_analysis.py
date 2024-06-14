import pickle
import joblib
import pandas as pd
from sentiment_result import Meta, Category

class PredictSentiment:
    """"""
    def __init__(self, svm_model, vectorizer):
        self.svm_model = pickle.load(open(svm_model, "rb"))
        self.vectorizer = joblib.load(vectorizer)
        self.tweet_vector = None

    def predict(self, tweet):
        tweet_preproc = pd.Series(tweet)
        self.tweet_vector = self.vectorizer.transform(tweet_preproc)
        print(type(self.tweet_vector))
        return self.svm_model.predict(self.tweet_vector)
    
    def categorize(self, category_num: int) -> Meta:
        if category_num == 0:
            sentiment = Category.NEGATIVE
        if category_num == 1:
            sentiment = Category.NEUTRAL
        if category_num == 2:
            sentiment =  Category.POSITIVE
        return sentiment

