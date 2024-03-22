#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    from models.engine.db_storage import DBStorage
    if type(models.storage) is not DBStorage:
        name = ""

        @property
        def cities(self):
            """
            return the list of City objects from storage
            linked to the current State
            """
            return models.storage.get_cities_by_state_id(self.id)
    else:
        __tablename__ = "states"
        name = Column("name", String(128), nullable=False)
        cities = relationship(
                "City",
                cascade="all,delete",
                back_populates="state")
