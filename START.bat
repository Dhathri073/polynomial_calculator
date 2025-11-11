@echo off
REM Polynomial Calculator - Startup Script for Windows

echo.
echo ============================================
echo   Polynomial Calculator Startup
echo   Using Linked List Data Structure
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python 3.7+ from https://www.python.org/
    pause
    exit /b 1
)

echo ✓ Python found
echo.

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo Flask not installed. Installing dependencies...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo ✓ Dependencies OK
echo.

REM Start the Flask server
echo Starting Polynomial Calculator...
echo.
echo Server will run at: http://127.0.0.1:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
pause
