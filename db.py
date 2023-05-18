from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

from user.tables import metadata

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as sesion:
        yield sesion

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
