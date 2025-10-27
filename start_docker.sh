#!/bin/bash

echo "🔥 Starting SavageScript..."
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo ""
    echo "Please create a .env file with your Gemini API key:"
    echo "GEMINI_API_KEY=your_actual_api_key_here"
    echo ""
    echo "You can get an API key from: https://aistudio.google.com/"
    exit 1
fi

# Check if GEMINI_API_KEY is set
if ! grep -q "GEMINI_API_KEY" .env || grep -q "your_api_key_here" .env; then
    echo "❌ Error: GEMINI_API_KEY not set in .env file!"
    echo ""
    echo "Please add your API key to the .env file:"
    echo "GEMINI_API_KEY=your_actual_api_key_here"
    exit 1
fi

# Start Docker Compose
echo "🐳 Building and starting Docker containers..."
docker-compose up --build

