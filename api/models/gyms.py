from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from api.db import Base

class Gym(Base):
    __tablename__ = "gyms"

    gym_id = Column(Integer, primary_key=True)
    gym_name = Column(String(1024))
    latitude = Column(Float)
    longitude = Column(Float)
    user_gyms = relationship("UserGym", back_populates="gym")