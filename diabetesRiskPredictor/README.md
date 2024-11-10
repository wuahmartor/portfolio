# Diabetes Predictor created by Reuben Martor 

## Overview
This project develops a machine learning model to predict diabetes outcomes using patient-level data. The pipeline includes data preprocessing, exploratory data analysis (EDA), model training, and evaluation, with insights drawn from confusion matrices and AUC scores to assess model performance.

## Features
- **Data Preprocessing**: Addressing missing values and normalizing features.
- **Exploratory Data Analysis (EDA)**: Visualizing feature relationships and identifying key predictors.
- **Machine Learning Models**: Logistic Regression, Decision Trees, and SVM for diabetes prediction.
- **Evaluation Metrics**:
  - Confusion Matrix: Analyzing true positives, true negatives, false positives, and false negatives.
  - AUC-ROC: Measuring the model’s ability to separate diabetic and non-diabetic cases.

## Key Results
- **Confusion Matrix**:
  - High true positive (TP) and true negative (TN) rates indicate strong predictive power.
  - Minimal false positives (FP) and false negatives (FN) reflect robust classification.
- **AUC-ROC**:
  - Achieved an AUC score of 0.87, indicating high model performance in distinguishing between classes.
- **Accuracy**: Consistently high across multiple evaluation runs, demonstrating reliability.

## How to Use
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt




Findings 

### Analysis and Conclusions
The project involves predicting diabetes outcomes using a structured machine learning pipeline. The dataset includes patient-level features such as glucose levels, blood pressure, BMI, and age, which are critical indicators for diabetes diagnosis.

Data Explanation

	•	Key Features:
	•	Glucose: Plasma glucose concentration (mg/dL).
	•	Blood Pressure: Diastolic blood pressure (mm Hg).
	•	BMI: Body mass index, calculated as weight in kg/(height in m)^2.
	•	Age: Patient’s age (years).
	•	Pregnancies: Number of pregnancies for female patients.
	•	Diabetes Pedigree Function (DPF): Indicates genetic influence on diabetes.
	•	Target Variable: Binary label indicating the presence (1) or absence (0) of diabetes.

The data underwent preprocessing steps, including handling missing values and feature scaling to normalize the range of variables.

Exploratory Data Analysis (EDA)

	•	Insights:
	•	Patients with diabetes tend to have higher glucose levels and BMI.
	•	Age and DPF show moderate correlations with diabetes prevalence.
	•	Features such as pregnancies and blood pressure have weaker correlations but still contribute to predictions.
	•	Outliers:
	•	Identified and analyzed to ensure they do not significantly skew the model’s performance.

Model Training and Evaluation

	•	Algorithms Used:
	•	Logistic Regression.
	•	Decision Trees.
	•	Support Vector Machines (SVM).
	•	Evaluation Metrics:
	•	Accuracy: Proportion of correctly predicted cases among all cases.
	•	Precision: Proportion of true positive predictions among all positive predictions.
	•	Recall: Proportion of true positives identified among all actual positives.
	•	F1-Score: Harmonic mean of precision and recall.
	•	Confusion Matrix:
	•	Provides a breakdown of predictions:
	•	True Positives (TP): Correctly predicted diabetic cases.
	•	True Negatives (TN): Correctly predicted non-diabetic cases.
	•	False Positives (FP): Non-diabetic cases predicted as diabetic.
	•	False Negatives (FN): Diabetic cases predicted as non-diabetic.

    •    Metrics:
Predicted
            Positive  Negative
Actual
Positive       TP        FN
Negative       FP        TN

High TP and TN with minimal FP and FN indicate good model performance.

	•	AUC-ROC (Area Under the Curve - Receiver Operating Characteristic):
	•	AUC represents the model’s ability to distinguish between classes.
	•	AUC values range from 0 to 1:
	•	1: Perfect classification.
	•	0.5: No better than random guessing.
	•	Example:
	•	The model achieved an AUC of 0.87, indicating high separability and robustness in distinguishing diabetic from non-diabetic cases.