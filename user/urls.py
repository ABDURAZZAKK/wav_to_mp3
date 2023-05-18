import uuid, os
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, BackgroundTasks
from fastapi.responses import JSONResponse
from .DTOs import UserIn, UserDTO, AudioIn
from .menager import UserMenager, AudioMenager
from depends import get_user_menager, get_audio_menager
from config import USERS_AUDIO_PATH
from .services import save_wav_as_mp3
user_router = APIRouter()



@user_router.post("/")
async def create_user(
    user: UserIn,
    UM: UserMenager = Depends(get_user_menager)):

    return await UM.create(user)
    



@user_router.post("/attaching_file", response_class=JSONResponse)
async def attach_hw_file(
    u_id: int,
    u_token: uuid.UUID,
    audio: UploadFile, 
    backgroung: BackgroundTasks,
    UM: UserMenager = Depends(get_user_menager),
    AM: AudioMenager = Depends(get_audio_menager)
):

    if audio.filename.split('.')[-1] != 'wav':
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="send wav file")
    
    user = await UM.get_by_id(u_id)

    if not user is None:
        user = UserDTO.from_orm(user)
        if u_token == user.token:
            file_name = audio.filename.split('.')[0]
            if not os.path.isdir(f"{USERS_AUDIO_PATH}/{u_token}"):
                os.mkdir(f"{USERS_AUDIO_PATH}/{u_token}")
            
            file_path = f"{USERS_AUDIO_PATH}/{u_token}/{file_name}.mp3"

            if not await AM.get_by_file_path(file_path):
                await AM.create(AudioIn(file_name=file_name,
                                    file_path=file_path,
                                    user_id=u_id))
                backgroung.add_task(save_wav_as_mp3, file_path, audio)
                return {'message': "OK"}
            
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="a file with the same name already exists")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid token")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found ")


