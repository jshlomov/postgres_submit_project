from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    cities = relationship('City', back_populates='country')
