from sqlalchemy import Column, TEXT, INT, BIGINT, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = "test"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(TEXT, nullable=False)
    number = Column(INT, nullable=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    phone_number = Column(String(20))
    gender = Column(Enum('남성', '여성'))
    school = Column(Enum('중학교', '고등학교'))
    password = Column(String(255))