from __future__ import annotations

import os
import sys
from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship, declarative_base, Mapped
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


user_planet_favorite = Table(
    "UserPlanetFavorite",
    Base.metadata,
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("planet_id", ForeignKey("Planet.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    favorites: Mapped[List[Planet]] = relationship("Planet", secondary=user_planet_favorite)

class Planet(Base):
    __tablename__ = "Planet"

    id = Column(Integer, primary_key=True)
    population = Column(Integer,nullable=False)
    climate = Column(String, nullable=False)
    surface_water_percentage = Column(String, nullable=False)
    radius = Column(Float, nullable=False)
    gravity = Column(Float, nullable=False)
    favorites: Mapped[List[User]] = relationship("User", secondary=user_planet_favorite)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')