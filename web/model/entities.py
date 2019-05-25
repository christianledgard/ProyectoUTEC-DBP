from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Users(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    name = Column(String(50))
    lastNamePaterno = Column(String(50))
    lastNameMaterno = Column(String(50))
    email = Column(String(50))
    club = Column(String(25))
    sailNumber = Column(String(15))


"""
class EmergencyContact(connector.Manager.Base):
    __tablename__ = 'emergencyContact'
    id = Column(Integer, Sequence('message_id_seq'), primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, foreign_keys=[user_id])
"""
