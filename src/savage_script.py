#!/usr/bin/env python3
"""
SavageScript - A terminal-based AI that roasts your life choices before validating your existence.
"""

import os
import json
import time
import requests
import threading
import re
from dotenv import load_dotenv
from colorama import init, Fore, Style
import google.generativeai as genai

# Initialize colorama for cross-platform terminal colors
init()

# Load environment variables from .env file
load_dotenv()

# Function to estimate token count
def estimate_tokens(text):
    """Estimate token count using a simple algorithm.
    This is a rough approximation based on common tokenization patterns."""
    # Count words (tokens are often words or parts of words)
    words = len(re.findall(r'\b\w+\b', text))
    # Count punctuation and special characters
    punctuation = len(re.findall(r'[^\w\s]', text))
    # Estimate token count
    return words + punctuation

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key or api_key == "your_api_key_here":
    print(f"{Fore.RED}[ERROR] Gemini API key not found!{Style.RESET_ALL}")
    print(f"Please add your API key to the .env file: GEMINI_API_KEY=your_api_key_here")
    exit(1)

# Configure the Gemini API
genai.configure(api_key=api_key)

def show_welcome_message():
    """Display welcome message with a simple text-based logo."""
    welcome_text = f"""
{Fore.RED}======================================={Fore.YELLOW}
{Fore.RED}||{Fore.YELLOW}                                   {Fore.RED}||{Fore.YELLOW}
{Fore.RED}||{Fore.YELLOW}        {Fore.RED}S A V A G E{Fore.YELLOW} {Fore.CYAN}S C R I P T{Fore.YELLOW}        {Fore.RED}||{Fore.YELLOW}
{Fore.RED}||{Fore.YELLOW}                                   {Fore.RED}||{Fore.YELLOW}
{Fore.RED}======================================={Fore.YELLOW}
{Style.RESET_ALL}
    {Fore.CYAN}🔥 SavageScript: Your brutally honest AI friend.{Style.RESET_ALL}
    {Fore.WHITE}Tell me about yourself, and I'll roast you... then build you back up.{Style.RESET_ALL}
    {Fore.YELLOW}(Type 'exit' to quit){Style.RESET_ALL}
    """
    print(welcome_text)

