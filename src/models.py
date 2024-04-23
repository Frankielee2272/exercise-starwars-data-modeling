import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from typing import List

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

user_planet_favorite = Table(
    "user_planet_favorite", 
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id")),
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    population = Column(Integer, nullable=False)
    climate = Column(String, nullable=False)
    surface_water = Column(Float, nullable=False)
    gravity = Column(Float, nullable=False)

    user_planet_favorite = Table(
        "user_planet_favorite", 
        Base.metadata,
        Column("user_id", Integer, ForeignKey("user.id")),
        Column("planet_id", Integer, ForeignKey("planet.id"))
    )
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    climate = Column(String, nullable=False)
    surface_water = Column(Float, nullable=False)
    gravity = Column(Float, nullable=False)
    favorites: Mapped[List["User"]] = relationship("User", secondary=user_planet_favorite)
    surface_water = Column(Float, nullable=False)
    gravity = Column(Float, nullable=False)
    favorites: Mapped[List [User]] = relationship("User", secondary=user_planet_favorite)
    