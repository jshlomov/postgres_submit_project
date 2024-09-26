from sqlalchemy import Column, Integer, Numeric, UniqueConstraint
from sqlalchemy.orm import relationship

from config.base import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    latitude = Column(Numeric)
    longitude = Column(Numeric)

    __table_args__ = (
        UniqueConstraint('latitude', 'longitude', name='unique_loc'),
    )

    targets = relationship('Target', back_populates='location')
