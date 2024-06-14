from fastapi import FastAPI, Query, HTTPException
from pydantic import Required
import uvicorn
from sentiment_result import settings, SentimentResult
from sentiment_analysis import PredictSentiment

ps: PredictSentiment = None

app = FastAPI(
    docs_url="/docs",
    title=settings.app_name,
    description=settings.description,
    version=settings.version,
    contact=settings.contact,
    license_info=settings.license_info,
)

@app.on_event("startup")
def before_first_request():
    """Loads the fasttext models before the first request is completed"""
    global ps
    ps = PredictSentiment(settings.SENTIMENT_MODEL_FILE, settings.VECTORIZER_FILE)        

@app.post('/sentiment/tweet')
def detect_sentiment(
    tweet: str = Query(default=Required, description=""),
    ):
    if type(tweet) != str:
        raise HTTPException(status_code=400, detail="Tweet input must be of type string.")
    sentiment_array = ps.predict(tweet)
    sentiment_num = sentiment_array[0]
    sentiment_category = ps.categorize(sentiment_num)
    return SentimentResult(category=sentiment_category)


if __name__ == '__main__':
    # used for running locally
    uvicorn.run(app, host="127.0.0.1", port=8080) 
