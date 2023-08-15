import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('C:\\Users\\Zach\\PycharmProjects\\pythonProject3\\files\\steam_games.csv')
df1 = df[["name", "desc_snippet", "popular_tags", "genre", "original_price", "all_reviews"]]
df2 = pd.DataFrame(df1.dropna())

tfidf = TfidfVectorizer(stop_words="english")
matrix = tfidf.fit_transform(df2["desc_snippet"])

tfidf.get_feature_names_out()
matrix.toarray()

cos_similarity = cosine_similarity(matrix, matrix)


def recommender(title, cos_similarity, dataframe):
    indices = pd.Series(dataframe.index, index=dataframe['name'])
    indices = indices[~indices.index.duplicated(keep='last')]
    game_index = indices[title]
    similarity_scores = pd.DataFrame(cos_similarity[game_index], columns=["score"])
    game_indices = similarity_scores.sort_values("score", ascending=False).index

    recommended_games = dataframe.iloc[game_indices]

    # Extract sentiment, percentage, and total reviews from all_reviews column
    recommended_games['review_sentiment'] = recommended_games['all_reviews'].str.extract(r'([A-Za-z\s]+),')[0]
    recommended_games['review_percentage'] = recommended_games['all_reviews'].str.extract(r'(\d+)%')[0]
    recommended_games['review_percentage'] = recommended_games['review_percentage'].fillna(-1).astype(int)
    recommended_games['total_reviews'] = recommended_games['all_reviews'].str.extract(r'of the (\d+)')[0]
    recommended_games['total_reviews'] = recommended_games['total_reviews'].str.replace(',', '').fillna(-1).astype(int)

    # Filter by games with Very Positive, Mostly Positive, or Overwhelmingly Positive reviews (>= 75%)
    positive_reviews = ['Very Positive', 'Mostly Positive', 'Overwhelmingly Positive']
    recommended_games = recommended_games[
        (recommended_games['review_sentiment'].isin(positive_reviews)) &
        (recommended_games['total_reviews'] >= 75)
        ]

    return recommended_games[['name', 'genre', 'original_price', 'review_sentiment']]

