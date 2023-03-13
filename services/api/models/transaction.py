from datetime import datetime

from pydantic import BaseModel
from pydantic.types import UUID4


class TransactionModel(BaseModel):
    id: int
    uid: UUID4
    timestamp: datetime
    transaction_type: str
    amount: float
    user_id: int


class TransactionInModel(BaseModel):
    uid: UUID4
    timestamp: datetime
    transaction_type: str
    amount: float
    user_id: int
