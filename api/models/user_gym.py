from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base

class UserGym(Base):
    __tablename__ = "user_gyms"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    gym_id = Column(Integer, ForeignKey("gyms.gym_id"))
    date = Column(Date)
    fine_amount = Column(Integer)

    # user = relationship("User", back_populates="user_gyms")
    # gym = relationship("Gym", back_populates="user_gyms")
    check_ins = relationship("CheckIn", back_populates="user_gym")

class CheckIn(Base):
    __tablename__ = "check_ins"

    check_in_id = Column(Integer, primary_key=True)
    user_gym_id = Column(Integer, ForeignKey("user_gyms.id"))
    status = Column(Boolean)

    user_gym = relationship("UserGym", back_populates="check_ins")