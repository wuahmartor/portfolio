## Loan Approval Prediction

This project leverages data from a loan approval dataset to build a predictive model that can classify loan applications as either approved or rejected. By following this approach, we explore different machine learning models and hyperparameter tuning to achieve optimal performance

#### Project Overview

##### Goal: To build a predictive model for loan approval using key features of applicants, such as income, education, credit history, and more.

Dataset: The loan dataset contains 614 entries with 13 features including gender, marital status, number of dependents, education level, employment status, applicant income, co-applicant income, loan amount, loan term, credit history, and loan status (target variable).

###### Project Steps

1.	Data Preprocessing: Load data, clean, and encode categorical features.
2.	Modeling: Use a pipeline with MinMaxScaler and KNN, followed by Logistic Regression and Random Forest.
3.	Hyperparameter Tuning: Tune parameters for optimal model selection.
4.	Evaluation: Evaluate models and choose the best based on accuracy.
5.	License :this project is open-source under the MIT License.

## Installation and Requirements

To run this project, you will need:
- Python 3.7+
- 1.	Run the code cells in sequence in a Python environment (Jupyter Notebook or similar).
	2.	Review the output to understand model performance.
- `pandas`, `numpy`, `scikit-learn`

Install the necessary libraries using:
```bash
pip install pandas numpy scikit-learn

###### 1. Data Preparation:
	Load the dataset.
	Drop the Loan_ID column as it is non-informative for prediction.
	Remove any rows with missing values to ensure data quality.
	Convert categorical variables to numerical using dummy variables.
###### 2. Feature and Target Variables:
	Set the feature matrix X by excluding the Loan_Status column.
	Define the target variable y as Loan_Status.
###### 3. Data Splitting:
	Split the data into training and testing sets with an 80-20 ratio.
###### 4. Model Pipeline:
    Create a pipeline with a MinMaxScaler for feature scaling and a classifier.         Initially, use K-Nearest Neighbors (KNN) as the classifier.
###### 5. Model Training:
	Train a default KNN classifier using the pipeline and evaluate accuracy on the     test set.
###### 6. Hyperparameter Tuning:
	Define a search space for the KNN classifier, varying n_neighbors from 1 to 10.
	Use GridSearchCV with 5-fold cross-validation to find the optimal n_neighbors     value.
###### 7. Expanded Model Search:
	Expand the search space to include other models like Logistic Regression and     Random Forest.
	Run another grid search to identify the best-performing model and its optimal hyperparameters.
###### 8. Result Analysis:
    Compare model performances and analyze the impact of hyperparameter tuning on accuracy.

##### Results Summary
The final model demonstrated improved accuracy by using Random Forest with optimized hyperparameters.
Through iterative modeling and tuning, I identified the best-performing model and optimized its parameters, achieving improved accuracy compared to the initial models. This project demonstrates the importance of model selection and hyperparameter tuning in predictive performance.

