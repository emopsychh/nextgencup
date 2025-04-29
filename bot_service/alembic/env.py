import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

from bot_service.db_container.db import Base  # Импорт всех моделей
from bot_service.db_container.models import User, Tournament, TournamentParticipant
from bot_service.config import DATABASE_URL  # Подключение к базе

# Alembic Config
config = context.config

# Логирование из alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Метаинформация для Alembic
target_metadata = Base.metadata


def run_migrations_offline():
    """Запуск миграций в оффлайн-режиме (без подключения к базе)."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Запуск миграций через переданное подключение."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Запуск миграций в онлайн-режиме с асинхронным движком."""
    connectable = create_async_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
        echo=True  # можно убрать echo, если логи не нужны
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


# Основная точка входа
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
