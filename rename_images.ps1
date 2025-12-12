# PowerShell script to rename plot images based on likely identification
# This makes educated guesses - verify the images after running!

$imagesPath = "images"

# Based on file sizes and typical analysis order, here's the mapping
# LARGE files (300KB+) = Complex visualizations (correlation matrix, feature importance)
# MEDIUM files (40-60KB) = ROC curves, confusion matrices  
# SMALL files (20-25KB) = Simple charts (distributions, bar charts)

$mapping = @{
    # Data Exploration - typically created first, smaller files
    "plot_1.png" = "churn_distribution.png"           # Small (19KB) - Simple bar chart
    "plot_2.png" = "tenure_distribution.png"           # Medium (74KB) - Histogram
    "plot_3.png" = "monthly_charges_distribution.png"  # Small (25KB) - Histogram
    "plot_4.png" = "total_charges_distribution.png"    # Small (21KB) - Histogram
    "plot_5.png" = "correlation_matrix.png"            # LARGE (406KB) - Heatmap
    "plot_7.png" = "feature_importance.png"            # LARGE (344KB) - Bar chart
    "plot_8.png" = "churn_by_contract.png"             # Small (25KB) - Bar chart
    "plot_9.png" = "monthly_charges_by_churn.png"      # Medium (45KB) - Box plot
    "plot_10.png" = "tenure_vs_charges.png"           # Small (25KB) - Scatter plot
    
    # Results - typically created later
    "plot_11.png" = "roc_random_forest.png"            # Medium (43KB) - ROC curve
    "plot_12.png" = "roc_xgboost.png"                  # Small (26KB) - ROC curve
    "plot_13.png" = "roc_logistic.png"                # Medium (44KB) - ROC curve
    "plot_14.png" = "confusion_matrix_random_forest.png" # Medium (62KB) - Confusion matrix
}

# Check if we need to identify the remaining confusion matrices
# They might be in a different order - you may need to adjust

Write-Host "Renaming images based on educated guesses..." -ForegroundColor Yellow
Write-Host "PLEASE VERIFY the images after renaming!" -ForegroundColor Red
Write-Host ""

$renamed = 0
foreach ($oldName in $mapping.Keys) {
    $oldPath = Join-Path $imagesPath $oldName
    $newName = $mapping[$oldName]
    $newPath = Join-Path $imagesPath $newName
    
    if (Test-Path $oldPath) {
        if (Test-Path $newPath) {
            Write-Host "SKIP: $newName already exists" -ForegroundColor Yellow
        } else {
            Rename-Item -Path $oldPath -NewName $newName
            Write-Host "OK: $oldName -> $newName" -ForegroundColor Green
            $renamed++
        }
    } else {
        Write-Host "NOT FOUND: $oldName" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Renamed $renamed images" -ForegroundColor Cyan
Write-Host ""
Write-Host "IMPORTANT: Check the images folder and verify the names are correct!" -ForegroundColor Yellow
Write-Host "If any are wrong, you can manually rename them or adjust this script." -ForegroundColor Yellow

# Check what's still missing
Write-Host ""
Write-Host "Checking for missing images..." -ForegroundColor Cyan
$required = @(
    "churn_distribution.png",
    "tenure_distribution.png", 
    "monthly_charges_distribution.png",
    "total_charges_distribution.png",
    "churn_by_contract.png",
    "tenure_vs_charges.png",
    "monthly_charges_by_churn.png",
    "correlation_matrix.png",
    "feature_importance.png",
    "roc_random_forest.png",
    "roc_xgboost.png",
    "roc_logistic.png",
    "confusion_matrix_random_forest.png",
    "confusion_matrix_xgboost.png",
    "confusion_matrix_logistic.png"
)

$missing = @()
foreach ($img in $required) {
    $path = Join-Path $imagesPath $img
    if (-not (Test-Path $path)) {
        $missing += $img
    }
}

if ($missing.Count -eq 0) {
    Write-Host "All required images are present!" -ForegroundColor Green
} else {
    Write-Host "Still missing $($missing.Count) images:" -ForegroundColor Yellow
    $missing | ForEach-Object { Write-Host "  - $_" }
    Write-Host ""
    Write-Host "Note: You may have plot_6.png or other plot files that need to be identified." -ForegroundColor Yellow
}

