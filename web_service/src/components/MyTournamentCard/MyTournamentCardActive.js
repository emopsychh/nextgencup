
import React from 'react';
import './MyTournamentCardActive.css';
import csIcon from '../../asset/cs.jpg';

function MyTournamentCardActive({ tournament }) {
  const { title, mode, prize, status, date } = tournament;

  const isOpen = status === 'Открытый';

  return (
    <div className="my-tournament-card-active">
      {/* Левая иконка */}
      <img src={csIcon} alt="Иконка турнира" className="my-tournament-image" />

      {/* Правая часть */}
      <div className="my-tournament-content">
        <div className='my-tournament-header'>
          <h3 className="my-tournament-title1">{title}</h3>
          <span className={`my-tournament-status ${isOpen ? 'win' : 'lose'}`}>
            {status}
          </span>
        </div>

        <div className="prize-and-mode1">
          <p className="my-tournament-prize">Призовой фонд: {prize}</p>
          <span className="mode-label-active">{mode}</span>
        </div>

        <div className="my-tournament-footer">
          <span className="my-tournament-date">{date}</span>
        </div>
      </div>
    </div>
  );
}

export default MyTournamentCardActive;
