from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:1234@Localhost/pdp_p16", echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


class User_chat(Base):
    __tablename__ = 'userchat'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True)
    username = Column(String)
    created = Column(DateTime)


class User_message(Base):
    __tablename__ = 'usermessage'
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    colum_message = Column(String)
    created = Column(DateTime)


Base.metadata.create_all(engine)

Base = declarative_base()
metadata = Base.metadata
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_teg_id = Column(String, unique=True)
    username = Column(String)
    created = Column(DateTime)
    messages = relationship("Message", back_populates="user")


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    text = Column(String())
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="messages")


Base.metadata.create_all(engine)
