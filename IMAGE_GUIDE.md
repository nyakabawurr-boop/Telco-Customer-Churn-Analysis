# Image Setup Guide

This guide helps you add your visualization images to the Streamlit application.

## Quick Start

1. **Create the images folder** (already created): `images/`

2. **Add your images** with these exact filenames:

### Data Exploration Section
- `churn_distribution.png` - Bar chart showing distribution of churn (0=No, 1=Yes)
- `tenure_distribution.png` - Histogram of customer tenure
- `monthly_charges_distribution.png` - Histogram of monthly charges
- `total_charges_distribution.png` - Histogram of total charges
- `churn_by_contract.png` - Bar chart of churn rate by contract type
- `tenure_vs_charges.png` - Scatter plot of tenure vs monthly charges colored by churn
- `monthly_charges_by_churn.png` - Box plot of monthly charges by churn status

### Analysis Section
- `correlation_matrix.png` - Heatmap showing correlations between features and churn
- `feature_importance.png` - Horizontal bar chart of top 15 feature importances

### Results Section
- `roc_random_forest.png` - ROC curve for Random Forest (AUC = 0.82)
- `roc_xgboost.png` - ROC curve for XGBoost (AUC = 0.82)
- `roc_logistic.png` - ROC curve for Logistic/Lasso Regression (AUC = 0.82)
- `confusion_matrix_random_forest.png` - Confusion matrix for Random Forest
- `confusion_matrix_xgboost.png` - Confusion matrix for XGBoost
- `confusion_matrix_logistic.png` - Confusion matrix for Logistic Regression

## Image Mapping from Your Descriptions

Based on the images you provided, here's the mapping:

| Your Image Description | Filename to Use |
|------------------------|-----------------|
| Distribution of Customer Churn (Encoded) | `churn_distribution.png` |
| Distribution of Tenure, Monthly Charges, Total Charges | `tenure_distribution.png`, `monthly_charges_distribution.png`, `total_charges_distribution.png` |
| Churn Rate by Contract Type | `churn_by_contract.png` |
| Tenure vs. Monthly Charges scatter plot | `tenure_vs_charges.png` |
| Monthly Charges by Churn Status box plot | `monthly_charges_by_churn.png` |
| Correlation Matrix | `correlation_matrix.png` |
| Top 15 Feature Importances | `feature_importance.png` |
| ROC Curve - Random Forest | `roc_random_forest.png` |
| ROC Curve - XGBoost | `roc_xgboost.png` |
| ROC Curve - Logistic/Lasso | `roc_logistic.png` |
| Confusion Matrix - Random Forest | `confusion_matrix_random_forest.png` |
| Confusion Matrix - XGBoost | `confusion_matrix_xgboost.png` |
| Confusion Matrix - Logistic/Lasso | `confusion_matrix_logistic.png` |

## Supported Formats

- PNG (recommended)
- JPG/JPEG

## Notes

- The app will automatically display images when they're placed in the `images/` folder
- If an image is missing, the app will show a helpful message
- Images are displayed with responsive width (use_container_width=True)
- All images should be saved from your analysis notebooks/scripts

## Testing

After adding images, restart your Streamlit app:
```bash
streamlit run app.py --server.port 8502
```

Then navigate through the sections to verify all images display correctly.

