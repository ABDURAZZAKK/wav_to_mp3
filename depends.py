from db import get_async_session
from user.tables import users, audios
from user.menager import UserMenager, AudioMenager
from user.DTOs import UserDTO, Audio


async def get_user_menager() -> UserMenager:
    async for session in get_async_session():
        yield UserMenager(session, users, UserDTO)

async def get_audio_menager() -> AudioMenager:
    async for session in get_async_session():
        yield AudioMenager(session, audios, Audio)         