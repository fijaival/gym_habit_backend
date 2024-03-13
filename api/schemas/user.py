from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

class UserBase(BaseModel):
    email: str = Field(None, max_length=1024)
    password: str = Field(None, max_length=1024)


class UserCreate(UserBase):
    pass

class UserCreateResponse(UserCreate):
    id: int

    model_config = ConfigDict(orm_mode=True)

class User(UserBase):
    id: int
    
    model_config = ConfigDict(orm_mode=True)