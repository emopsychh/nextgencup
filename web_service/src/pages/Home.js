import React from 'react';
import TournamentCard from '../components/TournamentCard/TournamentCard';
import MyTournamentCard from '../components/MyTournamentCard/MyTournamentCard';
import './Home.css'; 
import fireIcon from "../../src/asset/fire.png"
function Home() {
  // Пример тестовых данных; в будущем замените их на данные из API/БД
  const hotTournaments = [
    { 
      id: 1, 
      title: 'Counter-Strike 10 000₽', 
      gameName: 'Counter-Strike', 
      mode: '5x5', 
      prize: '10 000₽', 
      participants: 16, 
      status: 'Открытый', 
      date: '20 Апреля' 
    },
    { 
      id: 2, 
      title: 'Counter-Strike 5 000₽', 
      gameName: 'Counter-Strike', 
      mode: '1x1', 
      prize: '5 000₽', 
      participants: 2, 
      status: 'Закрытый', 
      date: '20 Апреля' 
    }
  ];

  const myTournaments = [
    { 
      id: 3, 
      title: 'Spring Cup Championship', 
      prize: '20 000₽', 
      status: 'Победа', 
      date: '3 Марта' 
    },
    { 
      id: 4, 
      title: 'Autumn Cup', 
      prize: '15 000₽', 
      status: 'Проигрыш', 
      date: '14 Апреля' 
    },
    { 
      id: 3, 
      title: 'Spring Cup Championship', 
      prize: '20 000₽', 
      status: 'Победа', 
      date: '3 Марта' 
    },
    { 
      id: 4, 
      title: 'Autumn Cup', 
      prize: '15 000₽', 
      status: 'Проигрыш', 
      date: '14 Апреля' 
    }
  ];

  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Nextgen</h1>
        <p>Играй. Побеждай. <br /> Зарабатывай.</p>
      </header>
      <button className="primary-button">Участвовать в турнире</button>
      
      <section className="hot-tournaments-section">
        <h2>Горячие турниры
           <img src={fireIcon} alt="" className="hot-icon" />
        </h2>
        <div className="tournaments-grid">
          {hotTournaments.map(t => (
            <TournamentCard key={t.id} tournament={t} />
          ))}
        </div>
      </section>
      
      <section className="my-tournaments-section">
        <h2>Мои турниры
        </h2>
        <div className="tournaments-grid">
          {myTournaments.map(t => (
            <MyTournamentCard key={t.id} tournament={t} />
          ))}
        </div>
      </section>
    </div>
  );
}

export default Home;
