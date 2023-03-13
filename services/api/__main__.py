import uvicorn

from settings import settings

uvicorn_logging_config = uvicorn.config.LOGGING_CONFIG
uvicorn_logging_config["formatters"]["access"][
    "fmt"
] = "[%(asctime)s][%(levelname)s] %(message)s"
uvicorn_logging_config["formatters"]["default"][
    "fmt"
] = "[%(asctime)s][%(levelname)s] %(message)s"

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=settings.host,
        port=settings.port,
        log_config=uvicorn_logging_config,
        use_colors=True,
        reload=settings.debug,
        workers=settings.worcers_count,
    )
