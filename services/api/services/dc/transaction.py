from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class TransactionDTO:
    id: int
    uid: UUID
    timestamp: datetime
    transaction_type: str
    amount: float
    user_id: int
