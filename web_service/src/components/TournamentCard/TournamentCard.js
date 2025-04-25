import React, { useState } from 'react';
import './TournamentCard.css';
import csIcon from '../../asset/cs.jpg';
import arrowImg from '../../asset/arrow2.png';

function TournamentCard({ tournament }) {
  const { gameName, mode, prize, status, date } = tournament;

  const [modalOpen, setModalOpen] = useState(false);

  const handleClick = () => {
    setModalOpen(true);
  };

  const handleClose = () => {
    setModalOpen(false);
  };

  // Проверяем открытый/закрытый статус
  const isOpen = status === 'Открытый';

  return (
    <>
      <div className="tournament-card" onClick={handleClick}> 
        <div className='head-line'>
          <div className="card-icon-wrapper">
            <img src={csIcon} alt="Иконка игры" className="card-icon" />
          </div> 

          <div className='right-for-icon'>
            <div className={`status-badge ${isOpen ? 'open' : 'closed'}`}>
              {status}
            </div> 

            <div className="mode-label">
              {mode}
            </div>
          </div>
        </div>

        <div className="card-content">
          <h3 className="card-title">{gameName}</h3>
          <h3 className="card-prize">{prize}</h3>
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
            <p>Форма регистрации пока отсутствует.</p>
            <button onClick={handleClose}>Закрыть</button>
          </div>
        </div>
      )}
    </>
  );
}

export default TournamentCard;
