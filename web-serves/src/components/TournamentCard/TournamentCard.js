import React, { useState } from 'react';
import './TournamentCard.css';
import csIcon from '../../asset/cs.jpg';
import arrowImg from '../../asset/arrow2.png';
function TournamentCard({ tournament }) {
  // Извлекаем нужные поля из объекта турнира
  // Поля можно назвать, как угодно: title, gameName, mode, prize, participants, status.
  const { title, gameName, mode, prize, participants, status, date } = tournament;

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
        <div className="status-badge">
          {status}
        </div> 
        <div className="card-content">
          <h3 className="card-title">{title}</h3>
          <p className="card-game">{gameName}</p>
          <p className="card-mode">{mode}</p>
          <p className="card-prize">Призовой фонд: {prize}</p>
          <p className="card-participants">Участников: {participants}</p>
          <div className="card-footer">
            <span className="card-date">{date}</span>
            <img src={arrowImg} alt="" className="card-arrow" />
        </div>
          
        </div>
      </div>
       
      {modalOpen && (
        <div className="modal-overlay" onClick={handleClose}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <h2>Регистрация на турнир</h2>
            <p>Форма регистрации пока отсутствует.Саш а как это будет</p>
            <button onClick={handleClose}>Закрыть</button>
          </div>
        </div>
      )}
    </>
  );
}

export default TournamentCard;
