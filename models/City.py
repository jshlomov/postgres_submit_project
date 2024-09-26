from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from config.base import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)

    __table_args__ = (UniqueConstraint('name', 'country_id', name='unique_city_country'),)

    country = relationship('Country', back_populates='cities')
    targets = relationship('Target', back_populates='city')
