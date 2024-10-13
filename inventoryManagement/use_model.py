import sqlite3
import pandas as pd
import streamlit as st
from utils import create_secure_connection, display_all_items
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# SQL-Based Recommendation Functions

# Function to fetch unique items from the database
conn = create_secure_connection()
def fetch_unique_items(conn):
    query = "SELECT DISTINCT description FROM item"
    result = pd.read_sql_query(query, conn)
    result = result.loc[:, ~result.columns.duplicated()]  # Drop duplicate columns if they exist
    return result['description'].tolist()


# Function to fetch unique categories from the database
def fetch_unique_categories(conn):
    query = "SELECT DISTINCT category FROM category"
    result = pd.read_sql_query(query, conn)
    result = result.loc[:, ~result.columns.duplicated()]  # Drop duplicate columns if they exist
    return result['category'].tolist()


# Function to search items based on partial matches in description
def search_similar_items(conn, search_query):
    query = "SELECT item.description, item.price, item.unit, qty_on_hand as qoh, manufacturer.name \
             item.price\
             FROM item item INNER JOIN manufacturer ON item.mfr_code = manufacturer.mfr_code \
             WHERE description LIKE ? LIMIT 5"
    result = pd.read_sql_query(query, conn, params=(f'%{search_query}%',))
    result = result.loc[:, ~result.columns.duplicated()]  # Drop duplicate columns if they exist
    return result


# Function to search categories based on partial matches
def search_similar_categories(conn, category_query):
    query = ("SELECT item.description, item.price, item.unit, item.qty_on_hand as qoh, category.category as category \
              FROM item JOIN category ON item.category_code = category.category_code \
              WHERE category LIKE ? LIMIT 10")
    result = pd.read_sql_query(query, conn, params=(f'%{category_query}%',))
    result = result.loc[:, ~result.columns.duplicated()]  # Drop duplicate columns if they exist
    return result


# TF-IDF Model-Based Recommendation Functions

# Function to preprocess data for TF-IDF
def preprocess_for_model(df):
    df['combined_features'] = df['description'] + ' ' + df['category'] + ' ' + df['name']+' ' + str(df['price'])
    df['combined_features'].fillna("", inplace=True)
    df_items = df[df['combined_features'].str.strip() != ""]  # Remove empty rows
    # Clean description and category fields to remove special characters or inconsistent formatting.
    df_items['description'] = df_items['description'].str.lower().str.replace('[^a-zA-Z0-9\s]', '', regex=True)
    return df_items


# Function to build the TF-IDF recommender
def build_tfidf_recommender(df_items):
    custom_stop_words = ['a', 'an', 'the','/']  # Add only general stop words
    tfidf_vectorizer = TfidfVectorizer(stop_words=custom_stop_words)
    # tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    tfidf_matrix = tfidf_vectorizer.fit_transform(df_items['combined_features'])
    return tfidf_vectorizer, tfidf_matrix


# Function to recommend items using TF-IDF and cosine similarity
def recommend_items(user_input, df_items, tfidf_vectorizer, tfidf_matrix, top_n=3):
    user_input_vector = tfidf_vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_input_vector, tfidf_matrix)
    similarity_scores = similarity_scores.flatten()
    top_indices = similarity_scores.argsort()[-top_n:][::-1]  # Sort by similarity score, in descending order
    return df_items.iloc[top_indices]

def model_based_recommendations():

    selection_col, display_col = st.columns([2,2])
    with selection_col:
        # Establish database connection and fetch items
        conn = create_secure_connection('ohs_inventory')
        display_items = display_all_items(conn)
        df = pd.DataFrame(display_items)
        df_items = preprocess_for_model(df)

        # Build the TF-IDF model
        tfidf_vectorizer, tfidf_matrix = build_tfidf_recommender(df_items)

        # Dropdown to select an item for recommendations
        selected_item = st.selectbox(
            "## Select an item for recommendations: For more accurate results, use 'View Inventory'",
            [""] + df_items['description'].unique().tolist(),  # Add an empty option to start
            format_func=lambda x: "Select an item" if x == "" else x
        )

        if selected_item:
            st.subheader("Top 3 Recommended Items")
            recommended_items = recommend_items(selected_item, df_items, tfidf_vectorizer, tfidf_matrix, top_n=3)

            for index, row in recommended_items.iterrows():
                st.markdown(
                    f"""
                    <div style="line-height:1.4; margin-bottom:4px;">
                        <b>Item:</b> {row['description']}<br>
                        <b>Price:</b> {row['price']}<br>
                        <b>Category:</b> {row['category']}<br>
                        <b>Manufacturer:</b> {row['name']}
                    </div>
                    <hr style="margin:5px 0;">
                    """,
                    unsafe_allow_html=True
                )