import pickle
from sentiment_results import settings

class PredictSentiment:
    """"""
    def __init__(self, model_file):
            # TODO: load svm model
            self._model_file = model_file
            self.svm_model = pickle.load(open("linear_svm.pkl", "rb"))

            # TODO: save and load in vectorizer
            self.vectorizer = []
            self.tweet_vector = None

    def predict(self, tweet):
        self.tweet_vector = self.vectorizer.transform(tweet)
        return self.svm_model.predict(self.tweet_vector)
