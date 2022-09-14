"""dsb.app.main."""
from fastapi import FastAPI
from app import config


def init_app() -> FastAPI:
    """Init application"""
    application = FastAPI()
    application.router.prefix = config.API_PREFIX
    return application


app = init_app()


@app.get("/")
async def root():
    return {"message": "Hello World"}
