import React from 'react';
import { motion } from 'framer-motion';
import { FaMoon, FaSun } from 'react-icons/fa';

const ThemeToggle = ({ darkMode, setDarkMode }) => {
  const toggleTheme = () => {
    const newTheme = !darkMode;
    setDarkMode(newTheme);
    localStorage.setItem('darkMode', newTheme);
  };

  return (
    <motion.button
      onClick={toggleTheme}
      whileHover={{ scale: 1.1 }}
      whileTap={{ scale: 0.9 }}
      className={`fixed top-6 right-6 z-50 p-3 rounded-full shadow-lg transition-colors ${
        darkMode 
          ? 'bg-gray-700 hover:bg-gray-600 text-yellow-400' 
          : 'bg-gray-200 hover:bg-gray-300 text-gray-900'
      }`}
      aria-label="Toggle theme"
    >
      <motion.div
        initial={false}
        animate={{ rotate: darkMode ? 0 : 180 }}
        transition={{ duration: 0.3 }}
      >
        {darkMode ? <FaMoon size={20} /> : <FaSun size={20} />}
      </motion.div>
    </motion.button>
  );
};

export default ThemeToggle;

