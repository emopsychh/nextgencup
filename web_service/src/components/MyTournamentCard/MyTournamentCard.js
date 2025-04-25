import React from 'react';
import './MyTournamentCard.css';
import csIcon from '../../asset/cs.jpg'; // Замените на путь к вашей иконке

function MyTournamentCard({ tournament }) {
  const { title, mode, prize, status, date } = tournament;

  // Преобразуем статус
  const resultText = status === 'Открытый' ? 'Победа' : 'Поражение';
  const isWin = resultText === 'Победа';

  return (
    <div className="my-tournament-card1">
      {/* Левая иконка */}
      <img src={csIcon} alt="Иконка турнира" className="my-tournament-image1" />

      {/* Правая часть */}
      <div className="my-tournament-content1">
        <div className='my-tournament-header1'>
          <h3 className="my-tournament-title1">{title}</h3>
          <span className={`my-tournament-status1 ${isWin ? 'win' : 'lose'}`}>
            {resultText}
          </span>
        </div>

        <div className="prize-and-mode2">
          <p className="my-tournament-prize1">Призовой фонд: {prize}</p>
          <div className="mode-and-date">
            <span className="mode-label3">{mode}</span>
            <span className="my-tournament-date1">{date}</span>
          </div>
        </div>

      </div>
    </div>
  );
}

export default MyTournamentCard;
