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

        @property
        def state(self):
            """state property getter"""
            from models import storage
            from models.state import State
            states = list(
                    filter(
                        lambda state: state.id == self.state_id,
                        storage.all(State).values()))
            if states:
                return states[0]
            return None

        @property
        def places(self):
            """places property getter"""
            from models import storage
            from models.place import Place
            return list(
                    filter(
                        lambda place: place.city_id == self.id,
                        storage.all(Place).values()))

    def __init__(self, *args, **kwargs):
        """initialize"""
        super().__init__(*args, **kwargs)
