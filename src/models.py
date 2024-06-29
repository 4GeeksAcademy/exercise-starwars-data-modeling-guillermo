import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Date, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    population = Column(Integer, nullable=False)
    climate = Column(Enum("arid", "temperate", "tropical", "frozen", "murky"), nullable=False)
    name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    date = Column(Date, default=func.current_date(), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    
    favorites = relationship("Favorite", back_populates="user")

class Favorite(Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    
    user = relationship("User", back_populates="favorites")
    character = relationship("Character")
    planet = relationship("Planet")

class Character(Base):
    __tablename__ = 'character'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(50))
    gender = Column(String(50))

    def to_dict(self):
        return {}

# Generate ER diagram
render_er(Base, 'diagram.png')
