import streamlit as st
from utils import *
import sqlite3
# Streamlit interface

# Function to fetch unique items from the database
# Function to fetch unique items from the database
# Function to fetch unique items from the database
# Function to fetch unique items from the database

conn = create_secure_connection('ohs_inventory')
def fetch_unique_items(conn):
    query = "SELECT DISTINCT description FROM item"
    result = pd.read_sql_query(query, conn)

    # Drop duplicate columns if they exist
    result = result.loc[:, ~result.columns.duplicated()]

    return result['description'].tolist()

# Function to fetch unique categories from the database
def fetch_unique_categories(conn):
    query = "SELECT DISTINCT category FROM category"
    result = pd.read_sql_query(query, conn)

    # Drop duplicate columns if they exist
    result = result.loc[:, ~result.columns.duplicated()]

    return result['category'].tolist()

# Function to search items based on partial matches in description (up to 5 results)
def search_similar_items(conn, search_query):
    query = "SELECT item.description, item.price, item.unit,qty_on_hand as qoh, manufacturer.name as Manufacturer \
    FROM item item inner join manufacturer on item.mfr_code = manufacturer.mfr_code\
             WHERE description LIKE ? LIMIT 5"

    result = pd.read_sql_query(query, conn, params=(f'%{search_query}%',))

    # Drop duplicate columns if they exist
    result = result.loc[:, ~result.columns.duplicated()]

    return result

# Function to search categories based on partial matches (up to 5 results)
def search_similar_categories(conn, category_query):
    query = ("SELECT item.description, item.price,item.unit,item.qty_on_hand as qoh, category.category as category,\
      manufacturer.name as Manufacturer\
      FROM item\
     JOIN category ON item.category_code = category.category_code\
     JOIN manufacturer on item.mfr_code = manufacturer.mfr_code\
     WHERE category LIKE ? LIMIT 10")
    result = pd.read_sql_query(query, conn, params=(f'%{category_query}%',))

    # Drop duplicate columns if they exist
    result = result.loc[:, ~result.columns.duplicated()]

    return result

# Streamlit interface
def app():
    st.title("Inventory Search")

    # Establish connection to the database
    # Set up two columns: one smaller for the search box and button, one larger for results
    search_col, result_col = st.columns([1, 2])  # Search column is smaller, result column is larger

    with search_col:
        # Set up search options
        search_option = st.radio('Search by:', ['Category', 'Item'])

        if search_option == 'Category':
            # Fetch unique categories from the database for the dropdown
            categories = fetch_unique_categories(conn)
            selected_category = st.selectbox('Select Category', categories)

            # Add the search button directly under the category selection box
            search_clicked = st.button('Search')

        elif search_option == 'Item':
            # Fetch unique items from the database for the dropdown
            items = fetch_unique_items(conn)
            selected_item = st.selectbox('Select Item', items)

            # Add the search button directly under the item selection box
            search_clicked = st.button('Search')


    if search_option == 'Category' and selected_category and search_clicked:
        # Search for similar categories (partial match, max 5 results)
        result = search_similar_categories(conn, selected_category)
        if not result.empty:
            st.write('Your searched Results:', result)
        else:
            st.warning('No similar categories found.')

    elif search_option == 'Item' and selected_item and search_clicked:
        # Search for similar items (partial match, max 5 results)
        result = search_similar_items(conn, selected_item)
        if not result.empty:
            st.write('Top 5 similar items:', result)
        else:
            st.warning('No similar items found.')
