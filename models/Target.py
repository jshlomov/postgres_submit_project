from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base


class Target(Base):
    __tablename__ = 'targets'

    id = Column(Integer, primary_key=True)
    target_id = Column(String(100))
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('target_types.id'))
    target_industry_id = Column(Integer, ForeignKey('industries.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))
    priority = Column(String(10))

    city = relationship('City', back_populates='targets')
    target_type = relationship('TargetType', back_populates='targets')
    industry = relationship('Industry', back_populates='targets')
    location = relationship('Location', back_populates='targets')
