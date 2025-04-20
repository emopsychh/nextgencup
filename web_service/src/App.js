// src/App.js
import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';

import Home from './pages/Home.js';
import Profile from './pages/Profile.js';
import Tournaments from './pages/Tournaments.js';
import BottomNav from './components/BottomNav/BottomNav.js';

import './App.css'; 

function App() {
  return (
    <Router>
      <div className="app-container">
        <div className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/tournaments" element={<Tournaments />} />
          </Routes>
        </div>
        <BottomNav />
      </div>
    </Router>
  );
}

export default App;
