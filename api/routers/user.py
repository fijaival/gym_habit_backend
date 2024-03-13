from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.user as user_crud
from api.db import get_db
from api.schemas import user as user_schema

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "fewafewa"}

#ユーザー作成
@router.post("/users", response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_crud.create_user(db, user_body)

#全ユーザー取得
@router.get("/users", response_model=List[user_schema.User])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await user_crud.get_users(db)


#ユーザー１人取得
@router.get("/users/{user_id}", response_model=user_schema.User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_crud.get_user(db, user_id)
