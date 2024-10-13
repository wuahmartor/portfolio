import sqlite3
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Set the page configuration
st.set_page_config(page_title="OHS Inventory Management", layout="wide")
from update_inventory import *
from view_inventory import *
from use_model import *
from create_order import *
# Import page functions from the pages directory
from utils import *

# Users for authentication (for demonstration purposes)
users = {
    "admin": {"password": "Admin@123", "role": "admin"},
    "viewer": {"password": "viewer123", "role": "viewer"}
}


# Function to authenticate users
def authenticate_user(username, password):
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    return None


# Dynamic sidebar for each menu based on the user role
def render_sidebar(menu_choice, role):
    if menu_choice == "View Inventory":
        st.sidebar.header("View Inventory Options")
        # Add more sidebar elements for this menu item

    elif menu_choice == "Update Inventory" and role == "admin":
        st.sidebar.header("Update Inventory Options")
        # Add more sidebar elements for this menu item
    elif menu_choice == "Use Model":
        st.sidebar.header("Model recommendation")
        # Add more sidebar elements for this menu item
    elif menu_choice == "Create Order":
        st.sidebar.header("Create Order Options")
        # Add more sidebar elements for this menu item


# Initialize session state variables
def initialize_session_state():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = None
    if "role" not in st.session_state:
        st.session_state["role"] = None


# Streamlit App to create a login page
def main():
    # Initialize session state variables if not present
    initialize_session_state()

    # Check if the user is already logged in using session state
    query_params = st.query_params

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = query_params.get("logged_in", ["false"])[0] == "true"

    # If not logged in, show login form in sidebar only
    if not st.session_state["logged_in"]:
        # Show login form in the sidebar
        with st.sidebar:
            st.write("[want login info: visit read 'readme.rm' ](https://github.com/wuahmartor/portfolio/blob/main/inventoryManagement/main_page.py)")
            st.subheader("Please login to access the system")

            # User input fields
            username = st.text_input("Username").strip()
            password = st.text_input("Password", type="password").strip()

            # Button to submit login
            if st.button("Login"):
                # Authenticate the user
                role = authenticate_user(username, password)
                if role:
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.session_state["role"] = role
                    st.success(f"Welcome {username}! You have successfully logged in as {role}.")
                    # Set query params to reflect logged-in state
                    st.set_query_params(logged_in="true")
                else:
                    st.error("Invalid username or password. Please try again.")
    else:
        # If logged in, show navigation and dynamic sidebar based on page selection
        with st.sidebar:
            st.sidebar.success(f"Logged in as: {st.session_state['username']} ({st.session_state['role']})")
            if st.button("Logout"):
                # Clear the session state and reset the query parameters
                for key in st.session_state.keys():
                    del st.session_state[key]
                st.set_query_params(logged_in="false")
                # Trigger a page refresh by clearing the query params
                st.set_query_params()  # Clears all query parameters to reset the state

        # Horizontal navigation menu (displayed in the main content area)
        choice = option_menu(
            menu_title=None,
            options=["View Inventory", "Update Inventory", "Use Model", "Create Order"],
            icons=["eye", "pencil", "box-arrow-down", "cart"],  # Add icons
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )

        # Render the sidebar based on the current page choice and user role
        render_sidebar(choice, st.session_state["role"])

        # Link each menu item to the respective page
        if choice == "View Inventory":
            view_inventory()
        elif choice == "Update Inventory":
            # Only allow "admin" users to update the inventory
            if st.session_state["role"] == "admin":
                st.write('Use left sidebar to select option')
                update_inventory()
            else:
                st.warning("You do not have permission to update the inventory.")
        elif choice == "Use Model":
            model_based_recommendations()
        elif choice == "Create Order":
            create_order()

# Run the app
if __name__ == '__main__':
    main()