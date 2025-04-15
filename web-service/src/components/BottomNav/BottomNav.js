// src/components/BottomNav/BottomNav.js
import React from 'react';
import { NavLink } from 'react-router-dom';
import './BottomNav.css'; 
function BottomNav() {
  return (
    <nav className="bottom-nav">
      <NavLink to="/" className="nav-item">
        {/* Можно вставить иконку (SVG) или текст */}
        <span>Главная</span>
      </NavLink>
      <NavLink to="/profile" className="nav-item">
        <span>Профиль</span>
      </NavLink>
      <NavLink to="/tournaments" className="nav-item">
        <span>Турниры</span>
      </NavLink>
    </nav>
  );
}

export default BottomNav;
