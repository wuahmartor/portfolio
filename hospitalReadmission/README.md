# Hospital Readmission Analysis

## Objective
To analyze and model hospital readmission rates to identify key factors contributing to high readmission and provide actionable insights to
healthcare facilities.

Excess hospital readmissions present a significant challenge for healthcare providers, affecting both patient outcomes and financial performance. This project aims to develop a predictive model that identifies hospitals at risk of high readmission rates, enabling targeted interventions to improve care quality, optimize resource allocation, and reduce costs associated with readmissions. By addressing this issue, hospitals can not only enhance patient satisfaction but also avoid penalties under the Hospital Readmissions Reduction Program (HRRP)
Background/History

Hospital readmission rates have long been a critical indicator of care quality. Under the HRRP, hospitals with higher-than-expected readmissions face financial penalties, making it essential for them to improve care coordination and discharge planning. This initiative aligns with broader efforts to improve healthcare quality and reduce costs under the Affordable Care Act. Historical data on hospital readmissions is leveraged in this project to analyze key factors influencing readmission rates and to develop actionable strategies for improvement.


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
