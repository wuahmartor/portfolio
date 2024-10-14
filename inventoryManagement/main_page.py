import sqlite3
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# Import functions from modules
from update_inventory import update_inventory
from view_inventory import view_inventory
from use_model import model_based_recommendations
from create_order import create_order
from utils import create_secure_connection

# Set page configuration
# st.set_page_config(page_title="OHS Inventory Management", layout="wide")

# Users for authentication (for demonstration purposes)
users = {
    "admin": {"password": "Admin@123", "role": "admin"},
    "viewer": {"password": "viewer123", "role": "viewer"}
}

# Authenticate users
def authenticate_user(username, password):
    """Authenticate the user based on username and password."""
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    return None

# Dynamic sidebar rendering based on the selected menu and user role
def render_sidebar(menu_choice, role):
    if menu_choice == "View Inventory":
        st.sidebar.header("View Inventory Options")
    elif menu_choice == "Update Inventory" and role == "admin":
        st.sidebar.header("Update Inventory Options")
    elif menu_choice == "Use Model":
        st.sidebar.header("Model Recommendations")
    elif menu_choice == "Create Order":
        st.sidebar.header("Create Order Options")

# Initialize session state variables
def initialize_session_state():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = None
    if "role" not in st.session_state:
        st.session_state["role"] = None

# Main function to run the Streamlit app
def main():
    # Initialize session state variables
    initialize_session_state()

    # Check for query parameters to maintain login state
    query_params = st.experimental_get_query_params()

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = query_params.get("logged_in", ["false"])[0] == "true"

    if not st.session_state["logged_in"]:
        # Login form in sidebar if not logged in
        with st.sidebar:
            st.write("[Visit README for login info](https://github.com/wuahmartor/portfolio/blob/main/inventoryManagement/README.md)")
            st.subheader("Please login to access the system")

            # Username and password input
            username = st.text_input("Username").strip()
            password = st.text_input("Password", type="password").strip()

            # Login button
            if st.button("Login"):
                role = authenticate_user(username, password)
                if role:
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.session_state["role"] = role
                    st.success(f"Welcome {username}! Logged in as {role}.")
                    st.experimental_set_query_params(logged_in="true")
                else:
                    st.error("Invalid username or password. Please try again.")
    else:
        # Show logout option and sidebar details for logged-in users
        with st.sidebar:
            st.sidebar.success(f"Logged in as: {st.session_state['username']} ({st.session_state['role']})")
            if st.button("Logout"):
                # Clear session state and query parameters
                for key in st.session_state.keys():
                    del st.session_state[key]
                st.experimental_set_query_params(logged_in="false")

        # Horizontal navigation menu
        choice = option_menu(
            menu_title=None,
            options=["View Inventory", "Update Inventory", "Use Model", "Create Order"],
            icons=["eye", "pencil", "box-arrow-down", "cart"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )

        # Render sidebar options based on the selected menu and user role
        render_sidebar(choice, st.session_state["role"])

        # Display the selected page
        if choice == "View Inventory":
            view_inventory()
        elif choice == "Update Inventory":
            if st.session_state["role"] == "admin":
                st.write('Use the sidebar to update inventory.')
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


