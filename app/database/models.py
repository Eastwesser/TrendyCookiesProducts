from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(String, index=True)
    price = Column(Integer, index=True)
    weight = Column(String, index=True)
    image = Column(String, index=True)


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, index=True)
