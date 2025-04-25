import React, { useState } from 'react';
import './Tournaments.css';
import MyTournamentCard from '../components/MyTournamentCard/MyTournamentCard';
import MyTournamentCardActive from '../components/MyTournamentCard/MyTournamentCardActive';


function Tournaments() {
  const [activeTab, setActiveTab] = useState('active');

  const myTournaments = [
    { id: 1, title: 'The war of the Xan', mode: '5x5', prize: '20 000₽', status: 'Победа', date: '20 апреля' },
    { id: 1, title: 'Zumers vs Parents', mode: '2x2', prize: '5 000₽', status: 'Победа', date: '23 апреля' },
  ];

  const activeTournaments = [
    { id: 1, title: 'Битва за чекушку', mode: '1x1', prize: '350₽', status: 'Открытый', date: '22 апреля' },
    { id: 2, title: 'Заруба на дискотеке', mode: '7x7', prize: '1 000₽', status: 'Закрытый', date: '26 апреля' },
    { id: 2, title: 'Деревенский переполох', mode: '20x20', prize: '100 000₽', status: 'Открытый', date: '28 апреля' },

  ];

  return (
    <div className="tournaments-page">
      <div className="tab-wrapper">
        <div className={`tab-bg ${activeTab}`} />
        <button
          className={`tab ${activeTab === 'active' ? 'active' : ''}`}
          onClick={() => setActiveTab('active')}
        >
          Активные 
        </button>
        <button
          className={`tab ${activeTab === 'my' ? 'active' : ''}`}
          onClick={() => setActiveTab('my')}
        >
          Завершенные
        </button>
      </div>

      <div className="tournament-lists-container">
        <div className={`tournament-list fade ${activeTab === 'active' ? 'visible' : 'hidden'}`}>
          {activeTournaments.map(t => (
            <MyTournamentCardActive key={t.id} tournament={t} />
          ))}
        </div>

        <div className={`tournament-list fade ${activeTab === 'my' ? 'visible' : 'hidden'}`}>
          {myTournaments.map(t => (
            <MyTournamentCard key={t.id} tournament={t} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Tournaments;
