import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Load all the datasets
dataset_path = 'dataset.csv'
disease_description_path = 'symptom_Description.csv'
symptom_precaution_path = 'symptom_precaution.csv'
symptom_severity_path = 'Symptom-severity.csv'

# Read the datasets
dataset = pd.read_csv(dataset_path)
disease_description = pd.read_csv(disease_description_path)
symptom_precaution = pd.read_csv(symptom_precaution_path)
symptom_severity = pd.read_csv(symptom_severity_path)

# Display the first few rows of each dataset and their info
datasets_info = {
    "Main Dataset": dataset.head(),
    "Disease Description": disease_description.head(),
    "Symptom Precaution": symptom_precaution.head(),
    "Symptom Severity": symptom_severity.head()
}

# # impute missing values
# # Display the info of the main dataset to check for missing values and datatypes
# dataset.info(), dataset.describe(include='all')
#
# # model development
#
# # Fill missing values with 'None'
dataset_filled = dataset.fillna('None')
#
# # Initialize label encoder
label_encoder = LabelEncoder()
#
# # Encode the Disease column
dataset_filled['Disease'] = label_encoder.fit_transform(dataset_filled['Disease'])
# Fill missing values with 'None'
print(f"dataset filled with label encoder {dataset_filled['Disease']}")

# Gather all symptom columns
symptom_columns = [col for col in dataset_filled.columns if 'Symptom' in col]

# Extract unique symptom names from all symptom columns in the dataset
unique_symptoms = set()
for col in symptom_columns:
    unique_symptoms.update(dataset[col].dropna().unique())

# Convert set to list and sort (excluding 'nan' if any)
unique_symptoms = sorted(list(unique_symptoms))
# Initialize a DataFrame to hold the binary features
symptom_features = pd.DataFrame(0, index=dataset.index, columns=unique_symptoms)

# Populate the binary features DataFrame: 1 if symptom is present, 0 otherwise
for index, row in dataset.iterrows():
    for col in symptom_columns:
        symptom = row[col]
        if pd.notna(symptom) and symptom in symptom_features.columns:
            symptom_features.at[index, symptom] = 1

# Combine the symptom features with the disease labels
transformed_data = pd.concat([dataset['Disease'], symptom_features], axis=1)
transformed_data.columns = transformed_data.columns.str.replace('_', ' ')
# Display the transformed data
print(transformed_data.head())

# Encode the 'Disease' column
label_encoder = LabelEncoder()
transformed_data['Disease'] = label_encoder.fit_transform(transformed_data['Disease'])

# Define features and target
X = transformed_data.drop('Disease', axis=1)
X.columns = X.columns.str.strip().str.replace('_', ' ')
y = transformed_data['Disease']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree Classifier
dt_classifier = DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train, y_train)

# save model
from joblib import dump
from joblib import load

# Saving the model and label encoder
dump(dt_classifier, 'disease_model.joblib')
dump(label_encoder, 'label_encoder.joblib')

# Predict on the test set
# Loading the model and label encoder
loaded_disease_model = load('disease_model.joblib')
label_encoder = load('label_encoder.joblib')

y_pred = loaded_disease_model.predict(X_test)

# Calculate accuracy and classification report
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(accuracy, report)

# proof od model efficiency using cross validation
# Perform 10-fold cross-validation
cv_scores = cross_val_score(loaded_disease_model, X, y, cv=10, scoring='accuracy')

# mean and standard deviation of the cross-validation scores
cv_mean = cv_scores.mean()
cv_std = cv_scores.std()

print(f'CV mean {cv_mean}, CV standard deviation: {cv_std}, CV Scores: {cv_scores}')

# Streamlit interface
print(f'symptoms list {X.columns}')
symptoms_list = list(X.columns)  # replace with actual symptoms

# Prepare lookup dictionaries
description_dict = pd.Series(disease_description.Description.values, index=disease_description.Disease).to_dict()
precaution_dict = symptom_precaution.set_index('Disease').T.to_dict('list')

print(description_dict)

import streamlit as st
import numpy as np

# Title and user input setup
st.title('Disease Prediction System')
st.markdown(
    '#### Check your current symptoms. The Prediction may not be accurate or conclusive. Always check with your '
    'healthcare provider:')

# Initialize session state to store selected symptoms and a clear flag
if 'selected_symptoms' not in st.session_state:
    st.session_state.selected_symptoms = []

if 'clear_selection' not in st.session_state:
    st.session_state.clear_selection = False  # To track if the clear button is pressed

# Set up the grid layout for the symptoms
num_columns = 6  # Define the number of columns
columns = st.columns(num_columns)

# Display symptoms in a grid layout with multiple columns
for i, symptom in enumerate(symptoms_list):
    col_idx = i % num_columns

    # If clear_selection is True, reset the checkboxes to unchecked state
    if st.session_state.clear_selection:
        checkbox_value = False
    else:
        checkbox_value = symptom in st.session_state.selected_symptoms

    # Checkbox with state management
    if columns[col_idx].checkbox(symptom, value=checkbox_value):
        if symptom not in st.session_state.selected_symptoms:
            st.session_state.selected_symptoms.append(symptom)
    else:
        if symptom in st.session_state.selected_symptoms:
            st.session_state.selected_symptoms.remove(symptom)

# Prediction button placed outside the container
if st.button('Predict Disease'):
    # Ensure at least two symptoms are selected
    if len(st.session_state.selected_symptoms) < 2:
        st.warning("Please select at least two symptoms before predicting the disease.")
    else:
        # Create input array for model prediction, initializing with zeros
        input_features = np.zeros(len(symptoms_list))
        for symptom in st.session_state.selected_symptoms:
            input_features[symptoms_list.index(symptom)] = 1  # set 1 for selected symptoms

        # Predicting the disease
        disease_index = loaded_disease_model.predict([input_features])[0]
        disease = label_encoder.inverse_transform([disease_index])[0]

        # Displaying the result
        st.success(f'Predicted Disease: {disease}')
        st.write(f'Description: {description_dict[disease]}')

        precautions = precaution_dict[disease]
        st.write('Precautions:')
        for precaution in precautions:
            st.write(f'- {precaution}')

    # Reset the clear selection flag after prediction
    st.session_state.clear_selection = False

# Clear selection button
if st.button('Clear Selection'):
    # Clear the selected symptoms in session state
    st.session_state.selected_symptoms = []
    st.session_state.clear_selection = True  # Set the flag to True to reset checkboxes
    st.experimental_rerun()  # Rerun the app to refresh the UI and clear checkboxes
st.write(
    'Disclaimer: The system aids in diagnosis and recommendations but does not replace professional medical advice.\n'
    'Use the system alongside clinical judgment and local guidelines and consult qualified healthcare providers for '
    'medical concerns.')
