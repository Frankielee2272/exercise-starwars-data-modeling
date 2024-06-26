from __future__ import annotations

import os
import sys
from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship, declarative_base, Mapped
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Association Table for Many-to-Many relationship between User and Planet
user_planet_favorite = Table(
    "UserPlanetFavorite",
    Base.metadata,
    Column("user_id", ForeignKey("User.id"), primary_key=True),
    Column("planet_id", ForeignKey("Planet.id"), primary_key=True),
)

# User Model
class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    favorites = relationship("Favorite", back_populates="user")
    starships = relationship("Starship", back_populates="owner")

# Planet Model
class Planet(Base):
    __tablename__ = "Planet"

    id = Column(Integer, primary_key=True)
    population = Column(Integer, nullable=False)
    climate = Column(String, nullable=False)
    surface_water_percentage = Column(Float, nullable=False)
    radius = Column(Float, nullable=False)
    gravity = Column(Float, nullable=False)
    characters = relationship("Character", back_populates="homeworld")

# Starship Model
class Starship(Base):
    __tablename__ = "Starship"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    cost_in_credits = Column(Float, nullable=False)
    capacity = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey('User.id'))
    owner = relationship("User", back_populates="starships")

# Character Model
class Character(Base):
    __tablename__ = "Character"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String)
    gender = Column(String)
    homeworld_id = Column(Integer, ForeignKey('Planet.id'))
    homeworld = relationship("Planet", back_populates="characters")

# Favorite Model
class Favorite(Base):
    __tablename__ = "Favorite"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    character_id = Column(Integer, ForeignKey('Character.id'))
    planet_id = Column(Integer, ForeignKey('Planet.id'))
    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    planet = relationship("Planet")

# Person Model (Updated with correct foreign key)
class Person(Base):
    __tablename__ = "Person"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    home_planet_id = Column(Integer, ForeignKey('Planet.id'))
    home_planet = relationship("Planet")

# Create engine and generate schema diagram
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

render_er(Base, 'diagram.png')
