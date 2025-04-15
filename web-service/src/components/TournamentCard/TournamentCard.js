// src/components/TournamentCard/TournamentCard.js
import React from 'react';
import './TournamentCard.css';

function TournamentCard({ tournament }) {
  const { title, date, isOpen, mode, status, prize } = tournament;

  return (
    <div className="tournament-card">
      <div className="tournament-info">
        <h3>{title}</h3>
        {mode && <p>{mode}</p>}
        {date && <p>{date}</p>}
        {prize && <p>Призовой фонд: {prize}</p>}
      </div>
      {isOpen && <span className="status-badge open">Открытый</span>}
      {status && <span className="status-badge">{status}</span>}
    </div>
  );
}

export default TournamentCard;
