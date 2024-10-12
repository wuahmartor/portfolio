import streamlit as st
import sqlite3
import pandas as pd
from utils import create_secure_connection

conn = create_secure_connection('ohs_inventory')
# Function to fetch unique items from the database
def fetch_unique_items(conn):
    query = "SELECT DISTINCT description FROM item"
    result = pd.read_sql_query(query, conn)
    result = result.loc[:, ~result.columns.duplicated()]
    return result['description'].tolist()

# Function to fetch details of a selected item
def fetch_item_details(conn, selected_item):
    query = "SELECT price, qty_on_hand FROM item WHERE description = ?"
    result = pd.read_sql_query(query, conn, params=(selected_item,))
    return result

# Function to update item price and quantity in the database
def update_item(conn, selected_item, new_price, new_qty):
    query = "UPDATE item SET price = ?, qty_on_hand = ? WHERE description = ?"
    cur = conn.cursor()
    cur.execute(query, (new_price, new_qty, selected_item))
    conn.commit()
# Establish connection to the database
# Fetch unique items from the database
items = fetch_unique_items(conn)
col1, col2 = st.columns(2)

def add_inventory():
    st.subheader('under construction')

def modify_inventory():
    pass

def delete_inventory():
    st.subheader('Under Construction')

def update_inventory():
    # Submenu for Add, Modify, Delete
    submenu = ["Add", "Modify", "Delete"]
    choice = st.sidebar.selectbox("Choose an action", submenu)

    if choice == "Add":
        add_inventory()

    elif choice == "Modify":
        selected_item = st.sidebar.selectbox('Select Item to Update', items)
        if selected_item:
            # Fetch current price and quantity of the selected item
            item_details = fetch_item_details(conn, selected_item)
            if not item_details.empty:
                # Handle None values for price and qty_on_hand
                current_price = item_details['price'].values[0]
                current_qty = item_details['qty_on_hand'].values[0]

                # # Set defaults if values are None
                if current_price is None:
                   current_price = 0.0
                if current_qty is None:
                   current_qty = 0

                # Display current price and quantity
        st.write(f"Current Price: {current_price}")
        st.write(f"Current Quantity on Hand: {current_qty}")

        # Input fields for new price and quantity

        col1, col2 = st.columns([1,3])
        with col1:
            new_price = st.number_input('New Price', value=float(current_price), step=0.01)
            new_qty = st.number_input('New Quantity on Hand', value=int(current_qty), step=1)
             # Button to update item in the database
            if st.button('Update Item'):
                update_item(conn, selected_item, new_price, new_qty)
                st.success(f"Item '{selected_item}' updated successfully!")
            else:
                st.warning(f"Waiting for update")

    elif choice == "Delete":
        delete_inventory()