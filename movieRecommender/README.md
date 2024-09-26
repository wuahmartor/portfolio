
# Welcome to Reuben's Movie Recommender System


This project is a Movie Recommender System built using Python and Streamlit. The system uses a content-based recommendation algorithm to suggest movies similar to the one selected by the user. It leverages the cosine similarity technique based on the genres, directors, and actors of the movies.

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

This app recommends movies based on the similarity of the selected movie to other movies in the dataset. The similarity is calculated based on features like the movie’s genre, director, and actors. It uses cosine similarity to suggest movies that are most similar to the user’s selection.

Features

	•	Movie Selection: Users can select a movie from a dropdown list after inputing atleast 4 characters of movie title they would like search.
	•	Recommendations: The user selects a move from the dropdown list to search for recommmended movies based on selection. 
   After selecting a movie, the system provides a list of 5 recommended movies based on similarity.
	•	Interactive Interface: The app is powered by Streamlit, providing an easy-to-use and interactive web interface.

Technologies Used

	•	Python: For backend logic and data handling.
	•	Streamlit: For creating the interactive web interface.
	•	Pandas: For data manipulation and preprocessing.
	•	Scikit-learn: For calculating the cosine similarity.
	•	CountVectorizer: For converting text data (genres, directors, actors) into numerical features.

Dataset

The dataset used is a movie dataset that contains information such as the Title, Genre, Director, and Actors of movies. The dataset is sourced from the f GitHub repository loaded directly from the URL in the code.

How the Model Works

The system works by analyzing the genres, directors, and actors of each movie. These features are combined into a single string, which is then converted into numerical data using CountVectorizer. The system then uses cosine similarity to compare movies based on these features.

Process:

	1.	Load Dataset: The dataset is loaded from a CSV file hosted online.
	2.	Preprocess Data: Genres, directors, and actors are combined into a single feature for each movie.
	3.	Cosine Similarity: The system calculates how similar the selected movie is to all other movies using cosine similarity.
	4.	Recommendations: The top 5 most similar movies are returned to the user.

Installation

To run this project on your local machine, follow these steps:

Prerequisites

Make sure you have Python installed on your system. You can download Python from here.

Step-by-Step Setup

	1.	Clone this repository or download the code.
	2.	Install the required Python libraries by running the following command in your terminal:
bash
pip install streamlit pandas scikit-learn

3.	Save the script as movie_recommender.py or any filename you prefer.

How to Run

After completing the installation, follow these steps to run the project:

	1.	Open a terminal or command prompt.
	2.	Navigate to the folder where the Python script is saved.
	3.	Run the Streamlit app using the following command:
 bash
 streamlit run movie_recommender.py

 4.	The app will automatically open in your web browser. If it doesn’t, open your browser and go to http://localhost:8501.

How to Use

	1.	Select a Movie: Use the dropdown to select a movie from the list of available titles.
	2.	Get Recommendations: After selecting a movie, click the Recommend button to receive a list of similar movies.
	3.	Explore: The app will display a list of 10 recommended movies that you can explore further.

License

This project is open-source and available under the MIT License.



Reuben's Skills 
## 🛠 Skills
Python, R, SQL, Machine Learning, PowerBI, Tableau, MS Office, Jupyter Notebook, Basic HTML Streamlit, Computer network, Hardware, Windows Server Active Directory concepts (Microsoft Certifed System Engineer on Windows Server 2003), Nursing Skills, Medical Case Management

# Projects Undertaken:

[Movie Recommender System](https://github.com/wuahmartor/portfolio/blob/main/movieRecommender/movieRecommender.py)


## Health Condition Prediction Model 
[Health Condition Predictor Model](https://github.com/wuahmartor/portfolio/blob/main/diseasePredictionSystem/disease_prediction.ipynb): Machine learning model predicts a health condition based on patient's symptoms and recommend first-aid precautions
[Try Web Interface]( http://192.168.12.76:8501)




## Weather Information Reporting System- US 
[Weather Information Reporting System](https://github.com/wuahmartor/portfolio/blob/main/weatherReportSystem/weatherReportSystem.py):
The system retrieves weather information for Cities in the US. The user may choose to look up weather report by inputing City Name or Zip Code



## Food Quality Dectection System Model At a Meat packing Plant


[Meat Quality Checker](
https://github.com/wuahmartor/portfolio/blob/main/foodQualityDetectionSystem/foodQualityDectection.ipynb): Based on Meat indicated production factors, the model predicts the quality status of the meat as either being good or bad. 


## Cardiac Event Risk Determination in Patient with Heart Failure 
Project Overview:

This project aims to develop a predictive model using machine learning techniques to assess the risk of cardiac events in patients diagnosed with heart failure. By analyzing clinical data, including age, anemia status, enzyme levels, ejection fraction, blood pressure, and other vital health metrics, the model seeks to identify key predictors of cardiac events. The goal is to provide healthcare professionals with a tool to understand the risk factors better and to aid in early intervention and personalized treatment plans for at-risk patients. The outcome of this project has the potential to improve patient care, reduce mortality rates, and optimize healthcare resources by focusing attention on individuals with a higher likelihood of adverse events.

[Cardiac Event Dectection Model](https://github.com/wuahmartor/portfolio/blob/main/heartFailurePredictionModel/heartFailurePrediction.ipynb): Model uses certain health parameters to predict patient's chance of developing a cardiac even given the patient has a heart failure. 

