from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base

class CheckIn(Base):
    __tablename__ = "check_ins"

    check_in_id = Column(Integer, primary_key=True)
    user_gym_id = Column(Integer, ForeignKey("user_gyms.id"))
    status = Column(Boolean)

    user_gym = relationship("UserGym", back_populates="check_ins")
