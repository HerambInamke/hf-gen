import React, { useState } from 'react';
import { motion } from 'framer-motion';

const InputSection = ({ onSubmit, loading, darkMode }) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(input);
    setInput(''); // Clear input after submission
  };

  return (
    <div className={`rounded-2xl shadow-2xl p-8 ${darkMode ? 'bg-gray-800' : 'bg-white'} border ${darkMode ? 'border-gray-700' : 'border-gray-200'}`}>
      <form onSubmit={handleSubmit}>
        <div className="mb-6">
          <label htmlFor="userInput" className="block text-sm font-semibold mb-3">
            Tell us about yourself
          </label>
          <textarea
            id="userInput"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="e.g., I'm a programmer who spends more time debugging than writing new code..."
            className={`w-full px-4 py-3 rounded-lg border focus:outline-none focus:ring-2 focus:ring-red-500 transition-all ${
              darkMode 
                ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400' 
                : 'bg-gray-50 border-gray-300 text-gray-900 placeholder-gray-500'
            }`}
            rows="4"
            disabled={loading}
          />
        </div>
        
        <motion.button
          type="submit"
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          disabled={loading || !input.trim()}
          className={`w-full py-4 px-6 rounded-lg font-semibold text-white bg-gradient-to-r from-red-600 to-orange-600 hover:from-red-700 hover:to-orange-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-lg ${
            loading ? 'animate-pulse' : ''
          }`}
        >
          {loading ? (
            <span className="flex items-center justify-center">
              <motion.span
                animate={{ rotate: 360 }}
                transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                className="mr-2"
              >
                🔥
              </motion.span>
              Cooking up something savage...
            </span>
          ) : (
            'Get Roasted! 🔥'
          )}
        </motion.button>
      </form>
    </div>
  );
};

export default InputSection;

