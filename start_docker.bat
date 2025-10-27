@echo off
echo 🔥 Starting SavageScript...
echo.

REM Check if .env file exists
if not exist .env (
    echo ❌ Error: .env file not found!
    echo.
    echo Please create a .env file with your Gemini API key:
    echo GEMINI_API_KEY=your_actual_api_key_here
    echo.
    echo You can get an API key from: https://aistudio.google.com/
    pause
    exit /b 1
)

REM Check if GEMINI_API_KEY is set
findstr /C:"GEMINI_API_KEY" .env >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: GEMINI_API_KEY not set in .env file!
    echo.
    echo Please add your API key to the .env file:
    echo GEMINI_API_KEY=your_actual_api_key_here
    pause
    exit /b 1
)

echo 🐳 Building and starting Docker containers...
docker-compose up --build
pause

