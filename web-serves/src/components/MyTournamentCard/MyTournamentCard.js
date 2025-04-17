import React from 'react';
import './MyTournamentCard.css';
import csIcon from '../../asset/cs.jpg'; // Замените на путь к вашей иконке

function MyTournamentCard({ tournament }) {
  // Распакуем нужные поля из объекта турнира
  const { title, prize, status, date } = tournament;

  return (
    <div className="my-tournament-card">
    {/* Блок изображения */}
    <img src={csIcon} alt="Иконка турнира" className="my-tournament-image" />
  
    {/* Оборачиваем текстовое содержимое в отдельный контейнер */}
    <div className="my-tournament-content">
        <h3 className="my-tournament-title">{title}</h3>
        <p className="my-tournament-prize">Призовой фонд: {prize}</p>
        <div className="my-tournament-footer">
        <span className="my-tournament-status">{status}</span>
        <span className="my-tournament-date">{date}</span>
        </div>
        </div>
    </div>
    
  );
}

export default MyTournamentCard;
