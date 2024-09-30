# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st

pd.set_option('display.max_columns', 15)
st.set_page_config(layout="wide")
# Load the dataset
@st.cache_data
def load_data():
    url = "https://github.com/YBI-Foundation/Dataset/raw/main/Movies%20Recommendation.csv"
    df = pd.read_csv(url)
    return df


# Preprocess the data (combining genre, director, and cast into one feature)
def preprocess_data(df):
    df['Movie_Genre'] = df['Movie_Genre'].fillna('')  # Fill missing values in 'Movie_Genre'
    df['Movie_Director'] = df['Movie_Director'].fillna('')  # Fill missing values in 'Movie_Director'
    df['Movie_Cast'] = df['Movie_Cast'].fillna('')  # Fill missing values in 'Movie_Cast'

    # Combine columns to create a 'combined_features' column
    df['combined_features'] = df['Movie_Genre'] + ' ' + df['Movie_Director'] + ' ' + df['Movie_Cast']
    return df


# Build a content-based recommender using cosine similarity
def build_recommender(df):
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(df['combined_features'])

    # Compute the cosine similarity matrix based on the count matrix
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    return cosine_sim


# Get movie recommendations based on the cosine similarity
def get_recommendations(movie_title, df, cosine_sim):
    try:
        # Get the index of the movie that matches the title
        movie_index = df[df['Movie_Title'] == movie_title].index[0]

        # Get similarity scores for all movies with that movie
        similarity_scores = list(enumerate(cosine_sim[movie_index]))

        # Sort the movies based on the similarity scores
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        # Get the indices of the 10 most similar movies
        top_movie_indices = [i[0] for i in sorted_scores[1:6]]  # Exclude the first one (itself)

        # Return the top 10 most similar movies
        return df['Movie_Title'].iloc[top_movie_indices]
    except IndexError:
        return ["Movie not found in the dataset. Please try a different movie."]


# Streamlit app
def main():
    st.markdown('#### Movie Recommender System')

    # Load and preprocess the data
    df = load_data()
    df = preprocess_data(df)

    # Build the recommender model
    cosine_sim = build_recommender(df)
    entry_col, display_col = st.columns(2)
    # User input: Enter at least 4 characters to search for a movie
    with entry_col:
        search_query = st.text_input('Enter at least 4 characters of the movie title you wish to search:')

        # Only show the selectbox if the search query has at least 4 characters
        if len(search_query) >=4:
           #Filter movies based on the search query
           filtered_movie_list = df[df['Movie_Title'].str.contains(search_query, case=False)]['Movie_Title'].tolist()

        # If movies match the search query, display them in the selectbox
           if filtered_movie_list:
              selected_movie = st.selectbox('Select a movie:', options=[""] + filtered_movie_list,
                                          format_func=lambda x: 'Click to select' if x == "" else x)
        # Recommend movies based on user input
              if selected_movie and st.button('Recommend'):
                 with display_col:
                    recommendations = get_recommendations(selected_movie, df, cosine_sim)
                    st.write(f'Recommended movies for "{selected_movie}":')
                    for i, movie in enumerate(recommendations):
                       st.write(f"{i + 1}. {movie}")
        else:
            st.write('No movies found matching your search.')

# Run the Streamlit app
if __name__ == '__main__':
    main()