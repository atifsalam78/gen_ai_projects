from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base

import datetime

class User(Base):
    __tablename__ = "userlogin"
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    user_name = Column(String(50), nullable=False)
    email_id = Column(String(100), nullable=False)
    password = Column(String(50), nullable=False)

class TokenTable(Base):
    __tablename__ = "token"
    user_id = Column(Integer)
    access_toke = Column(String(450), primary_key=True)
    refresh_toke = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)
