import contextlib

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from .core import async_engine


def async_session(expire_on_commit: bool = False):
    return sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=expire_on_commit,
    )()


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@contextlib.asynccontextmanager
async def transaction(async_session):
    if not async_session.in_transaction():
        async with async_session.begin():
            yield

    else:
        async with async_session.begin_nested():
            yield

    await async_session.commit()
