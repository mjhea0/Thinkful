from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship, backref


engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    item_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class User(object):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    items = relationship("Item", backref="user")
    bids = relationship("Bid", backref="user")
    user_id = Column(Integer, ForeignKey('bid.id'), nullable=False)


class Bid():
    __tablename__ = "bid"

    id = Column(Integer, primary_key=True)
    price_point = (Integer, nullable=False)
    user = relationship("User", backref="bid")
    bid_id = Column(Integer, ForeignKey("user.id"), nullable=False)

Base.metadata.create_all(engine)
