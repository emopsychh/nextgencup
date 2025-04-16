from . import start, profile, tournaments
from . import start, profile, tournaments, settings

routers = [
    start.router,
    profile.router,
    tournaments.router,
    settings.router,
    # сюда добавим остальные
]