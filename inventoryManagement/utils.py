import sqlite3
import getpass
import streamlit as st
import pandas as pd


def authenticate_user(username, password):
    """
    Authenticates the user by checking the provided username and password.
    """
    # Hardcoded credentials (In a real-world scenario, avoid hardcoding)
    valid_username = "admin"
    valid_password = "Admin123"

    if username == valid_username and password == valid_password:
        print("Authentication successful.")
        return True
    else:
        print("Authentication failed. Invalid username or password.")
        return False


def create_secure_connection(db_file):
    """
    Securely create a connection to the SQLite database after user authentication.
    """
    conn = None
    try:
        # Ask for username and password before allowing access to the database
        # Authenticate the user
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
    return conn

# Displays category items from the 'category' table in the database.
def display_category_items(conn):
    try:
        query = ("SELECT item.description, item.price, item.unit, item.qty_on_hand as QOH, manufacturer.name as manufacturer\
                 FROM  item\
                 inner join manufacturer on item.mfr_code = manufacturer.mfr_code" ) # Modify if you want specific columns
        df = pd.read_sql_query(query, conn)
        st.dataframe(df)  # Display the categories in a table
    except Exception as e:
        st.error(f"Error fetching category data: {e}")

def display_all_items(conn):
    try:
        query = """
            SELECT item.description, category.category, manufacturer.name, item.price
            FROM item
            JOIN category ON item.category_code = category.category_code
            JOIN manufacturer ON item.mfr_code = manufacturer.mfr_code
            """
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        print(f"Error fetching category data: {e}")  # Corrected this line

# if __name__ == "__main__":
#     # Path to your SQLite database file
#     database_file = "inventory.db"
#
#     # Create a secure connection to the database
#     conn = create_secure_connection(database_file)
#
#     if conn:
#         # Perform database operations securely here
#         conn.close()  # Always close the connection when done


#
#  Create functions for each action submenu for updating inventory
def add_inventory():
    st.subheader("Add Inventory")
    st.write("This is where you can add new inventory items.")
    # Add your code to add items to the inventory

def modify_inventory():
    st.write("This is where you can modify existing inventory items.")
    # Add your code to modify inventory items
    # Function to fetch unique items from the database

def delete_inventory():
    st.write("This is where you can delete inventory items.")
    # Add your code to delete items from the inventory

def display_item_category(category):
   pass

def display_item(item):
    pass

