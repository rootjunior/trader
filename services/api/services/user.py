from sqlalchemy.ext.asyncio import AsyncSession
from starlette.exceptions import HTTPException

from db import TransactionType, User, transaction

from .dc import UserDTO
from .general import CRUD


class UserService:
    crud: CRUD
    table: User

    def __init__(self, crud: CRUD, table: User) -> None:
        self.crud = crud
        self.table = table

    async def create_user(self, session: AsyncSession, name: str) -> UserDTO:
        obj = await self.crud.insert(session, self.table, name=name)
        await session.commit()

        return UserDTO(id=obj.id, name=obj.name, balance=obj.balance)

    async def _get_user_by_id(
        self, session: AsyncSession, user_id: int
    ) -> User:
        obj = await self.crud.retrieve(
            session, table=self.table, where=self.table.id == user_id
        )
        if not obj:
            raise HTTPException(400, f"User ID {user_id} does not exist")
            
        return obj

    async def update_user_balance(
        self, session, transaction_type: str, user_id: int, amount: int
    ) -> None:
        obj = await self._get_user_by_id(session, user_id=user_id)

        async with transaction(session):
            if transaction_type == TransactionType.WITHDRAW:
                if obj.balance - amount >= 0:
                    await self.crud.update(
                        session,
                        table=self.table,
                        balance=obj.balance - amount,
                        where=self.table.id == user_id,
                    )
                else:
                    raise HTTPException(
                        400,
                        f"There are not enough funds on the balance to carry out the operation",
                    )
            else:
                await self.crud.update(
                    session,
                    table=self.table,
                    balance=obj.balance + amount,
                    where=self.table.id == user_id,
                )
