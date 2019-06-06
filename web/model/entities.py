from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Users(connector.Manager.Base):
    __tablename__ = 'Users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
    password = Column(String(80))
    email = Column(String(50), unique=True)


"""
class EmergencyContact(connector.Manager.Base):
    __tablename__ = 'emergencyContact'
    id = Column(Integer, Sequence('message_id_seq'), primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, foreign_keys=[user_id])
"""
