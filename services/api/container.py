from dependency_injector import containers, providers

from db import Transaction, User
from services import CRUD, TransactionService, UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["routers", "dependencies"],
    )
    config = providers.Configuration(strict=True)

    user_service = providers.Singleton(UserService, table=User, crud=CRUD)
    transaction_service = providers.Singleton(
        TransactionService,
        user_service=user_service,
        table=Transaction,
        crud=CRUD,
    )
