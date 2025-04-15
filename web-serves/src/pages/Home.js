// src/pages/Home.js
import React from 'react';
import TournamentCard from '../components/TournamentCard/TournamentCard';
import './Home.css'; // стили конкретно для главной (если нужно)

function Home() {
  // Здесь можно имитировать данные турниров, пока нет backend
  const hotTournaments = [
    { id: 1, title: 'Counter-Strike 10 000₽', date: '20 Апреля', isOpen: true, mode: '5х5' },
    { id: 2, title: 'Counter-Strike 5 000₽', date: '20 Апреля', isOpen: true, mode: '2х2' },
  ];

  const myTournaments = [
    { id: 3, title: 'Spring Cup Championship', date: '3 Марта', status: 'Победа', prize: '20 000₽' },
    { id: 4, title: 'Spring Cup Championship', date: '14 Апреля', status: 'Победа', prize: '20 000₽' },
    // ... и т.д.
  ];

  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Nextgen</h1>
        <p>Играй. Побеждай. Зарабатывай.</p>
        <button className="primary-button">Участвовать в турнире</button>
      </header>

      <section className="hot-tournaments-section">
        <h2>Горячие турниры</h2>
        <div className="tournaments-grid">
          {hotTournaments.map(t => (
            <TournamentCard key={t.id} tournament={t} />
          ))}
        </div>
      </section>

      <section className="my-tournaments-section">
        <h2>Мои турниры</h2>
        <div className="tournaments-grid">
          {myTournaments.map(t => (
            <TournamentCard key={t.id} tournament={t} />
          ))}
        </div>
      </section>
    </div>
  );
}

export default Home;
    