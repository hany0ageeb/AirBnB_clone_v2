#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if type(models.storage) is DBStorage:
        __tablename__ = "cities"
        state_id = Column(
                "state_id",
                ForeignKey("states.id"),
                nullable=False)
        name = Column(
                "name",
                String(128),
                nullable=False)
        state = relationship(
                'State',
                back_populates="cities")
        places = relationship(
                'Place',
                back_populates='city',
                cascade='all,delete')
    else:
        state_id = ""
        name = ""
