# 🔥 SavageScript - Docker Edition

**SavageScript** is a modern, containerized AI application that roasts your life choices before validating your existence. Now with a beautiful React frontend and full Docker support!

## ✨ Features

- 🐳 **Fully Dockerized** - Easy deployment with Docker Compose
- ⚛️ **Modern React Frontend** - Beautiful UI with Framer Motion animations
- 🎨 **TailwindCSS** - Responsive, modern styling
- 🌙 **Dark Mode** - Toggle between light and dark themes
- 🏆 **Leaderboard** - View recent roasts from other users
- 🔄 **Dynamic UI** - Smooth animations and transitions
- 💾 **SQLite Database** - Persistent storage for roasts
- 🎵 **Sound Effects** - Audio feedback on roast generation
- 📱 **Responsive Design** - Works on all devices

## 🚀 Quick Start with Docker

### Prerequisites

1. **Docker** and **Docker Compose** installed
   - [Install Docker](https://docs.docker.com/get-docker/)
   - [Install Docker Compose](https://docs.docker.com/compose/install/)

2. **Gemini API Key**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Sign in and generate a new API key

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd hf-gen
   ```

2. **Create a `.env` file** in the root directory:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

3. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. **Access the application:**
   - Open your browser and navigate to `http://localhost:5000`
   - Start getting roasted! 🔥

### Using Docker

```bash
# Start the application
docker-compose up --build

# Stop the application
docker-compose down

# View logs
docker-compose logs -f

# Rebuild after changes
docker-compose up --build

# Run in background
docker-compose up -d
```

## 📖 Usage

1. **Enter your confession**: Type something about yourself in the input field (e.g., "I'm a programmer who spends more time debugging than writing new code")

2. **Get roasted**: Click "Get Roasted! 🔥" and wait for the AI to generate your roast

3. **View results**: See your roast and compliment side-by-side with smooth animations

4. **Browse leaderboard**: Check out recent roasts from other users

5. **Try again**: Click "Try Again? 🎲" to generate a new roast

6. **Toggle theme**: Click the sun/moon icon to switch between light and dark modes

## 🏗️ Architecture

```
hf-gen/
├── app.py                    # Flask API backend
├── requirements.txt          # Python dependencies
├── Dockerfile               # Multi-stage Docker build
├── docker-compose.yml       # Docker Compose configuration
├── frontend/                # React frontend
│   ├── src/
│   │   ├── App.js          # Main app component
│   │   ├── components/      # React components
│   │   └── index.js        # Entry point
│   ├── package.json        # Node dependencies
│   └── tailwind.config.js  # TailwindCSS config
└── savage_script.db        # SQLite database (auto-generated)
```

## 🛠️ Development

### Backend Development (Flask)

The Flask API runs on port 5000 and provides the following endpoints:

- `GET /` - Serve React frontend
- `GET /api/health` - Health check
- `POST /api/roast` - Generate roast and compliment
- `GET /api/leaderboard` - Get recent roasts

### Frontend Development (React)

To run the frontend in development mode:

```bash
cd frontend
npm install
npm start
```

The frontend will run on `http://localhost:3000` (with proxy to backend on port 5000).

### Backend Development (Flask)

To run the backend in development mode:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

## 🎨 Tech Stack

### Backend
- **Flask** - Python web framework
- **Google Gemini AI** - AI model for generating roasts
- **SQLite** - Database for storing roasts
- **Flask-CORS** - CORS support

### Frontend
- **React 18** - UI library
- **TailwindCSS** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **React Hot Toast** - Toast notifications
- **React Icons** - Icon library

## 🐳 Docker Details

### Dockerfile

The Dockerfile uses a **multi-stage build**:
1. **Frontend Builder**: Builds the React app
2. **Python Backend**: Runs Flask API and serves the frontend

### Container Features

- ✅ Alpine-based for smaller image size
- ✅ Multi-stage build for optimization
- ✅ Health checks included
- ✅ Volume mounts for persistent data
- ✅ Environment variable support

## 🌐 Deployment

### Deploy to Render

1. Create a new Web Service
2. Connect your GitHub repository
3. Set build command: `docker build -t savage-script .`
4. Set start command: `docker run -p 5000:5000 savage-script`
5. Add environment variable: `GEMINI_API_KEY`

### Deploy to Railway

1. Create a new project
2. Connect your GitHub repository
3. Railway will detect the Docker setup automatically
4. Add environment variable: `GEMINI_API_KEY`
5. Deploy!

## 📝 Environment Variables

Create a `.env` file with:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🔧 Troubleshooting

### API Key Issues
- Make sure your `.env` file has `GEMINI_API_KEY` set correctly
- Check that there are no extra spaces or quotes in the API key

### Docker Issues
- Ensure Docker is running: `docker info`
- Check logs: `docker-compose logs`
- Rebuild: `docker-compose up --build --force-recreate`

### Port Conflicts
- If port 5000 is in use, change it in `docker-compose.yml`
- Update the frontend build and restart

### Frontend Not Loading
- Check browser console for errors
- Verify the backend is running: `curl http://localhost:5000/api/health`
- Check Flask logs for errors

## 🎯 Future Enhancements

- [ ] Add user authentication
- [ ] Add social sharing features
- [ ] Implement advanced analytics
- [ ] Add more AI models for variety
- [ ] Create mobile app version
- [ ] Add sound effects customization
- [ ] Implement rate limiting
- [ ] Add admin dashboard

## 📄 License

This project is created for educational purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- Google Gemini AI for the AI capabilities
- React and TailwindCSS communities
- All the users who get roasted (and complimented!) daily

---

Made with 🔥 by the SavageScript team

