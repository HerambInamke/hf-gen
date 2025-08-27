# 🔥 SavageScript - CLI Setup Guide

## What is SavageScript?

SavageScript is a terminal-based AI that roasts your life choices before validating your existence. It's the brutally honest friend you never knew you needed, packaged in a fun CLI experience.

## Setup Instructions

### 1. Get a Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Go to API Keys section
4. Generate a new API key

### 2. Configure Your API Key

Edit the `.env` file in the root of the project and add your API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Install Dependencies

The project uses a Python virtual environment with the following dependencies:
- python-dotenv
- colorama
- tqdm
- google-generativeai
- requests

The dependencies should already be installed in the virtual environment.

### 4. Run SavageScript

#### On Windows:

Double-click the `run_savage_script.bat` file or run the PowerShell script:

```
.\run_savage_script.ps1
```

## How to Use

1. When prompted, describe yourself in a single line (e.g., "I'm a programmer who spends more time debugging than writing new code").
2. SavageScript will first roast you, then provide a sincere compliment to balance it out.
3. Type 'exit' to quit the application.

## Technical Details

### Gemini 1.5 Flash Model

SavageScript uses Google's Gemini 1.5 Flash model through the google-generativeai Python library. The responses are formatted as JSON to provide a clean separation between the roast and compliment components.

### Multiple-Shot Prompting

The application implements multiple-shot prompting, a technique that improves the model's output quality by providing example inputs and outputs. Our system prompt includes several examples of user descriptions and corresponding roast/compliment pairs, which helps the model understand:

1. The expected tone and style for both roasts and compliments
2. The appropriate level of humor and edginess without crossing into offensive territory
3. The exact JSON format that the application expects

This approach results in more consistent, higher-quality responses that better match the intended personality of SavageScript.

### Error Handling

The application includes robust error handling to:
- Verify the JSON structure of responses
- Recover from malformed responses when possible
- Provide clear feedback when issues occur

## Troubleshooting

- **API Key Issues**: Make sure your API key is correctly pasted in the `.env` file without any extra spaces or quotes.
- **Connection Issues**: Ensure you have a stable internet connection to reach the Gemini API servers.
- **Response Format Errors**: If you see an error about parsing JSON, it might mean the model didn't return a properly formatted response. Try again with a different description.

## License

This project is created for educational purposes.
