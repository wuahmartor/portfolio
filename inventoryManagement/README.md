Welcome to the Streamlit Inventory Management System

This project is a comprehensive Inventory Management System built using Python and Streamlit. 
It offers both SQL-based search functionality and model-based item recommendations to assist with efficient inventory management.
The system uses a content-based recommendation algorithm to suggest items similar to the one selected by the user, 
leveraging TF-IDF vectorization and cosine similarity. The system uses basic authentication for access. 
basic user with readonly rights 
username: viewer 
password: viewer123


Table of Contents

	•	Overview
	•	Features
	•	Technologies Used
	•	Dataset
	•	How the Model Works
	•	Installation
	•	How to Run
	•	How to Use

Overview

This system provides a dual approach to inventory management. Users can search for items directly from the 
SQL database or use a model-based recommendation system to find items that are similar to their selection.
The model calculates similarity based on the description, category, and manufacturer using the TF-IDF vectorizer.

Features

	•	Inventory Search (SQL-based): Users can search for items or categories using a SQL query-based dropdown.
	•	Model-Based Recommendations: Users can select an item, and the system will recommend three similar items based on cosine similarity.
	•	Interactive Interface: The system is built using Streamlit, providing a user-friendly interface.
	•	Dual Functionality: Users can switch between SQL-based search and model-based recommendations from the sidebar.

Technologies Used

	•	Python: For backend logic and data handling.
	•	Streamlit: For creating the web-based user interface.
	•	Pandas: For data manipulation and preprocessing.
	•	SQLite: For managing the inventory database.
	•	Scikit-learn: For building the TF-IDF vectorizer and calculating cosine similarity.

Dataset

The inventory dataset contains item descriptions, categories, prices, manufacturers, and quantities. 
The dataset has missing components that are required to improve the model and achieve project goals. 
For example, to estimate or determine if item needs reorder, the reorder level and quantity on hand should be establisged. 
These are information still being collected from stakeholders.
The data is stored in an SQLite database, which is queried directly for SQL-based searches or used to build the model for recommendations.

How the Model Works

The model-based recommendation system uses the following steps to suggest items:

	1.	Load Data: The system fetches item data (description, category, and name) from the SQLite database.
	2.	Preprocess Data: It combines these features into a single string for each item.
	3.	TF-IDF Vectorization: The system converts the combined features into a vectorized form using TF-IDF.
	4.	Cosine Similarity Calculation: The system compares the selected item with others based on cosine similarity.
	5.	Top 3 Recommendations: The system suggests the top 3 most similar items to the selected one.

Installation

Prerequisites

Make sure you have Python installed on your system. If not, you can download it from here.

Step-by-Step Setup

	1.	Clone this repository or download the code.
	2.	Install the required Python libraries by running the following command in your terminal:
 bash:
 pip install streamlit pandas scikit-learn sqlite3
  3.	Make sure your SQLite database (ohs_inventory) is properly configured.

How to Run

After completing the installation, follow these steps to run the project:

	1.	Open a terminal or command prompt.
	2.	Navigate to the folder where your Python script is saved.
	3.	Run the Streamlit app using the following command:
 streamlit run inventory_management.py
 4.	The app will automatically open in your web browser. If it doesn’t, open your browser and go to:
http://localhost:8501

How to Use

	1.	Navigate to the App: Open the app in your browser.
	2.	Select Functionality: Choose between SQL-Based Search and Model-Based Recommendations from the sidebar.
	3.	SQL-Based Search:
	   •	Select either Category or Item from the dropdown.
	   •	Click Search to retrieve results from the database.
	4.	Model-Based Recommendations:
	   •	Select an item from the dropdown.
	   •	The system will display the top 3 recommended items based on similarity.
