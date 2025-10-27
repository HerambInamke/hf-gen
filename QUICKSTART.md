# 🚀 SavageScript Quick Start Guide

Get your SavageScript app up and running in minutes!

## Prerequisites

1. **Docker & Docker Compose** installed
2. **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/)

## Setup Steps

### 1. Get Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Go to "Get API Key" section
4. Create a new API key
5. Copy the key

### 2. Configure Environment

Create a `.env` file in the project root:

```bash
# On Windows
echo GEMINI_API_KEY=your_actual_api_key_here > .env

# On Linux/Mac
echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
```

Or manually create the file and add:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Run the Application

#### Option 1: Using Docker Compose (Recommended)

**Windows:**
```bash
start_docker.bat
```

**Linux/Mac:**
```bash
chmod +x start_docker.sh
./start_docker.sh
```

Or directly:
```bash
docker-compose up --build
```

#### Option 2: Using Docker CLI

```bash
# Build the image
docker build -t savage-script .

# Run the container
docker run -p 5000:5000 --env-file .env savage-script
```

### 4. Access the App

Open your browser and visit:
```
http://localhost:5000
```

## Using the Application

1. **Type your confession** in the input field
   - Example: "I'm a programmer who spends more time debugging than writing new code"

2. **Click "Get Roasted! 🔥"** button

3. **Wait for the magic** ✨
   - Watch the loading animation
   - Hear the sound effect
   - See your roast and compliment appear

4. **Try again** or **check the leaderboard** for recent roasts

5. **Toggle dark/light mode** using the button in the top-right

## Troubleshooting

### Port 5000 Already in Use

If port 5000 is busy, edit `docker-compose.yml`:

```yaml
ports:
  - "5001:5000"  # Use port 5001 instead
```

Then access at `http://localhost:5001`

### Docker Not Running

**Windows:**
- Start Docker Desktop
- Wait for it to fully start (whale icon in system tray)

**Linux:**
```bash
sudo systemctl start docker
```

### API Key Issues

Make sure your `.env` file contains:
```
GEMINI_API_KEY=your_key_here
```

No spaces, no quotes, no `your_api_key_here` placeholder!

### Frontend Not Loading

1. Check if backend is running:
   ```bash
   curl http://localhost:5000/api/health
   ```

2. Check Docker logs:
   ```bash
   docker-compose logs
   ```

3. Rebuild containers:
   ```bash
   docker-compose up --build --force-recreate
   ```

## Development Mode

### Run Backend Only (Flask)

```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

### Run Frontend Only (React)

```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm start
```

Frontend will be on `http://localhost:3000`
Backend API on `http://localhost:5000`

## Production Deployment

### Deploy to Render

1. Push code to GitHub
2. Create new Web Service on Render
3. Connect repository
4. Set environment variable: `GEMINI_API_KEY`
5. Deploy!

### Deploy to Railway

1. Push code to GitHub
2. Create new project on Railway
3. Connect repository
4. Add environment variable: `GEMINI_API_KEY`
5. Deploy!

## What's Next?

- Read the [README-DOCKER.md](README-DOCKER.md) for detailed documentation
- Check out [SETUP.md](SETUP.md) for CLI version setup
- Read [readme.md](readme.md) for project details

## Need Help?

- Check the logs: `docker-compose logs -f`
- Verify API key: Ensure it's set correctly in `.env`
- Test connection: `curl http://localhost:5000/api/health`

Happy Roasting! 🔥

