# SavageScript Implementation

This folder contains the implementation of SavageScript, a terminal-based AI that roasts your life choices before validating your existence.

## Setup

1. Make sure you have Python installed (Python 3.8+ recommended)
2. Install dependencies:
   ```
   pip install google-generativeai colorama tqdm python-dotenv
   ```
3. Add your Gemini API key to the `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
   
   You can get an API key from the [Google AI Studio](https://ai.google.dev/).

## Running the Script

To run SavageScript, use the following command from the root directory:

```bash
python src/savage_script.py
```

## How it Works

1. The script initializes and configures the Gemini model with your API key.
2. It displays a welcome message with instructions.
3. You enter a self-description (e.g., "I'm a programmer who spends more time debugging than writing new code").
4. The script sends your input to the Gemini model along with a carefully crafted prompt that instructs it to:
   - Generate a savage roast based on your description
   - Follow it with a sincere compliment
   - Return the response in a structured JSON format
5. The script parses the JSON response and displays the roast and compliment with different colors.

## Adding Features

This is a basic implementation. You can extend it by:

- Adding a RAG (Retrieval-Augmented Generation) component to ground the roasts in a database of examples
- Implementing function calling to trigger special effects based on the roast content
- Adding a history feature to remember past interactions
- Creating different prompt templates (zero-shot, one-shot, multi-shot) as described in the main README
