#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.db_storage import DBStorage


class Review(BaseModel, Base):
    """ Review classto store review information """
    if type(models.storage) is DBStorage:
        __tablename__ = 'reviews'
        place_id = Column('place_id', ForeignKey('places.id'), nullable=False)
        user_id = Column('user_id', ForeignKey('users.id'), nullable=False)
        text = Column('text', String(1024), nullable=False)
        user = relationship('User', back_populates='reviews')
        place = relationship('Place', back_populates='reviews')
    else:
        place_id = ""
        user_id = ""
        text = ""
