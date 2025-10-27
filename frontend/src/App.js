import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import toast, { Toaster } from 'react-hot-toast';
import InputSection from './components/InputSection';
import ResultsSection from './components/ResultsSection';
import LeaderboardSection from './components/LeaderboardSection';
import ThemeToggle from './components/ThemeToggle';

function App() {
  const [darkMode, setDarkMode] = useState(true);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    // Load theme preference
    const savedTheme = localStorage.getItem('darkMode');
    if (savedTheme !== null) {
      setDarkMode(savedTheme === 'true');
    }
    
    // Toggle dark mode class
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    
    // Load leaderboard
    fetchLeaderboard();
  }, [darkMode]);

  const fetchLeaderboard = async () => {
    try {
      const response = await fetch('/api/leaderboard?limit=5');
      const data = await response.json();
      setLeaderboard(data.leaderboard || []);
    } catch (error) {
      console.error('Error fetching leaderboard:', error);
    }
  };

  const handleSubmit = async (input) => {
    if (!input.trim()) {
      toast.error('Please enter something about yourself!');
      return;
    }

    setLoading(true);
    
    // Play sound effect
    playSoundEffect();

    try {
      const response = await fetch('/api/roast', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
      });

      if (!response.ok) {
        throw new Error('Failed to generate roast');
      }

      const data = await response.json();
      setResults(data);
      
      // Show success toast
      toast.success('Roast generated successfully! 🔥');
      
      // Refresh leaderboard
      fetchLeaderboard();
      
      // Scroll to results
      setTimeout(() => {
        const resultsSection = document.getElementById('results');
        if (resultsSection) {
          resultsSection.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
      
    } catch (error) {
      console.error('Error generating roast:', error);
      toast.error('Failed to generate roast. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const playSoundEffect = () => {
    // Create a simple beep sound effect using Web Audio API
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.frequency.value = 800;
    oscillator.type = 'sine';
    
    gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
    
    oscillator.start(audioContext.currentTime);
    oscillator.stop(audioContext.currentTime + 0.2);
  };

  const handleTryAgain = () => {
    setResults(null);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className={`min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-white transition-colors duration-300 ${!darkMode ? 'dark bg-gradient-to-br from-gray-100 via-white to-gray-200 text-gray-900' : ''}`}>
      <Toaster 
        position="top-right"
        toastOptions={{
          className: '',
          duration: 3000,
          style: {
            background: darkMode ? '#1a1a1a' : '#fff',
            color: darkMode ? '#fff' : '#000',
            border: darkMode ? '1px solid #333' : '1px solid #e5e7eb',
          },
        }}
      />
      
      <div className="container mx-auto px-4 py-8">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="max-w-6xl mx-auto"
        >
          {/* Header */}
          <div className="text-center mb-12">
            <ThemeToggle darkMode={darkMode} setDarkMode={setDarkMode} />
            
            <motion.h1 
              className="text-6xl md:text-8xl font-bold mb-4 bg-gradient-to-r from-red-500 via-yellow-500 to-orange-500 bg-clip-text text-transparent"
              initial={{ scale: 0.5 }}
              animate={{ scale: 1 }}
              transition={{ type: "spring", stiffness: 260, damping: 20 }}
            >
              SAVAGE SCRIPT
            </motion.h1>
            
            <motion.p 
              className="text-xl md:text-2xl text-gray-400 dark:text-gray-500"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.3 }}
            >
              🔥 Your brutally honest AI friend 🔥
            </motion.p>
            
            <motion.p 
              className="text-sm md:text-base text-gray-500 dark:text-gray-600 mt-4"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.5 }}
            >
              Tell us about yourself, and we'll roast you... then build you back up.
            </motion.p>
          </div>

          {/* Input Section */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.7 }}
            className="mb-12"
          >
            <InputSection onSubmit={handleSubmit} loading={loading} darkMode={darkMode} />
          </motion.div>

          {/* Results Section */}
          <AnimatePresence>
            {results && (
              <motion.div
                id="results"
                initial={{ opacity: 0, y: 50 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -50 }}
                transition={{ duration: 0.5 }}
              >
                <ResultsSection 
                  results={results} 
                  onTryAgain={handleTryAgain}
                  darkMode={darkMode}
                />
              </motion.div>
            )}
          </AnimatePresence>

          {/* Leaderboard Section */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1 }}
            className="mt-16"
          >
            <LeaderboardSection leaderboard={leaderboard} darkMode={darkMode} />
          </motion.div>

          {/* Footer */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.2 }}
            className="text-center mt-16 text-gray-500 dark:text-gray-600"
          >
            <p>Powered by Google Gemini AI</p>
          </motion.div>
        </motion.div>
      </div>
    </div>
  );
}

export default App;

