import React from 'react';
import { motion } from 'framer-motion';

const ResultsSection = ({ results, onTryAgain, darkMode }) => {
  return (
    <div className="space-y-8">
      {/* Roast Card */}
      <motion.div
        initial={{ opacity: 0, x: -50 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ delay: 0.2 }}
        className={`rounded-2xl shadow-2xl p-8 border-l-4 ${
          darkMode ? 'bg-gray-800 border-red-500' : 'bg-white border-red-500'
        }`}
      >
        <div className="flex items-start space-x-4">
          <motion.div
            animate={{ rotate: [0, 10, -10, 0] }}
            transition={{ duration: 0.5 }}
            className="text-4xl"
          >
            🔥
          </motion.div>
          <div className="flex-1">
            <h3 className="text-xl font-bold mb-3 text-red-500">The Roast</h3>
            <p className={`text-lg leading-relaxed ${darkMode ? 'text-gray-300' : 'text-gray-700'}`}>
              {results.roast}
            </p>
          </div>
        </div>
      </motion.div>

      {/* Compliment Card */}
      <motion.div
        initial={{ opacity: 0, x: 50 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ delay: 0.4 }}
        className={`rounded-2xl shadow-2xl p-8 border-l-4 ${
          darkMode ? 'bg-gray-800 border-green-500' : 'bg-white border-green-500'
        }`}
      >
        <div className="flex items-start space-x-4">
          <motion.div
            animate={{ scale: [1, 1.2, 1] }}
            transition={{ duration: 2, repeat: Infinity }}
            className="text-4xl"
          >
            💚
          </motion.div>
          <div className="flex-1">
            <h3 className="text-xl font-bold mb-3 text-green-500">The Compliment</h3>
            <p className={`text-lg leading-relaxed ${darkMode ? 'text-gray-300' : 'text-gray-700'}`}>
              {results.compliment}
            </p>
          </div>
        </div>
      </motion.div>

      {/* Try Again Button */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.6 }}
        className="flex justify-center"
      >
        <motion.button
          onClick={onTryAgain}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          className="px-8 py-4 rounded-lg font-semibold bg-gradient-to-r from-purple-600 to-pink-600 text-white shadow-lg hover:from-purple-700 hover:to-pink-700 transition-all"
        >
          Try Again? 🎲
        </motion.button>
      </motion.div>
    </div>
  );
};

export default ResultsSection;

