from flask import Flask
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


def create_db():
    #url of the database
    db_url = 'sqlite:///database.db'
    
    engine = create_engine(db_url)
    
    #specify the base class for all the models
    Base = declarative_base()
    
    #create a table for the users
    class User(Base):
        __tablename__ = 'users'
        
        id = Column(Integer, primary_key=True)
        username = Column(String, unique=True)
        password = Column(String)
    
    #create database
    Base.metadata.create_all(engine)
    
    return engine, Base