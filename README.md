# Predictive Analytics for Telco Customer Churn

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/144GQEmf4GCDoauPvRseTRNFpF9kYDZOB?usp=sharing)

---

## 1. Project Overview

This project presents a comprehensive analysis of customer churn for a telecommunications company. The primary goal is to identify the key factors driving customer churn and to develop a predictive model that can identify at-risk customers. By leveraging machine learning, the project aims to provide actionable insights that can help the company develop targeted retention strategies, reduce customer attrition, and improve overall profitability.

---

## 2. Business Problem

Customer churn is a critical issue in the highly competitive telecommunications industry. Acquiring new customers is significantly more expensive than retaining existing ones, making churn reduction a top priority. This project addresses the need for a data-driven approach to understand *why* customers leave and *who* is most likely to leave, enabling the business to shift from a reactive to a proactive retention model.

---

## 3. Dataset

The analysis is based on the **Telco Customer Churn** dataset, publicly available on Kaggle. The dataset contains 7,043 customer records with 21 attributes, including:

*   **Customer Demographics:** Gender, Senior Citizen status, Partner, and Dependents.
*   **Services Subscribed:** Phone Service, Multiple Lines, Internet Service, Online Security, Online Backup, Device Protection, Tech Support, and Streaming services.
*   **Account Information:** Tenure, Contract type, Payment Method, Paperless Billing, Monthly Charges, and Total Charges.

> **Source:** [Kaggle: Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### Data Exploration

The initial exploration of the dataset revealed important patterns:

![Distribution of Customer Churn](images/churn_distribution.png)

*Distribution of Customer Churn - showing class imbalance between churned and retained customers*

![Distribution of Tenure](images/tenure_distribution.png)

*Distribution of Tenure - revealing a U-shaped distribution with peaks at low and high tenure values*

---

## 4. Methodology

The project followed a structured data analysis workflow:

1.  **Exploratory Data Analysis (EDA):** The dataset was analyzed to uncover patterns, identify anomalies, and understand the relationships between different variables and churn. This included visualizing distributions and correlations.

2.  **Data Preprocessing & Feature Engineering:** The data was cleaned and prepared for modeling. This involved handling missing values, encoding categorical variables (One-Hot and Label Encoding), and scaling numerical features to prevent bias in the models.

3.  **Model Development:** Three different machine learning models were trained and evaluated:
    *   **Logistic Regression (with Lasso):** Chosen for its high interpretability and ability to serve as a strong baseline.
    *   **XGBoost Classifier:** A powerful gradient boosting model chosen for its high predictive accuracy.
    *   **Random Forest Classifier:** An ensemble model chosen for its robustness and ability to rank feature importance.

4.  **Model Evaluation:** Models were evaluated using a variety of metrics, including Accuracy, **Recall**, and **ROC AUC**. Recall was prioritized as the key metric to ensure the model effectively identifies the maximum number of actual churners.

### Analysis Visualizations

![Correlation Matrix](images/correlation_matrix.png)

*Correlation Matrix showing relationships between features and churn probability*

![Feature Importance](images/feature_importance.png)

*Top 15 Feature Importances for Churn Prediction (Random Forest) - Contract_Month-to-month is the most important predictor*

![Monthly Charges by Churn Status](images/monthly_charges_by_churn.png)

*Monthly Charges by Churn Status - Churned customers tend to have higher monthly charges*

![Churn Rate by Contract Type](images/churn_by_contract.png)

*Churn Rate by Contract Type - Month-to-month contracts show significantly higher churn rates*

![Tenure vs Monthly Charges](images/turnure_vs_monthly_charges.png)

*Tenure vs. Monthly Charges Analysis - Relationship between tenure, charges, and churn patterns*

---

## 5. Key Findings

The analysis revealed several key drivers of customer churn:

*   **Contract Type is Critical:** Customers on **month-to-month contracts** are significantly more likely to churn than those on one-year or two-year contracts.
*   **Lack of Support Drives Churn:** The absence of services like **Tech Support**, **Online Security**, and **Online Backup** is strongly correlated with a higher churn rate.
*   **Tenure Matters:** New customers with low tenure are more likely to leave, while long-term customers are more loyal.
*   **Payment Method Impact:** Customers using **Electronic check** as a payment method show a higher propensity to churn.

Based on the evaluation, the **Tuned Logistic Regression model** was selected as the final model due to its superior **Recall score of 79.41%**, aligning best with the business goal of identifying the most at-risk customers.

### Model Performance

![ROC Curve - Random Forest](images/roc_randomforest.png)

*ROC Curve - Tuned Random Forest Classifier (AUC = 0.82)*

![ROC Curve - XGBoost](images/roc_xgboost.png)

*ROC Curve - Tuned XGBoost Classifier (AUC = 0.82)*

![ROC Curve - Logistic Regression](images/roc_logistic.png)

*ROC Curve - Tuned Logistic/Lasso Regression (AUC = 0.82)*

![Confusion Matrix - Random Forest](images/confusion_matrix_randomforest.png)

*Confusion Matrix - Tuned Random Forest Classifier*

![Confusion Matrix - XGBoost](images/confusion_matrix_xgboost.png)

*Confusion Matrix - Tuned XGBoost Classifier*

![Confusion Matrix - Logistic Regression](images/confusion_matrix_logistic.png)

*Confusion Matrix - Tuned Logistic/Lasso Regression*

---

## 6. Business Recommendations

Based on the findings, the following actionable recommendations are proposed:

1.  **Incentivize Long-Term Contracts:** Develop targeted campaigns to encourage month-to-month customers to switch to annual or two-year contracts.
2.  **Promote Value-Added Services:** Increase the adoption of Tech Support, Online Security, and Online Backup by bundling them or offering promotional trials.
3.  **Focus on Early-Stage Customers:** Implement a proactive onboarding program for new customers to address their needs and improve their initial experience.
4.  **Review Payment Processes:** Investigate why customers using electronic checks are more likely to churn and encourage the use of more stable, automated payment methods.

---

## 7. Tools and Libraries

This project was implemented in Python 3 and relied on the following key libraries:

*   **Data Manipulation:** `pandas`, `numpy`
*   **Data Visualization:** `matplotlib`, `seaborn`
*   **Machine Learning:** `scikit-learn`, `xgboost`
*   **Dataset Access:** `opendatasets`

---

## 8. How to Run This Project

### Option 1: Interactive Streamlit App

A beautiful, interactive Streamlit application is available to explore the project:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app features:
- **Horizontal Navigation:** Easy access to all project sections
- **Data Exploration:** Interactive visualizations and distributions
- **Analysis:** Correlation matrices and feature importance
- **Results:** Model performance metrics and confusion matrices
- **Insights:** Key findings and business recommendations

### Option 2: Jupyter Notebook (Google Colab)

To explore the analysis and run the code yourself, you can use the provided Jupyter Notebook.

1.  **Open in Google Colab:**
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/144GQEmf4GCDoauPvRseTRNFpF9kYDZOB?usp=sharing)

