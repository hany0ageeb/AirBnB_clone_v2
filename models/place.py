#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False),
        Column(
            'amenity_id',
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column('city_id', ForeignKey('cities.id'), nullable=False)
    user_id = Column('user_id', ForeignKey('users.id'), nullable=False)
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024), nullable=True)
    number_rooms = Column('number_rooms', Integer, nullable=False, default=0)
    number_bathrooms = Column(
            'number_bathrooms',
            Integer,
            nullable=False,
            default=0)
    max_guest = Column('max_guest', Integer, nullable=False, default=0)
    price_by_night = Column(
            'price_by_night',
            Integer,
            nullable=False,
            default=0)
    latitude = Column('latitude', Float, nullable=True)
    longitude = Column('longitude', Float, nullable=True)
    user = relationship('User', back_populates='places')
    city = relationship('City', back_populates='places')
    reviews = relationship(
            'Review',
            back_populates='place',
            cascade='all,delete')
    amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            back_populates='place_amenities',
            viewonly=False)
    amenity_ids = []
