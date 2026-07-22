from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="API oficial do projeto StudyFlow.",
    version=settings.APP_VERSION,
)

@app.get("/")
def root() -> dict[str, str]:
    return {
         "message": "Bem-vindo à API do StudyFlow!"
    }
