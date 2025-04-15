from . import start, profile, tournaments

routers = [
    start.router,
    profile.router,
    tournaments.router,
    # сюда добавим остальные
]