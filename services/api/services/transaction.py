from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from db import Transaction

from .dc import TransactionDTO
from .general import CRUD
from .user import UserService


class TransactionService:
    crud: CRUD
    table: Transaction
    user_service: UserService

    def __init__(
        self, crud: CRUD, table: Transaction, user_service: UserService
    ) -> None:
        self.crud = crud
        self.table = table
        self.user_service = user_service

    async def process_transaction(
        self,
        session: AsyncSession,
        transaction_type: str,
        amount: float,
        uid: UUID,
        timestamp: datetime,
        user_id: int,
    ) -> TransactionDTO:
        await self.user_service.update_user_balance(
            session,
            transaction_type=transaction_type,
            amount=amount,
            user_id=user_id,
        )

        obg = await self.crud.insert(
            session,
            self.table,
            transaction_type=transaction_type,
            amount=amount,
            uid=uid,
            user_id=user_id,
            timestamp=timestamp,
        )

        return TransactionDTO(
            id=obg.id,
            uid=obg.uid,
            transaction_type=obg.transaction_type,
            timestamp=obg.timestamp,
            amount=obg.amount,
            user_id=obg.user_id,
        )
