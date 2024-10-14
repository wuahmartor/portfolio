import sqlite3
import getpass
import streamlit as st
import pandas as pd
import os


# Authentication function
def authenticate_user(username, password):
    """
    Authenticates the user by checking the provided username and password.
    """
    # Hardcoded credentials (Avoid hardcoding in production)
    valid_username = "admin"
    valid_password = "Admin123"

    if username == valid_username and password == valid_password:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed. Invalid username or password.")
        return False


# Function to create a secure connection using a context manager
def create_secure_connection():
    """Create a secure connection to the SQLite database."""
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'ohs_inventory')  # Ensure the correct path
        conn = sqlite3.connect(db_path, check_same_thread=False)  # Allow multi-threaded access
        print("Connected to the database successfully.")
        return conn
    except sqlite3.Error as e:
        st.error(f"Database connection error: {e}")
        return None


# Fetch and display items from the category table using a context manager
def display_category_items():
    query = """
        SELECT item.description, item.price, item.unit, item.qty_on_hand AS QOH, 
               manufacturer.name AS manufacturer
        FROM item
        INNER JOIN manufacturer ON item.mfr_code = manufacturer.mfr_code
    """  # Modify the query as needed

    try:
        with create_secure_connection() as conn:  # Use context manager
            df = pd.read_sql_query(query, conn)
            st.dataframe(df)  # Display the categories in a table
    except Exception as e:
        st.error(f"Error fetching category data: {e}")


# Fetch and display all items with their categories and manufacturers
def display_all_items():
    query = """
        SELECT item.description, category.category, manufacturer.name, item.price
        FROM item
        JOIN category ON item.category_code = category.category_code
        JOIN manufacturer ON item.mfr_code = manufacturer.mfr_code
    """

    try:
        with create_secure_connection() as conn:  # Use context manager
            df = pd.read_sql_query(query, conn)
            return df
    except Exception as e:
        st.error(f"Error fetching all items: {e}")


# Function for adding inventory
def add_inventory():
    st.subheader("Add Inventory")
    st.write("This is where you can add new inventory items.")
    # Add code to handle the addition of inventory items


# Function for modifying inventory
def modify_inventory():
    st.subheader("Modify Inventory")
    st.write("This is where you can modify existing inventory items.")
    # Add code to handle inventory modifications


# Function for deleting inventory
def delete_inventory():
    st.subheader("Delete Inventory")
    st.write("This is where you can delete inventory items.")
    # Add code to handle inventory deletion


# Placeholder function for displaying items by category
def display_item_category(category):
    st.write(f"Displaying items in the category: {category}")
    # Add code to display items in the selected category


# Placeholder function for displaying a specific item
def display_item(item):
    st.write(f"Displaying details for item: {item}")
    # Add code to display specific item details


# Example usage of context manager for testing
if __name__ == "__main__":
    # Test display functions
    st.title("Inventory Management System")

    # Display all items
    df = display_all_items()
    if df is not None:
        st.dataframe(df)














# import sqlite3
# import streamlit as st
# import pandas as pd
# import os
#
# def authenticate_user(username, password):
#     """
#     Authenticates the user by checking the provided username and password.
#     """
#     # Hardcoded credentials (In a real-world scenario, avoid hardcoding)
#     valid_username = "admin"
#     valid_password = "Admin123"
#
#     if username == valid_username and password == valid_password:
#         print("Authentication successful.")
#         return True
#     else:
#         print("Authentication failed. Invalid username or password.")
#         return False
#
# # Create secure connection
#
#
#
# def create_secure_connection():
#     """Create a secure connection to the SQLite database."""
#     try:
#         # Ensure the correct relative path to the database
#         db_path = os.path.join(os.path.dirname(__file__), 'ohs_inventory')
#
#         # Connect to the SQLite database
#         conn = sqlite3.connect(db_path)
#         print("Connected to the database successfully.")
#         return conn
#     except sqlite3.Error as e:
#         st.error(f"Database connection error: {e}")
#         return None
#
# # Displays category items from the 'category' table in the database.
# def display_category_items(conn):
#     try:
#         query = ("SELECT item.description, item.price, item.unit, item.qty_on_hand as QOH, manufacturer.name as manufacturer\
#                  FROM  item\
#                  inner join manufacturer on item.mfr_code = manufacturer.mfr_code" ) # Modify if you want specific columns
#         df = pd.read_sql_query(query, conn)
#         st.dataframe(df)  # Display the categories in a table
#     except Exception as e:
#         st.error(f"Error fetching category data: {e}")
#
# def display_all_items(conn):
#     try:
#         query = """
#             SELECT item.description, category.category, manufacturer.name, item.price
#             FROM item
#             JOIN category ON item.category_code = category.category_code
#             JOIN manufacturer ON item.mfr_code = manufacturer.mfr_code
#             """
#         df = pd.read_sql_query(query, conn)
#         return df
#     except Exception as e:
#         print(f"Error fetching category data: {e}")  # Corrected this line
#
# # if __name__ == "__main__":
# #     # Path to your SQLite database file
# #     database_file = "inventory.db"
# #
# #     # Create a secure connection to the database
# #     conn = create_secure_connection(database_file)
# #
# #     if conn:
# #         # Perform database operations securely here
# #         conn.close()  # Always close the connection when done
#
#
# #
# #  Create functions for each action submenu for updating inventory
# def add_inventory():
#     st.subheader("Add Inventory")
#     st.write("This is where you can add new inventory items.")
#     # Add your code to add items to the inventory
#
# def modify_inventory():
#     st.write("This is where you can modify existing inventory items.")
#     # Add your code to modify inventory items
#     # Function to fetch unique items from the database
#
# def delete_inventory():
#     st.write("This is where you can delete inventory items.")
#     # Add your code to delete items from the inventory
#
# def display_item_category(category):
#    pass
#
# def display_item(item):
#     pass
#
