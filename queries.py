from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///actor_roles.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_christian_bales_roles(session):
    return session.query(Actor).filter_by(name='Christian Bale')[0].roles

def return_catwoman_actors(session):
    return session.query(Role).filter_by(character='Catwoman')[0].actors

def return_number_of_batman_actors(session):
    return len(session.query(Role).filter_by(character='Batman')[0].actors)
