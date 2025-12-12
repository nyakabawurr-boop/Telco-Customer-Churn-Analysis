@echo off
echo Starting Streamlit application...
echo.

cd /d "%~dp0"
python -m streamlit run app.py --server.port 8502

pause

