from itertools import chain
from typing import Any, Generator, List, Tuple, Type, Union

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import RelationshipProperty, joinedload
from sqlalchemy.sql.functions import count

from db import Base


class CRUD:
    @classmethod
    async def insert(
        cls,
        session: AsyncSession,
        table: Base,
        *args,
        **kwargs,
    ) -> Base:
        db_item = table(*args, **kwargs)
        session.add(db_item)
        await session.flush()
        return db_item

    @staticmethod
    async def insert_bulk(
        session: AsyncSession,
        items: Union[Generator, List],
        bulk: int = 200,
    ) -> None:
        i, buf = 1, []
        for item in items:
            if i <= bulk:
                buf.append(item)
                i += 1
            else:
                session.add_all(buf)
                if len(buf) != 0:
                    await session.flush()
                i, buf = 1, []

        if len(buf) != 0:
            session.add_all(buf)
            await session.flush()

    @classmethod
    async def values_list(
        cls,
        session: AsyncSession,
        table: Base,
        where: Any,
        fields: List[Any] = None,
        limit: int = 20,
        offset: int = 0,
        join: Tuple[RelationshipProperty, ...] = None,
        flat: bool = False,
    ) -> List[Any]:
        selectable = select(fields) if fields else select(table)

        ordering = table.id.desc() if hasattr(table, "id") else None

        query = selectable.order_by(ordering).limit(limit).offset(offset)
        if where is not None:
            query = query.where(where)
        if join is not None:
            for relation in join:
                query = query.options(joinedload(relation))
        sa_result = await session.execute(query)

        query_result = sa_result if join is None else sa_result.unique()
        if flat:
            return list(chain.from_iterable(query_result))
        return [_ for _ in query_result]

    @classmethod
    async def list(
        cls,
        session: AsyncSession,
        table: Base,
        limit: int = 20,
        offset: int = 0,
        where: Any = None,
        join: Tuple[RelationshipProperty, ...] = None,
    ) -> List:
        items = await cls.values_list(
            session=session,
            table=table,
            limit=limit,
            offset=offset,
            where=where,
            join=join,
        )
        return [_[0] for _ in items]

    @classmethod
    async def count(table, session: AsyncSession, where: Any = None) -> int:
        query = select(count("*")).select_from(table)
        if where is not None:
            query = query.where(where)
        return await session.scalar(query)

    @classmethod
    async def retrieve(
        cls,
        session: AsyncSession,
        table: Base,
        where: Any = None,
        join: Tuple[RelationshipProperty, ...] = None,
    ) -> Type["Base"]:
        result = await cls.list(
            session, table=table, limit=1, where=where, join=join
        )
        return result[0] if result else None

    @classmethod
    async def update(
        cls,
        session: AsyncSession,
        table: Base,
        where: Any = None,
        **kwargs,
    ):
        result = (
            await session.execute(
                update(table).where(where).values(**kwargs).returning(table)
            )
        ).first()
        await session.flush()
        return result

    @classmethod
    async def delete(
        cls,
        session: AsyncSession,
        table: Base,
        where: Any = None,
    ) -> None:
        await session.execute(delete(table).where(where).returning(table))
        await session.flush()
