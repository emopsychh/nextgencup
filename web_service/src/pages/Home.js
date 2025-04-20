// src/pages/Home.js
import React from 'react';
import TournamentCard from '../components/TournamentCard/TournamentCard';
import MyTournamentCard from '../components/MyTournamentCard/MyTournamentCard';
import FireIcon from '../../src/asset/fire.png';

import './Home.css';

function Home() {
  // Пример данных турнира; в будущем они будут приходить из базы данных
  const hotTournaments = [
    {
      id: 1,
      title: 'Counter-Strike',
      gameName: 'Counter-Strike',
      mode: '5х5',
      prize: '10 000₽',
      status: 'Открытый',
      date:"20 апреля"
    },
    {
      id: 2,
      title: 'Counter-Strike',
      gameName: 'Counter-Strike',
      mode: '1х1',
      prize: '5 000₽',
      status: 'Закрытый',
      date:"20 апреля"
    },
    {
      id: 2,
      title: 'Counter-Strike',
      gameName: 'Counter-Strike',
      mode: '1х1',
      prize: '5 000₽',
      status: 'Закрытый',
      date:"20 апреля"
    },
  ];

  const myTournaments = [
    {
      id: 3,
      title: 'Spring Cup Championship',
      gameName: 'Counter-Strike',
      mode: '5х5',
      prize: '20 000₽',
      participants: 10,
      status: 'Открытый',
      date:"20 апреля"
    },
    {
      id: 4,
      title: 'Autumn Cup',
      gameName: 'Counter-Strike',
      mode: '5х5',
      prize: '15 000₽',
      participants: 8,
      status: 'Закрытый',
      date:"20 апреля"
    },
    {
      id: 5,
      title: 'Autumn Cup',
      gameName: 'Counter-Strike',
      mode: '5х5',
      prize: '15 000₽',
      participants: 8,
      status: 'Закрытый',
      date:"20 апреля"
    },
  ];

  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Nextgen</h1>
        <p>Играй. Побеждай.<br /> Зарабатывай.</p>
        <button className="primary-button">Участвовать в турнире</button>
      </header>

      <section className="hot-tournaments-section">
        <div className="hot-title">
          <h2>Горячие турниры</h2>
          <img src={FireIcon} alt="Иконка огня" className="fire-icon" />
        </div>
  
        <div className="tournaments-grid">
          {hotTournaments.map(t => (
          <TournamentCard key={t.id} tournament={t} />
          ))}
        </div>
      </section>


      <section className="my-tournaments-section">
        <h2>Мои турниры</h2>
        {/* Контейнер для списка турниров */}
        <div className="my-tournaments-list">
          {myTournaments.map(t => (
            <MyTournamentCard key={t.id} tournament={t} />
          ))}
        </div>
      </section>
    </div>
  );
}

export default Home;
