// src/pages/Profile.js
import React from 'react';
import './Profile.css';
import settingsIcon from '../asset/settings.png';
import defaultAvatar from '../asset/Sex.jpg';
import arrowRight from '../asset/arrowRight.png';  
export default function Profile() {
  return (
    <div className="profile-container">
      <header className="profile-header">
        <img src={settingsIcon} alt="Настройки" className="settings-icon" />
        <img src={defaultAvatar} alt="Аватар" className="avatar" />
        <h2 className="nickname">nickname</h2>
      </header>

      <div className="profile-menu">
        {['Кошелёк', 'Достижения', 'Статистика'].map((label) => (
          <div key={label} className="profile-menu-item">
            <span className="menu-label">{label}</span>
            <img src={arrowRight} alt="" className="menu-arrow" />
          </div>
        ))}
      </div>
    </div>
  );
}
