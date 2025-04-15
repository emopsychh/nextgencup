from . import start, profile, tournaments
from . import start, profile, tournaments, back

routers = [
    start.router,
    profile.router,
    tournaments.router,
    back.router,
    # сюда добавим остальные
]