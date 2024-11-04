# Hospital Readmission Analysis

## Objective
To analyze and model hospital readmission rates to identify key factors contributing to high readmission and provide actionable insights to
healthcare facilities.

## Summary
Hospital readmission is a critical issue impacting both patient care and healthcare costs. This project explores a dataset on hospital readmissions, 
with features like the number of discharges, predicted and expected readmission rates, and excess readmission ratio.

### Steps
1. **Data Cleaning**: Prepared the data by handling missing values, filtering outliers, and selecting important features.
2. **Exploratory Data Analysis (EDA)**: Analyzed feature distributions, correlations, and trends affecting readmission.
3. **Modeling**: Used a regression model to predict readmission likelihood, with a focus on minimizing error and maximizing interpretability.
4. **Evaluation**: Assessed model performance using metrics like MAE and RMSE (for regression).
5. **Insights & Recommendations**: Summarized key findings, highlighting factors that significantly impact readmission rates, and 
                                                                               suggested potential interventions.

## Key Findings
Certain factors, such as the number of discharges and predicted readmission rate, are strongly correlated with actual readmission.
High excess readmission ratios may indicate areas where patient follow-up or discharge planning improvements could reduce readmissions.

## How to Use This Project
1. **Requirements**: Ensure that you have Python installed, along with required packages (`pandas`, `seaborn`, `matplotlib`, `scikit-learn`).
2. **Running the Notebook**: Open `hospitalReadmission.ipynb` in Jupyter Notebook or JupyterLab and execute cells step-by-step.
3. **Modifying the Analysis**: Adjust feature selection, model parameters, or add new metrics to tailor the analysis further.

## Conclusion
This project provides a data-driven approach to understanding hospital readmission, offering insights that healthcare providers can leverage
to enhance patient care and reduce costs associated with readmission.
