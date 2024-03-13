from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import api.models.user as user_model
import api.schemas.user as user_schema

#ユーザー作成
async def create_user(db:AsyncSession, user_create: user_schema.UserCreate) -> user_model.User:
    user = user_model.User(**user_create.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

#全ユーザー取得
async def get_users(db:AsyncSession) -> list[user_model.User]:
    result = await (db.execute(select(user_model.User.id,user_model.User.email,user_model.User.password)))
    return result.all()

#ユーザー１人取得
async def get_user(db:AsyncSession, user_id: int) -> user_model.User:
    result = await (db.execute(select(user_model.User.id,user_model.User.email,user_model.User.password).filter(user_model.User.id == user_id)))
    return result.first()