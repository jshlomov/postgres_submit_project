from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base


class Industry(Base):
    __tablename__ = 'industries'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    targets = relationship('Target', back_populates='industry')
