from fastapi import FastAPI

from routers import transaction_touter, user_router


def setup_routers(app: FastAPI) -> None:
    app.include_router(user_router, prefix="/v1/user", tags=["Users"])
    app.include_router(
        transaction_touter, prefix="/v1/transaction", tags=["Transactions"]
    )
