import uuid
from pydantic import BaseModel



class UserDTO(BaseModel):
    id: int
    name: str
    token: uuid.UUID
    
    class Config:
        orm_mode = True


class UserIn(BaseModel):
    name: str



class Audio(BaseModel):
    id: uuid.UUID
    file_name: str
    file_path: str
    user_id = int
    
    class Config:
        orm_mode = True


class AudioIn(BaseModel):
    file_name: str
    file_path: str
    user_id = int 