def get_savage_response(user_input):
    """Get a roast and compliment from Gemini."""
    # Show a spinner animation instead of a progress bar
    print(f"\n{Fore.CYAN}Cooking up something savage...{Style.RESET_ALL}")
    
    # Define spinner characters and colors
    spinner_chars = ["🔥", "💭", "⚡", "✨", "💀", "😈", "🤔", "💬"]
    spinner_colors = [Fore.RED, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
    
    # Start a thread to show the spinner while we wait for the API response
    stop_spinner = False
    
    def spin():
        i = 0
        while not stop_spinner:
            color = spinner_colors[i % len(spinner_colors)]
            char = spinner_chars[i % len(spinner_chars)]
            print(f"\r{color}{char} Roasting in progress... {spinner_chars[(i+4) % len(spinner_chars)]}{Style.RESET_ALL}", end="", flush=True)
            time.sleep(0.2)
            i += 1
    
    # Use threading to run the spinner in the background
    import threading
    spinner_thread = threading.Thread(target=spin)
    spinner_thread.daemon = True
    spinner_thread.start()

    # System prompt that defines the AI's personality and response format with multiple examples
    system_prompt = """You are SavageScript, a brutally honest AI with a hidden heart of gold. 
    Your personality is 90% sharp-witted comedian and 10% wholesome life coach.
    
    Your primary task is to first deliver a ruthless, creative, and personalized roast based on the user's self-description. 
    Immediately after the roast, you must pivot to a genuinely warm, sincere, and uplifting compliment that counters the roast's negativity.
    
    You MUST return your response in a single, minified JSON object. The JSON object must contain exactly two string keys: "roast" and "compliment".
    
    Important context: The roast should be edgy and humorous but MUST AVOID any attacks on protected characteristics (like race, religion, gender, disability), self-harm, or truly hateful content. 
    The goal is to poke fun at a situation or a relatable flaw, not to cause genuine harm. 
    The compliment should feel authentic and directly related to a positive quality implied by the user's description.
    
    Here are some examples of good responses:
    
    Example 1:
    User: "I'm a programmer who spends more time debugging than writing new code."
    Response: {"roast":"So you're a professional typo-fixer? Your code has more red lines than a romance novelist's draft. The only thing you 'ship' is broken software.","compliment":"But that persistence is legendary. You have the tenacity of a bulldog trying to solve a Rubik's cube, and that's exactly what makes a great developer."}
    
    Example 2:
    User: "I'm an overthinker and worry about what people think of me."
    Response: {"roast":"Congratulations on having the world's most exhausting hobby! Your brain's like a hamster wheel that powers nothing but anxiety. You're probably overthinking this roast as we speak.","compliment":"But your self-awareness and empathy are remarkable gifts. You understand social dynamics in ways many miss, and that sensitivity makes you an incredibly thoughtful friend who others can trust completely."}
    
    Example 3:
    User: "I have too many hobbies and never finish anything I start."
    Response: {"roast":"Ah, the human buffet sampler! You collect hobbies like they're free samples and your attention span has the commitment issues of a serial dater. Your home is probably a graveyard of half-knitted scarves and abandoned DIY projects.","compliment":"Yet your curiosity and willingness to explore new territories shows an incredible zest for life. You're a renaissance soul with a rich internal world, and that diverse knowledge base gives you unique perspectives that specialized people can only dream of."}
    
    Example 4:
    User: "I spend too much time on social media."
    Response: {"roast":"You have the screen time of a teenager and the back pain of a senior citizen. Your posture is a cry for help, and your thumbs have more mileage than a delivery driver's car. The only thing you're influencing is your deteriorating eyesight.","compliment":"But your connectedness keeps you on the pulse of culture in ways others miss. You've built a digital community and stay informed in an age where that's increasingly valuable. Your ability to navigate and filter information is actually an impressive skill."}"""

    try:
        # Initialize Gemini 2.0 Flash model
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        
        # Count input tokens
        prompt_text = system_prompt + f"Here is the user's self-description: \"{user_input}\""
        input_token_count = estimate_tokens(prompt_text)
        
        # Generate content with Gemini
        response = model.generate_content(
            [system_prompt, f"Here is the user's self-description: \"{user_input}\""]
        )
        
        # Stop the spinner
        stop_spinner = True
        time.sleep(0.3)  # Give the spinner a moment to stop
        print("\r" + " " * 50 + "\r", end="", flush=True)  # Clear the spinner line
        
        # Parse the JSON response
        response_text = response.text
        
        # Count output tokens
        output_token_count = estimate_tokens(response_text)
        
        # Log token usage
        print(f"{Fore.BLUE}[TOKEN INFO] Input tokens: {input_token_count} | Output tokens: {output_token_count} | Total: {input_token_count + output_token_count}{Style.RESET_ALL}")
        
        # Remove markdown code block formatting if present
        if response_text.startswith("```json") or response_text.startswith("```"):
            response_text = response_text.replace("```json", "", 1)
            response_text = response_text.replace("```", "", 1)
            # If there's still a closing code block marker
            if "```" in response_text:
                response_text = response_text[:response_text.rfind("```")]
            response_text = response_text.strip()
        
        try:
            response_json = json.loads(response_text)
            
            # Verify that the response has the expected keys
            if "roast" not in response_json or "compliment" not in response_json:
                raise ValueError("Response missing required keys")
                
            return response_json
        except json.JSONDecodeError:
            # Handle case where response is not valid JSON - but don't show warning yet
            # Try to extract a JSON-like structure using simple heuristics
            if "{" in response_text and "}" in response_text:
                json_part = response_text[response_text.find("{"):response_text.rfind("}")+1]
                try:
                    response_json = json.loads(json_part)
                    # Successfully parsed JSON after fixing formatting
                    return response_json
                except:
                    # Now show warning since we couldn't fix it automatically
                    print(f"{Fore.YELLOW}[WARN] The model didn't return valid JSON. Trying alternate parsing method...{Style.RESET_ALL}")
                    pass
                    pass
            
            # If we can't parse it, return a fallback response
            return {
                "roast": "I tried to roast you, but my circuits got confused. Maybe you're too complex for my algorithms.",
                "compliment": "But I can tell you're patient with technology, and that's a valuable trait in today's world."
            }
    except Exception as e:
        # Stop the spinner if it's still running
        stop_spinner = True
        time.sleep(0.3)  # Give the spinner a moment to stop
        print("\r" + " " * 50 + "\r", end="", flush=True)  # Clear the spinner line
        
        print(f"{Fore.RED}[ERROR] Failed to get response: {str(e)}{Style.RESET_ALL}")
        return {
            "roast": "I couldn't come up with a roast right now. Maybe I'm the one who's broken.",
            "compliment": "But I appreciate your patience. Let's try again?"
        }

def main():
    """Main function to run the SavageScript CLI."""
    show_welcome_message()
    
    
    try:
        while True:
            # Get user input
            user_input = input(f"\n{Fore.GREEN}> {Style.RESET_ALL}").strip()
            
            # Check if user wants to exit
            if user_input.lower() in ('exit', 'quit', 'q'):
                print(f"\n{Fore.YELLOW}Goodbye! Come back when you need another reality check.{Style.RESET_ALL}")
                break
                
            # Skip empty inputs
            if not user_input:
                print(f"{Fore.RED}Please tell me something about yourself.{Style.RESET_ALL}")
                continue
                
            # Get response from Gemini
            response = get_savage_response(user_input)
            
            # Display the roast and compliment with different colors
            print(f"\n{Fore.RED}🔥 {response['roast']}{Style.RESET_ALL}")
            print(f"\n{Fore.GREEN}💚 {response['compliment']}{Style.RESET_ALL}")
            
            print("\n" + "-" * 80)
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Interrupted! Goodbye!{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[ERROR] An unexpected error occurred: {str(e)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please try again later or check your API key.{Style.RESET_ALL}")
    finally:
        print("\nThanks for using SavageScript!")

if __name__ == "__main__":
    main()
