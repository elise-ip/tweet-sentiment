import pickle
import joblib
import pandas as pd

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

