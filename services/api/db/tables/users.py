from sqlalchemy import FLOAT, Column, String
from sqlalchemy.orm import relationship

from .bases import Base


class User(Base):
    __tablename__ = "users_table"
    __table_args__ = {"extend_existing": True}

    name = Column(String, nullable=False)
    balance = Column(FLOAT, nullable=False, default=0)

    transactions = relationship("Transaction", backref="user")
