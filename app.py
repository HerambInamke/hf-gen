#!/usr/bin/env python3
"""
Flask API wrapper for SavageScript
"""

import os
import json
import re
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime
import sqlite3

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)  # Enable CORS for React frontend

# Get API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key or api_key == "your_api_key_here":
    print("[ERROR] Gemini API key not found!")
    print("Please add your API key to the .env file: GEMINI_API_KEY=your_api_key_here")

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize database
def init_db():
    conn = sqlite3.connect('savage_script.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS roasts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_input TEXT,
                  roast TEXT,
                  compliment TEXT,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

def estimate_tokens(text):
    """Estimate token count using a simple algorithm."""
    words = len(re.findall(r'\b\w+\b', text))
    punctuation = len(re.findall(r'[^\w\s]', text))
    return words + punctuation

@app.route('/')
def index():
    """Serve the React frontend."""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "message": "SavageScript API is running"})

@app.route('/api/roast', methods=['POST'])
def get_roast():
    """Generate a roast and compliment."""
    data = request.get_json()
    user_input = data.get('input', '').strip()
    
    if not user_input:
        return jsonify({"error": "Please provide some input"}), 400
    
    try:
        # System prompt
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
        
        # Initialize Gemini model
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        
        # Generate response
        response = model.generate_content(
            [system_prompt, f"Here is the user's self-description: \"{user_input}\""]
        )
        
        # Parse JSON response
        response_text = response.text
        
        # Remove markdown code blocks if present
        if response_text.startswith("```json") or response_text.startswith("```"):
            response_text = response_text.replace("```json", "", 1)
            response_text = response_text.replace("```", "", 1)
            if "```" in response_text:
                response_text = response_text[:response_text.rfind("```")]
            response_text = response_text.strip()
        
        # Parse JSON
        try:
            response_json = json.loads(response_text)
            
            # Verify response has required keys
            if "roast" not in response_json or "compliment" not in response_json:
                raise ValueError("Response missing required keys")
            
            # Save to database
            save_roast_to_db(user_input, response_json['roast'], response_json['compliment'])
            
            return jsonify({
                "roast": response_json['roast'],
                "compliment": response_json['compliment'],
                "timestamp": datetime.now().isoformat()
            })
            
        except json.JSONDecodeError:
            # Try to extract JSON if there's extra text
            if "{" in response_text and "}" in response_text:
                json_part = response_text[response_text.find("{"):response_text.rfind("}")+1]
                try:
                    response_json = json.loads(json_part)
                    save_roast_to_db(user_input, response_json['roast'], response_json['compliment'])
                    return jsonify({
                        "roast": response_json['roast'],
                        "compliment": response_json['compliment'],
                        "timestamp": datetime.now().isoformat()
                    })
                except:
                    pass
            
            # Fallback response
            return jsonify({
                "roast": "I tried to roast you, but my circuits got confused. Maybe you're too complex for my algorithms.",
                "compliment": "But I can tell you're patient with technology, and that's a valuable trait in today's world.",
                "timestamp": datetime.now().isoformat()
            }), 500
            
    except Exception as e:
        return jsonify({"error": f"Failed to generate roast: {str(e)}"}), 500

def save_roast_to_db(user_input, roast, compliment):
    """Save roast to database."""
    conn = sqlite3.connect('savage_script.db')
    c = conn.cursor()
    c.execute('INSERT INTO roasts (user_input, roast, compliment) VALUES (?, ?, ?)',
              (user_input, roast, compliment))
    conn.commit()
    conn.close()

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    """Get recent roasts from the database."""
    limit = request.args.get('limit', 10, type=int)
    conn = sqlite3.connect('savage_script.db')
    c = conn.cursor()
    c.execute('SELECT user_input, roast, compliment, created_at FROM roasts ORDER BY created_at DESC LIMIT ?', (limit,))
    rows = c.fetchall()
    conn.close()
    
    leaderboard = []
    for row in rows:
        leaderboard.append({
            "user_input": row[0],
            "roast": row[1],
            "compliment": row[2],
            "created_at": row[3]
        })
    
    return jsonify({"leaderboard": leaderboard})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

