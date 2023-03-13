from fastapi import FastAPI

from container import Container
from db import async_engine, discover_model_classes
from urls import setup_routers


class FastAPIWithContainer(FastAPI):
    container: Container


def create_app() -> FastAPIWithContainer:
    container = Container()
    app = FastAPIWithContainer()
    app.container = container

    return app


app = create_app()


@app.on_event("startup")
async def startup() -> None:
    setup_routers(app=app)
    discover_model_classes()


@app.on_event("shutdown")
async def shutdown() -> None:
    await async_engine.dispose()
