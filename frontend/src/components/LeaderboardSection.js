import React from 'react';
import { motion } from 'framer-motion';

const LeaderboardSection = ({ leaderboard, darkMode }) => {
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  };

  return (
    <div className={`rounded-2xl shadow-2xl p-8 ${darkMode ? 'bg-gray-800' : 'bg-white'} border ${darkMode ? 'border-gray-700' : 'border-gray-200'}`}>
      <h2 className="text-2xl font-bold mb-6 flex items-center">
        <span className="mr-2">🏆</span>
        Recent Roasts
      </h2>
      
      {leaderboard.length === 0 ? (
        <p className={`text-center py-8 ${darkMode ? 'text-gray-400' : 'text-gray-600'}`}>
          No roasts yet. Be the first to get roasted! 🔥
        </p>
      ) : (
        <div className="space-y-4">
          {leaderboard.map((item, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className={`rounded-lg p-4 ${darkMode ? 'bg-gray-700' : 'bg-gray-50'}`}
            >
              <div className="flex items-start justify-between mb-2">
                <p className={`text-sm font-semibold ${darkMode ? 'text-gray-300' : 'text-gray-700'}`}>
                  "{item.user_input}"
                </p>
                <span className={`text-xs ${darkMode ? 'text-gray-500' : 'text-gray-500'}`}>
                  {formatDate(item.created_at)}
                </span>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-3">
                <div className={`p-3 rounded border-l-2 ${darkMode ? 'bg-red-900/20 border-red-500' : 'bg-red-50 border-red-400'}`}>
                  <p className="text-xs font-semibold text-red-500 mb-1">🔥 Roast</p>
                  <p className={`text-sm ${darkMode ? 'text-gray-300' : 'text-gray-700'}`}>
                    {item.roast}
                  </p>
                </div>
                
                <div className={`p-3 rounded border-l-2 ${darkMode ? 'bg-green-900/20 border-green-500' : 'bg-green-50 border-green-400'}`}>
                  <p className="text-xs font-semibold text-green-500 mb-1">💚 Compliment</p>
                  <p className={`text-sm ${darkMode ? 'text-gray-300' : 'text-gray-700'}`}>
                    {item.compliment}
                  </p>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      )}
    </div>
  );
};

export default LeaderboardSection;

