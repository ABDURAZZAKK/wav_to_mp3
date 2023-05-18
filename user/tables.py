import sqlalchemy as sa
import uuid


metadata = sa.MetaData()



users = sa.Table(
    "users",
    metadata,
    sa.Column('id',sa.Integer, primary_key=True, autoincrement=True),
    sa.Column('name',sa.String(63)),
    sa.Column('token', sa.UUID, unique=True),
)


audios = sa.Table(
    "audios",
    metadata,
    sa.Column('id',sa.UUID, primary_key=True, default=uuid.uuid4),
    sa.Column('file_name',sa.String(63)),
    sa.Column('file_path', sa.String(319), unique=True, nullable=True),
    sa.Column('user_id', sa.Integer, nullable=True)
)