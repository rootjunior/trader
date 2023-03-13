import datetime

from sqlalchemy import FLOAT, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from settings import settings

from .bases import Base


class Transaction(Base):
    __tablename__ = "transactions_table"
    __table_args__ = {"extend_existing": True}

    uid = Column(UUID(as_uuid=True), unique=True, nullable=False)
    transaction_type = Column(String, nullable=False)
    amount = Column(FLOAT, nullable=False, default=0)
    timestamp = Column(
        DateTime(settings.use_timezone),
        default=datetime.datetime.utcnow,
        nullable=False,
    )

    user_id = Column(
        ForeignKey("users_table.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
