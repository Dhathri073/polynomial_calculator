# Polynomial Calculator - Startup Script for PowerShell

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "   Polynomial Calculator Startup" -ForegroundColor Cyan
Write-Host "   Using Linked List Data Structure" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Error: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.7+ from https://www.python.org/" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""

# Check if Flask is installed
try {
    python -c "import flask" 2>$null
    Write-Host "✓ Dependencies OK" -ForegroundColor Green
} catch {
    Write-Host "Flask not installed. Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ Error: Failed to install dependencies" -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

Write-Host ""
Write-Host "Starting Polynomial Calculator..." -ForegroundColor Cyan
Write-Host ""
Write-Host "Server will run at: http://127.0.0.1:5000" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python app.py

Read-Host "Press Enter to exit"
