import pickle

class PredictSentiment:
    """"""
    def __init__(self, svm_model, vectorizer):
        self.svm_model = pickle.load(open(svm_model, "rb"))
        self.vectorizer = pickle.load(open(vectorizer, "rb"))
        self.tweet_vector = None

    def predict(self, tweet):
        self.tweet_vector = self.vectorizer.transform(tweet)
        return self.svm_model.predict(self.tweet_vector)

