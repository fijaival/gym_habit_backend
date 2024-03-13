from sqlalchemy import create_engine
from api.db import Base  # Baseインポートの更新
from api.models.user import User  
from api.models.gym import Gym  
from api.models.user_gym import UserGym,CheckIn


# from app.models.users import Base

DB_URL = "mysql+pymysql://root@db:3306/gym?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()