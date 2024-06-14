# tweet-sentiment
This sentiment analysis project takes in a text tweet and determines the appropriate sentiment according to the emotional language being used. It employs a TF-IDF vectorizer to manage the text and feeds the vectorized values through a Support Vector Machine (SVM) to provide the category.

##### Model
An SVM is trained from a large dataset of tweets to determine the sentiment of future tweets. 

##### API Layer
The project showcases how to use the FastAPI Framework as an API Layer to deploy a machine learning model locally.

##### Data
Data for this project comes from the Kaggle Dataset: `Twitter Sentiment Analysis` found [here](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis).
