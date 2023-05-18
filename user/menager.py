import uuid
import sqlalchemy as sa
from baseMenager import BaseMenager
from .tables import users, audios
from .DTOs import Audio, UserIn, UserDTO, AudioIn



class UserMenager(BaseMenager):
    async def create(self, d: UserIn | dict) -> dict:
        d = dict(d)
        new = UserDTO(
            id=0,
            name=d['name'],
            token=uuid.uuid4()
        )

        values = {**new.dict()}
        values.pop("id", None)
        query = sa.insert(users).values(**values).returning(users.c.id, users.c.token)
        new_user = await self.session.execute(query)
        new_user = new_user.fetchone()
        await self.session.commit()
        return {'id': new_user[0], 'token': new_user[1]}


    async def get_audios(self):
        query = sa.select(audios).where(audios.c.user_id == self.id)
        result = await self.session.execute(query)

        return result.all()
        

class AudioMenager(BaseMenager):
    async def create(self, d: AudioIn | dict) -> None:
        d = dict(d)
        new = Audio(
            id=uuid.uuid4(),
            file_name=d['file_name'],
            file_path=d['file_path']
        )

        values = {**new.dict()}
        query = sa.insert(audios).values(**values)
        new_user = await self.session.execute(query)
        await self.session.commit()


    async def get_by_file_path(self, file_path):
        query = sa.select(audios).where(audios.c.file_path == file_path)
        _ = await self.session.execute(query)

        if _ is None:
            return None
        return _