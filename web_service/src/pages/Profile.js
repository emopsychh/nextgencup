// src/pages/Profile.js
import React, { useState, useEffect } from 'react'; // добавлен useEffect
import './Profile.css';
import defaultAvatar from '../asset/Sex.jpg';

export default function Profile() {
  const [activeTab, setActiveTab] = useState('stats');
  const [showContent, setShowContent] = useState('stats'); // добавлено

  useEffect(() => {
    const timer = setTimeout(() => setShowContent(activeTab), 10); // небольшая задержка
    return () => clearTimeout(timer);
  }, [activeTab]);

  return (
    <div className="profile-container">
      <header className="profile-header">
        <img src={defaultAvatar} alt="Аватар" className="avatar" />
        <h2 className="nickname">nickname</h2>
      </header>

      {/* Таб-переключатель */}
      <div className="tab-wrapper">
        <div className={`tab-bg ${activeTab}`} />
        <button
          className={`tab ${activeTab === 'stats' ? 'active' : ''}`}
          onClick={() => setActiveTab('stats')}
        >
          Статистика
        </button>
        <button
          className={`tab ${activeTab === 'achievements' ? 'active' : ''}`}
          onClick={() => setActiveTab('achievements')}
        >
          Достижения
        </button>
      </div>

      {/* Контент табов */}
      <div className="tab-content">
        {showContent === 'stats' ? (
          <div key="stats" className="fade-in">
            <div className="stats-grid">
              {['K/D', 'Win Rate%', 'Streak', 'Average kills', 'Headshot%', 'Rating'].map((label) => (
                <div key={label} className="stat-card">
                  <div className="stat-label">{label}</div>
                  <div className="stat-value">---</div>
                </div>
              ))}
            </div>
            <div className="matches-info">
              <h3 className="last-matches-title">Последние матчи</h3>
              <p className="no-matches">У вас нет матчей</p>
            </div>
          </div>
        ) : (
          <div key="achievements" className="achievements-placeholder fade-in">
            Скоро здесь будут достижения
          </div>
        )}
      </div>
    </div>
  );
}
