"""
Script to help identify and rename plot images
This will open each image so you can identify what it is
"""

import os
from pathlib import Path
from PIL import Image
import subprocess
import sys

images_dir = Path("images")
plot_files = sorted(images_dir.glob("plot_*.png"))

if not plot_files:
    print("No plot_*.png files found in images/ directory")
    sys.exit(1)

print(f"Found {len(plot_files)} plot files to identify\n")
print("="*60)
print("IMAGE IDENTIFICATION GUIDE")
print("="*60)
print("\nBased on your image descriptions, here's the mapping:")
print("\nData Exploration (7 images):")
print("  1. churn_distribution.png - Bar chart: Distribution of Customer Churn")
print("  2. tenure_distribution.png - Histogram: Distribution of Tenure")
print("  3. monthly_charges_distribution.png - Histogram: Distribution of Monthly Charges")
print("  4. total_charges_distribution.png - Histogram: Distribution of Total Charges")
print("  5. churn_by_contract.png - Bar chart: Churn Rate by Contract Type")
print("  6. tenure_vs_charges.png - Scatter plot: Tenure vs Monthly Charges")
print("  7. monthly_charges_by_churn.png - Box plot: Monthly Charges by Churn Status")
print("\nAnalysis (2 images):")
print("  8. correlation_matrix.png - Heatmap: Correlation Matrix")
print("  9. feature_importance.png - Bar chart: Top 15 Feature Importances")
print("\nResults (6 images):")
print("  10. roc_random_forest.png - ROC Curve: Random Forest")
print("  11. roc_xgboost.png - ROC Curve: XGBoost")
print("  12. roc_logistic.png - ROC Curve: Logistic/Lasso Regression")
print("  13. confusion_matrix_random_forest.png - Confusion Matrix: Random Forest")
print("  14. confusion_matrix_xgboost.png - Confusion Matrix: XGBoost")
print("  15. confusion_matrix_logistic.png - Confusion Matrix: Logistic Regression")
print("\n" + "="*60)
print("\nTo identify images, you can:")
print("1. Open each plot_*.png file manually")
print("2. Match it to the descriptions above")
print("3. Rename them using the mapping below")
print("\nOr use this automated approach:")

# Create a mapping based on common patterns
# This is a guess - you may need to adjust
mapping = {
    # Try to match based on common patterns
    # You'll need to verify these manually
}

print("\n" + "="*60)
print("AUTOMATED RENAMING")
print("="*60)
print("\nTo rename automatically, create a mapping dictionary in this script")
print("or manually rename using:")
print("\nExample PowerShell commands:")
for i, plot_file in enumerate(plot_files, 1):
    print(f'  Rename-Item "images\\{plot_file.name}" "images\\[correct_filename].png"')
    print(f'  # plot_{i} -> [identify and use correct name]')

print("\n" + "="*60)
print("QUICK RENAME HELPER")
print("="*60)
print("\nRun this in PowerShell to rename (update the numbers):")
print("\n$files = @{")
for i, plot_file in enumerate(plot_files, 1):
    print(f'    "{plot_file.name}" = "[correct_name].png"  # Update this')
print("}")
print('foreach ($old in $files.Keys) {')
print('    Rename-Item "images\\$old" "images\\$($files[$old])"')
print('}')

