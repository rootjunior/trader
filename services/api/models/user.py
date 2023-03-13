from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    name: str
    balance: float

    class Config:
        orm_mode = True


class UserInModel(BaseModel):
    name: str
