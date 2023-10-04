from fastapi import FastAPI, Query
from pydantic import Required
import uvicorn
from sentiment_results import settings

app = FastAPI(
    docs_url="/docs",
    title=settings.app_name,
    description=settings.description,
    version=settings.version,
    contact=settings.contact,
    license_info=settings.license_info,
)

@app.post('/sentiment/tweet')
def detect_sentiment(
    tweet: str = Query(default=Required, description=""),
    ):
    """
    """



if __name__ == '__main__':
    # used for running locally
    uvicorn.run(app, host="127.0.0.1", port=8000) 