2.  **Run the Cells:** Execute the cells sequentially to load the data, perform the analysis, and train the models. You will be prompted to enter your Kaggle API credentials to download the dataset.

---

## 9. Project Structure

```
Telco-Customer-Churn-Analysis/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── images/                     # Visualization images
│   ├── churn_distribution.png
│   ├── tenure_distribution.png
│   ├── correlation_matrix.png
│   ├── feature_importance.png
│   ├── monthly_charges_by_churn.png
│   ├── churn_by_contract.png
│   ├── turnure_vs_monthly_charges.png
│   ├── roc_randomforest.png
│   ├── roc_xgboost.png
│   ├── roc_logistic.png
│   ├── confusion_matrix_randomforest.png
│   ├── confusion_matrix_xgboost.png
│   └── confusion_matrix_logistic.png
└── *.py                        # Helper scripts
```

---

## 10. Acknowledgments

*   **Dataset:** The Telco Customer Churn dataset was provided by IBM and is available on Kaggle.
*   **AI Assistance:** The structure and content of this analysis were developed with assistance from Gemini, an AI model by Google.

---

## 11. Repository Links

*   **GitHub Repository:** [https://github.com/nyakabawurr-boop/Telco-Customer-Churn-Analysis](https://github.com/nyakabawurr-boop/Telco-Customer-Churn-Analysis)
*   **Kaggle Dataset:** [https://www.kaggle.com/datasets/blastchar/telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
*   **Google Colab Notebook:** [https://colab.research.google.com/drive/144GQEmf4GCDoauPvRseTRNFpF9kYDZOB](https://colab.research.google.com/drive/144GQEmf4GCDoauPvRseTRNFpF9kYDZOB?usp=sharing)

---

**Course:** ISOM 835 - Predictive Analytics Modelling  
**Project:** Telco Customer Churn Analysis
