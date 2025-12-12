# Streamlit App Launcher
Write-Host "Starting Streamlit application..." -ForegroundColor Green
Write-Host ""

# Change to the script directory
Set-Location $PSScriptRoot

# Start Streamlit on port 8502
python -m streamlit run app.py --server.port 8502

Write-Host ""
Write-Host "If the browser didn't open automatically, go to: http://localhost:8502" -ForegroundColor Yellow

