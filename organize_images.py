"""
Script to organize and copy images to the images/ folder
Run this script to automatically find and organize your visualization images
"""

import os
import shutil
from pathlib import Path

# Define the target directory
TARGET_DIR = Path("images")
TARGET_DIR.mkdir(exist_ok=True)

# Required image filenames
REQUIRED_IMAGES = {
    # Data Exploration
    "churn_distribution.png": ["churn", "distribution", "bar"],
    "tenure_distribution.png": ["tenure", "distribution", "histogram"],
    "monthly_charges_distribution.png": ["monthly", "charges", "distribution", "histogram"],
    "total_charges_distribution.png": ["total", "charges", "distribution", "histogram"],
    "churn_by_contract.png": ["churn", "contract", "type"],
    "tenure_vs_charges.png": ["tenure", "charges", "scatter"],
    "monthly_charges_by_churn.png": ["monthly", "charges", "churn", "box"],
    
    # Analysis
    "correlation_matrix.png": ["correlation", "matrix", "heatmap"],
    "feature_importance.png": ["feature", "importance", "bar"],
    
    # Results
    "roc_random_forest.png": ["roc", "random", "forest"],
    "roc_xgboost.png": ["roc", "xgboost"],
    "roc_logistic.png": ["roc", "logistic", "lasso", "regression"],
    "confusion_matrix_random_forest.png": ["confusion", "random", "forest"],
    "confusion_matrix_xgboost.png": ["confusion", "xgboost"],
    "confusion_matrix_logistic.png": ["confusion", "logistic", "lasso"],
}

def find_images_in_directory(directory):
    """Find all PNG/JPG images in a directory"""
    image_files = []
    for ext in ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG']:
        image_files.extend(Path(directory).rglob(ext))
    return image_files

def match_image_to_filename(image_path, required_images):
    """Try to match an image file to a required filename based on keywords"""
    image_name_lower = image_path.name.lower()
    
    best_match = None
    best_score = 0
    
    for required_name, keywords in required_images.items():
        score = sum(1 for keyword in keywords if keyword in image_name_lower)
        if score > best_score:
            best_score = score
            best_match = required_name
    
    return best_match if best_score > 0 else None

def organize_images(source_directory=None):
    """Organize images from source directory to images/ folder"""
    
    if source_directory is None:
        # Common locations to search
        search_dirs = [
            Path.home() / "Downloads",
            Path.home() / "Desktop",
            Path("."),
            Path(".."),
        ]
        
        print("Searching for images in common locations...")
        all_images = []
        for search_dir in search_dirs:
            if search_dir.exists():
                images = find_images_in_directory(search_dir)
                all_images.extend(images)
                print(f"Found {len(images)} images in {search_dir}")
    else:
        source_path = Path(source_directory)
        if not source_path.exists():
            print(f"Error: Source directory '{source_directory}' does not exist!")
            return
        all_images = find_images_in_directory(source_path)
        print(f"Found {len(all_images)} images in {source_directory}")
    
    # Match and copy images
    copied = {}
    for image_path in all_images:
        match = match_image_to_filename(image_path, REQUIRED_IMAGES)
        if match and match not in copied:
            target_path = TARGET_DIR / match
            try:
                shutil.copy2(image_path, target_path)
                copied[match] = image_path
                print(f"[OK] Copied: {image_path.name} -> {match}")
            except Exception as e:
                print(f"[ERROR] Error copying {image_path.name}: {e}")
    
    # Check what's missing
    print("\n" + "="*50)
    print("Summary:")
    print("="*50)
    
    existing = set(f.name for f in TARGET_DIR.glob("*.png"))
    existing.update(f.name for f in TARGET_DIR.glob("*.jpg"))
    existing.update(f.name for f in TARGET_DIR.glob("*.jpeg"))
    
    missing = set(REQUIRED_IMAGES.keys()) - existing
    
    if copied:
        print(f"\n[OK] Successfully copied {len(copied)} images")
    if missing:
        print(f"\n[!] Missing {len(missing)} images:")
        for img in sorted(missing):
            print(f"  - {img}")
    else:
        print("\n[OK] All required images are present!")
    
    return copied, missing

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Use provided directory
        source_dir = sys.argv[1]
        organize_images(source_dir)
    else:
        # Search common locations
        print("Organizing images...")
        print("Usage: python organize_images.py [source_directory]")
        print("If no directory provided, will search Downloads, Desktop, and current directory\n")
        organize_images()

