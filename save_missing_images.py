"""
Script to help save the two missing confusion matrix images
If you have the images, place them in the Downloads folder with any name,
and this script will help identify and rename them.
"""

import os
import shutil
from pathlib import Path
from PIL import Image

def find_and_save_confusion_matrices():
    """Find confusion matrix images and save them with correct names"""
    
    images_dir = Path("images")
    downloads_dir = Path.home() / "Downloads"
    
    # Check if images already exist
    xgboost_path = images_dir / "confusion_matrix_xgboost.png"
    logistic_path = images_dir / "confusion_matrix_logistic.png"
    
    if xgboost_path.exists() and logistic_path.exists():
        print("✓ Both confusion matrices already exist!")
        return True
    
    # Look for new images in Downloads
    print("Searching for confusion matrix images...")
    print("\nPlease ensure the images are saved in your Downloads folder.")
    print("They can have any filename - this script will help identify them.")
    
    # Check Downloads for recent PNG files
    if downloads_dir.exists():
        png_files = list(downloads_dir.glob("*.png"))
        recent_files = [f for f in png_files if f.stat().st_mtime > (os.path.getmtime(__file__) - 3600)]
        
        if recent_files:
            print(f"\nFound {len(recent_files)} recent PNG files in Downloads:")
            for i, f in enumerate(recent_files[:10], 1):
                size_kb = f.stat().st_size / 1024
                print(f"  {i}. {f.name} ({size_kb:.1f} KB)")
            
            print("\n" + "="*60)
            print("MANUAL INSTRUCTIONS:")
            print("="*60)
            print("\n1. Open each image to identify which is which:")
            print("   - XGBoost: Should show 'Tuned XGBoost Classifier' in title")
            print("   - Logistic: Should show 'Tuned Logistic/Lasso Regression' in title")
            print("\n2. Rename them manually:")
            print(f"   - Copy XGBoost confusion matrix to: images/confusion_matrix_xgboost.png")
            print(f"   - Copy Logistic confusion matrix to: images/confusion_matrix_logistic.png")
            print("\nOr use PowerShell:")
            print('   Copy-Item "Downloads\\[filename].png" "images\\confusion_matrix_xgboost.png"')
            print('   Copy-Item "Downloads\\[filename].png" "images\\confusion_matrix_logistic.png"')
        else:
            print("\nNo recent PNG files found in Downloads.")
            print("\nTo add the missing images:")
            print("1. Download them from your Colab notebook")
            print("2. Save them to your Downloads folder")
            print("3. Run this script again, or manually copy them to the images/ folder")
    
    return False

if __name__ == "__main__":
    find_and_save_confusion_matrices()

