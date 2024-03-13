from typing import Union

from fastapi import FastAPI

from api.routers import user, check_in, gym, user_gym

app = FastAPI()

app.include_router(user.router)