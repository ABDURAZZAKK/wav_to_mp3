from fastapi import UploadFile
from pydub import AudioSegment

from config import USERS_AUDIO_PATH


def save_wav_as_mp3(path: str,audio: UploadFile):
    AudioSegment.from_file(audio.file).export(path, format="mp3")

