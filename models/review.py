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

        @property
        def user(self):
            """user property getter"""
            from models import storage
            from models.user import User
            users = list(
                    filter(
                        lambda usr: user.id == self.user_id,
                        storage.all(User).values()))
            if users:
                return users[0]
            return None

        @property
        def place(self):
            """place property getter"""
            from models import storage
            from models.place import Place
            places = list(
                    filter(
                        lambda plc: plac.id == self.place_id,
                        storage.all(Place).values()))
            if places:
                return places[0]
            return None

    def __init__(self, *args, **kwargs):
        """Initialize Review"""
        super().__init__(*args, **kwargs)
