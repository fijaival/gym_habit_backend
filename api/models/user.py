from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from api.db import Base

from api.models.user_gym import UserGym

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(1024))
    password = Column(String(1024))

    user_gyms = relationship("UserGym", backref="user")

    
    