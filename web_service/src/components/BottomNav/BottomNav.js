import React from 'react';
import { NavLink } from 'react-router-dom';
import './BottomNav.css';

import homeIcon from '../../asset/home.png';
import personIcon from '../../asset/person.png';
import contrIcon from '../../asset/tournaments.png';

function BottomNav() {
  const navItems = [
    { to: '/', label: 'Главная', icon: homeIcon },
    { to: '/profile', label: 'Профиль', icon: personIcon },
    { to: '/tournaments', label: 'Турниры', icon: contrIcon }
  ];

  return (
    <nav className="bottom-nav">
      {navItems.map(({ to, label, icon }) => (
        <NavLink
          key={to}
          to={to}
          className={({ isActive }) => `nav-item${isActive ? ' active' : ''}`}
        >
          <img src={icon} alt={label} className="nav-icon" />
          <span>{label}</span>
        </NavLink>
      ))}
    </nav>
  );
}

export default BottomNav;
