#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column('place_id', ForeignKey('places.id'), nullable=False)
    user_id = Column('user_id', ForeignKey('users.id'), nullable=False)
    text = Column('text', String(1024), nullable=True)
    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')
