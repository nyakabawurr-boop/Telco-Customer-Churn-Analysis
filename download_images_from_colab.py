"""
Script to download/save images from Google Colab notebook
Run this in your Colab notebook to save all visualizations
"""

# Instructions for using this script in Google Colab:
"""
1. Copy this code into a cell in your Colab notebook
2. Make sure all your visualizations have been generated
3. Run the cell to save all images
4. Download the images folder from Colab
5. Extract and copy the images to your local images/ folder
"""

import matplotlib.pyplot as plt
import os

# Create images directory in Colab
os.makedirs('images', exist_ok=True)

# Image mapping - Update these with your actual figure objects
# Example: If you have plt.figure() objects, save them like this:

def save_all_images():
    """
    Save all your visualization images with the correct filenames.
    Update this function with your actual figure objects.
    """
    
    # Example structure - REPLACE WITH YOUR ACTUAL FIGURES:
    # 
    # # Data Exploration Images
    # fig1 = plt.figure()  # Your churn distribution plot
    # fig1.savefig('images/churn_distribution.png', dpi=300, bbox_inches='tight')
    # plt.close(fig1)
    # 
    # fig2 = plt.figure()  # Your tenure distribution plot
    # fig2.savefig('images/tenure_distribution.png', dpi=300, bbox_inches='tight')
    # plt.close(fig2)
    # 
    # ... and so on for all images
    
    print("Images saved! Now download the 'images' folder from Colab.")
    print("Files to save:")
    print("""
    Data Exploration:
    - churn_distribution.png
    - tenure_distribution.png
    - monthly_charges_distribution.png
    - total_charges_distribution.png
    - churn_by_contract.png
    - tenure_vs_charges.png
    - monthly_charges_by_churn.png
    
    Analysis:
    - correlation_matrix.png
    - feature_importance.png
    
    Results:
    - roc_random_forest.png
    - roc_xgboost.png
    - roc_logistic.png
    - confusion_matrix_random_forest.png
    - confusion_matrix_xgboost.png
    - confusion_matrix_logistic.png
    """)

# Alternative: If you're using seaborn/matplotlib, you can use this pattern:
"""
# For each plot you create, save it immediately:
import matplotlib.pyplot as plt
import seaborn as sns

# Example: Churn distribution
plt.figure(figsize=(10, 6))
# ... your plotting code ...
plt.savefig('images/churn_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Example: ROC Curve
plt.figure(figsize=(10, 6))
# ... your plotting code ...
plt.savefig('images/roc_random_forest.png', dpi=300, bbox_inches='tight')
plt.close()
"""

if __name__ == "__main__":
    save_all_images()

