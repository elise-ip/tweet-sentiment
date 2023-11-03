
from typing import Dict, NamedTuple
from pydantic import BaseModel, BaseSettings


class Settings(BaseSettings):
    app_name: str = "tweet-sentiment"
    version: str = "0.0.1"
    description: str = """"""
    contact: Dict = {
        "name": "Sentiment Analysis of Tweets",
        "url": "https://github.com/elise-ip/tweet-sentiment",
        "email": "elise.mo.brady@gmail.com",
    }
    license_info: Dict = {
        "name": "Kaggle Twitter Sentiment Analysis Dataset",
        "url": "https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis",
    }
   
    TWITTER_TRAIN: str = r"data\twitter_training.csv"
    TWITTER_VALIDATION: str = r"data\twitter_validation.csv"

    SENTIMENT_MODEL_FILE: str = "models\linear_svm_v0.pkl"

settings = Settings()