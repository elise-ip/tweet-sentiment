# tweet-sentiment
This service project takes in a text tweet and determines the appropriate sentiment according to the emotional language being used. It employs a TF-IDF vectorizer to manage the text and feeds the vectorized values through a Support Vector Machine (SVM) to provide the category.

### Layout
| Folder | Description |
| --- | --- |
| [`/data`](/data) | Data files |
| [`/exp`](/exp) | Experiments and ad-hoc analysis, model training |
| [`/models`](/models) | Trained models |
| [`/src`](/src) | Source code, packages, openapi specification |
| [`/`](/root.md) | Root project files (README, requirements, app frontend) |

### Model Training
An SVM is trained from a large dataset of vectorized tweets and their respective sources to determine the sentiment of future tweets. 

### API Layer
The project showcases how to use the FastAPI Framework as an API Layer to deploy a machine learning model locally.

### Data
Data for this project comes from the Kaggle Dataset: `Twitter Sentiment Analysis` found [here](https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis).

### Model Performance
The following table depicts the performance of the SVM model to identify tweet sentiment. 

| Category     | Precision | Recall | F1-Score |
|--------------|-----------|--------|----------|
| 0 (Negative) | 0.89      | 0.88   | 0.89     |
| 1 (Neutral)  | 0.93      | 0.91   | 0.92     |
| 2 (Positive) | 0.89      | 0.92   | 0.90     |

| Accuracy |
|----------|
| 0.90     |
