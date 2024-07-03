from typing import Dict
from pydantic import BaseModel, BaseSettings
import pydantic

class Settings(BaseSettings):
    app_name: str = "tweet-sentiment"
    version: str = "0.0.1"
    description: str = """Locally deployed service to determine tweet sentiment"""
    contact: Dict = {
        "name": "Sentiment Analysis of Tweets",
        "url": "https://github.com/elise-ip/tweet-sentiment",
        "email": "elise.mo.brady@gmail.com",
    }
    license_info: Dict = {
        "name": "Kaggle Twitter Sentiment Analysis Dataset",
        "url": "https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis"
    }
   
    TWITTER_TRAIN: str = r"data/twitter_training.csv"
    TWITTER_VALIDATION: str = r"data/twitter_validation.csv"

    SENTIMENT_MODEL_FILE: str = "models/linear_svm_v0.pkl"
    VECTORIZER_FILE: str = "models/vectorizer.pkl"

settings = Settings()

class Meta(BaseModel):
    category: str
    description: str

class Config:
    arbitrary_types_allowed = True

@pydantic.dataclasses.dataclass(config=Config)
class Category:
    NEUTRAL = Meta(category='Neutral', description='Sentiment of tweet input is considered neutral.')
    POSITIVE = Meta(category='Positive', description='Sentiment of tweet input is considered positive.')
    NEGATIVE = Meta(category='Negative', description='Sentiment of tweet input is considered negative.')
    
class SentimentResult(BaseModel):
    category: Meta
