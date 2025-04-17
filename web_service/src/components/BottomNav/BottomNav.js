// src/components/BottomNav/BottomNav.js
import React from 'react';
import { NavLink } from 'react-router-dom';
import './BottomNav.css'; 
import homeIcon from '../../asset/home.png' 
import personIcon from '../../asset/person.png' 
import contrIcon from '../../asset/controller.png'    
function BottomNav() {
  return (
    <nav className="bottom-nav">
      <NavLink to="/" className="nav-item">
        <img src={homeIcon} alt="Главная" className="nav-icon" />
        <span>Главная</span>
      </NavLink>
      <NavLink to="/profile" className="nav-item">
        <img src={personIcon} alt="Главная" className="nav-icon" />
        <span>Профиль</span>
      </NavLink>
      <NavLink to="/tournaments" className="nav-item">
        <img src={contrIcon} alt="Главная" className="nav-icon" />
        <span>Турниры</span>
      </NavLink>
    </nav>
  );
}

export default BottomNav;
