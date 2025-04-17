import React, { useState } from 'react';
import './TournamentCard.css';
import csIcon from '../../asset/cs.jpg';        // Изображение игры (иконка)
import arrowImg from '../../asset/arrow2.png';    // Изображение стрелки

function TournamentCard({ tournament }) {
  const { title, gameName, mode, prize, status, date } = tournament;
  const [modalOpen, setModalOpen] = useState(false);

  const handleClick = () => {
    setModalOpen(true);
  };

  const handleClose = () => {
    setModalOpen(false);
  };

  return (
    <>
      <div className="tournament-card" onClick={handleClick}>
        <div className="card-icon-wrapper">
          <img src={csIcon} alt="Иконка игры" className="card-icon" />
        </div>
        
        <div className="status-container">
          <div className="status-badge">
            {status}
          </div>
          <div className="card-participants">
            {mode}
          </div>
        </div>
        
        
        <div className="card-content">
          <h3 className="card-title">{title}</h3>
          <p className="card-game">{gameName}</p> 
          <p className="card-prize"> {prize}</p> 
        </div>
        
        <div className="card-footer">
          <span className="card-date">{date}</span>
          <img src={arrowImg} alt="Стрелка" className="card-arrow" />
        </div>
      </div>

      {modalOpen && (
        <div className="modal-overlay" onClick={handleClose}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <h2>Регистрация на турнир</h2>
            <p>Здесь можно разместить форму регистрации.</p>
            <button onClick={handleClose}>Закрыть</button>
          </div>
        </div>
      )}
    </>
  );
}

export default TournamentCard;
