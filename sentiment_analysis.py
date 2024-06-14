import pickle
import joblib
import pandas as pd
from sentiment_result import Meta, Category

class PredictSentiment:
    """This class takes in a text tweet and return the appropriate sentiment category.
    """
    def __init__(self, svm_model, vectorizer):
        self.svm_model = pickle.load(open(svm_model, "rb"))
        self.vectorizer = joblib.load(vectorizer)
        self.tweet_vector = None

    def predict(self, tweet: str):
        """Predicts the numeric sentiment according to a text input tweet by vectorizing and running through svm model.

        Args:
            tweet (str): Tweet text input

        Returns:
            sentiment result (int): Numeric sentiment value
        """
        tweet_preproc = pd.Series(tweet)
        self.tweet_vector = self.vectorizer.transform(tweet_preproc)
        print(type(self.tweet_vector))
        return self.svm_model.predict(self.tweet_vector)
    
    def categorize(self, category_num: int) -> Meta:
        """Reformats numeric sentiment result as a Category.

        Args:
            category_num (int): numeric category value

        Returns:
            Meta: Class with mapped category and description
        """
        if category_num == 0:
            sentiment = Category.NEGATIVE
        if category_num == 1:
            sentiment = Category.NEUTRAL
        if category_num == 2:
            sentiment =  Category.POSITIVE
        return sentiment

