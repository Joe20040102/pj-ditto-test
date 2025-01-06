from fastapi import FastAPI

from .api import llm


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(llm.router, prefix="/api/llm", tags=["llm"])

    return app

app = create_app()