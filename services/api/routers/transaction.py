from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session
from dependencies import s_transaction
from models import TransactionInModel, TransactionModel
from services import TransactionDTO, TransactionService

router = APIRouter()


@router.post("/", response_model=TransactionModel, status_code=201)
async def create_transaction(
    payload: TransactionInModel,
    session: AsyncSession = Depends(get_async_session),
    service: TransactionService = Depends(s_transaction),
) -> TransactionDTO:
    return await service.process_transaction(
        session=session,
        transaction_type=payload.transaction_type,
        uid=payload.uid,
        amount=payload.amount,
        user_id=payload.user_id,
        timestamp=payload.timestamp,
    )
