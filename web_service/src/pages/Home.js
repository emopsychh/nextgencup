import React, { useEffect, useState } from 'react';
import TournamentCard from '../components/TournamentCard/TournamentCard';
import MyTournamentCard from '../components/MyTournamentCard/MyTournamentCard';
import FireIcon from '../../src/asset/fire.png';

import './Home.css';

function Home() {
  const [showContent, setShowContent] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setShowContent(true), 10);
    return () => clearTimeout(timer);
  }, []);

  const hotTournaments = [
    { id: 1, title: 'Counter-Strike', gameName: 'Counter-Strike', mode: '5х5', prize: '10 000₽', status: 'Открытый', date: "20 апреля" },
    { id: 2, title: 'Counter-Strike', gameName: 'Counter-Strike', mode: '1х1', prize: '5 000₽', status: 'Закрытый', date: "20 апреля" },
    { id: 3, title: 'Counter-Strike', gameName: 'Counter-Strike', mode: '1х1', prize: '5 000₽', status: 'Закрытый', date: "20 апреля" },
  ];

  const myTournaments = [
    { id: 4, title: 'Spring Cup Championship', gameName: 'Counter-Strike', mode: '5х5', prize: '20 000₽', participants: 10, status: 'Открытый', date: "20 апреля" },
    { id: 5, title: 'Autumn Cup', gameName: 'Counter-Strike', mode: '5х5', prize: '15 000₽', participants: 8, status: 'Закрытый', date: "20 апреля" },
    { id: 6, title: 'Autumn Cup', gameName: 'Counter-Strike', mode: '5х5', prize: '15 000₽', participants: 8, status: 'Закрытый', date: "20 апреля" },
  ];

  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Nextgen</h1>
        <p>Играй. Побеждай.<br /> Зарабатывай.</p>
        <button className="primary-button">Участвовать в турнире</button>
      </header>

      {/* Только здесь добавляем анимацию */}
      <div className={`home-content ${showContent ? 'fade-in1' : ''}`}>
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
          <div className="-title">
            <h2>Мои турниры</h2>
          </div>
          <div className="my-tournaments-list">
            {myTournaments.map(t => (
              <MyTournamentCard key={t.id} tournament={t} />
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}

export default Home;
