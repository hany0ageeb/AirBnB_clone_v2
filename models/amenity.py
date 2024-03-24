#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class"""
    if type(models.storage) is DBStorage:
        from models.place import place_amenity
        __tablename__ = 'amenities'
        name = Column('name', String(128), nullable=False)
        place_amenities = relationship(
                'Place',
                secondary=place_amenity,
                back_populates='amenities')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity"""
        super().__init__(*args, **kwargs)
