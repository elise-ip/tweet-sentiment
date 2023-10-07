
from typing import Dict, NamedTuple
from pydantic import BaseModel, BaseSettings


class Settings(BaseSettings):
    app_name: str = ""
    version: str = ""
    description: str = """"""
    contact: Dict = {
        "name": "",
        "url": "",
        "email": "elise.mo.brady@gmail.com",
    }
    license_info: Dict = {
        "name": "CDC Source",
        "url": "https://www.cdc.gov/growthcharts/percentile_data_files.htm",
    }
   
    TWITTER_TRAIN: str = r"data\twitter_training.csv"
    TWITTER_VALIDATION: str = r"data\twitter_validation.csv"

    SENTIMENT_MODEL_FILE: str = "models/lid.176.bin"

settings = Settings()