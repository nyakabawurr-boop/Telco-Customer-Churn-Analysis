# Instructions: Downloading Images from Google Colab

Since your images are in your Google Colab notebook, follow these steps to download them:

## Method 1: Save Images Directly in Colab (Recommended)

1. **Open your Colab notebook**: https://colab.research.google.com/drive/144GQEmf4GCDoauPvRseTRNFpF9kYDZOB

2. **Add this code cell** at the end of your notebook (after all visualizations are created):

```python
import matplotlib.pyplot as plt
import os

# Create images directory
os.makedirs('images', exist_ok=True)

# Save each figure with the correct filename
# Replace 'fig' with your actual figure variable names

# Data Exploration Images
# Example: plt.savefig('images/churn_distribution.png', dpi=300, bbox_inches='tight')

# After saving all images, download the folder:
from google.colab import files
import shutil

# Create a zip file
shutil.make_archive('images', 'zip', 'images')
files.download('images.zip')
```

3. **Update your plotting code** to save images. For each plot, add:
   ```python
   plt.savefig('images/filename.png', dpi=300, bbox_inches='tight')
   plt.close()  # Close to free memory
   ```

4. **Run the cell** to download the images.zip file

5. **Extract the zip** and copy all PNG files to your local `images/` folder

## Method 2: Manual Download from Colab

1. In your Colab notebook, right-click on any image/plot
2. Select "Save image as..." or "Download"
3. Save with the correct filename from IMAGE_GUIDE.md
4. Repeat for all 13 images
5. Copy all images to your local `images/` folder

## Method 3: Use Colab's File Browser

1. In Colab, click the folder icon (📁) in the left sidebar
2. If you've saved images, they'll appear in the file browser
3. Right-click each image → Download
4. Save with correct filenames
5. Copy to your local `images/` folder

## Required Filenames

Make sure to save/download with these exact names:

### Data Exploration (7 images)
- `churn_distribution.png`
- `tenure_distribution.png`
- `monthly_charges_distribution.png`
- `total_charges_distribution.png`
- `churn_by_contract.png`
- `tenure_vs_charges.png`
- `monthly_charges_by_churn.png`

### Analysis (2 images)
- `correlation_matrix.png`
- `feature_importance.png`

### Results (6 images)
- `roc_random_forest.png`
- `roc_xgboost.png`
- `roc_logistic.png`
- `confusion_matrix_random_forest.png`
- `confusion_matrix_xgboost.png`
- `confusion_matrix_logistic.png`

## After Downloading

1. Place all images in: `TelcoCustomerChurn/images/`
2. Verify all 13 images are present
3. Restart your Streamlit app
4. Navigate through sections to see your visualizations!

## Quick Check

Run this in PowerShell to verify images are in place:
```powershell
Get-ChildItem images\*.png | Select-Object Name
```

You should see all 13 image files listed.

