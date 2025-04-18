import React from 'react';
import './MyTournamentCard.css';
import csIcon from '../../asset/cs.jpg'; // Замените на путь к вашей иконке

function MyTournamentCard({ tournament }) {
  const { title, prize, status, date } = tournament;

  // Преобразуем статус
  const resultText = status === 'Открытый' ? 'Победа' : 'Поражение';
  const isWin = resultText === 'Победа';

  return (
    <div className="my-tournament-card">
      {/* Левая иконка */}
      <img src={csIcon} alt="Иконка турнира" className="my-tournament-image" />
      
      {/* Правая часть */}
      <div className="my-tournament-content">
        <div className='my-tournament-header'>
          <h3 className="my-tournament-title">{title}</h3>
          <span className={`my-tournament-status ${isWin ? 'win' : 'lose'}`}>
            {resultText}
          </span>
        </div>
        <p className="my-tournament-prize">Призовой фонд: {prize}</p>
        
        <div className="my-tournament-footer">
          <span className="my-tournament-date">{date}</span>
        </div>
      </div>
    </div>
  );
}


export default MyTournamentCard;
