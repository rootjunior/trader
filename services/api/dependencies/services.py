from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from container import Container
from services import TransactionService, UserService


@inject
async def s_user(
    instance: UserService = Depends(Provide[Container.user_service]),
) -> UserService:
    return instance


@inject
async def s_transaction(
    instance: TransactionService = Depends(
        Provide[Container.transaction_service]
    ),
) -> TransactionService:
    return instance
