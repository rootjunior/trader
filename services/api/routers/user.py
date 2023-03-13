from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session
from dependencies import s_user
from models import UserInModel, UserModel
from services import UserDTO, UserService

router = APIRouter()


@router.post("/", response_model=UserModel, status_code=201)
async def create_user(
    payload: UserInModel,
    session: AsyncSession = Depends(get_async_session),
    service: UserService = Depends(s_user),
) -> UserDTO:
    return await service.create_user(session=session, name=payload.name)
