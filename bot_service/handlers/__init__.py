# bot_service/handlers/__init__.py

from .start import router as start_router
from .profile import router as profile_router
from .tournaments import router as tournaments_router
from .settings import router as settings_router

routers = [
    start_router,
    profile_router,
    tournaments_router,
    settings_router,
]
