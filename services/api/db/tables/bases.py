from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative

from db import meta


@as_declarative(metadata=meta)
class Base:
    id = Column(Integer, primary_key=True, autoincrement=True)


@as_declarative(metadata=meta)
class BaseThrough:
    ...
