import uvicorn
from fastapi import FastAPI, APIRouter
from user.urls import user_router
from db import init_models


app = FastAPI(title="Quizze")
main_router = APIRouter()

main_router.include_router(user_router, prefix="/users")

app.include_router(main_router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    await init_models()



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")