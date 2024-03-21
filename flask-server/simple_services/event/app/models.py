from sqlalchemy import Column, Integer, TIMESTAMP, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Event(Base):
    __tablename__ = 'event'
    event_id = Column(Integer, primary_key=True)
    event_name = Column(String(64), nullable=False)
    event_desc = Column(String(256), nullable=True)
    start_time = Column(TIMESTAMP, nullable=True)
    end_time = Column(TIMESTAMP, nullable=True)
    time_out = Column(TIMESTAMP, nullable=True)
    event_location = Column(String(64), nullable=True)
    user_id = Column(Integer, nullable=False)
    
    recommendation = relationship("Recommendation", back_populates="event")

  

class Invitee(Base):
    __tablename__ = 'invitee'
    event_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, primary_key=True, nullable=False)
    status = Column(String(64), nullable=True)

class Recommendation(Base):
    __tablename__ = 'recommendation'
    recommendation_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    recommendation_name = Column(String(64), nullable=False)
    recommendation_address = Column(String(64), nullable=False)
    event_id = Column(Integer, ForeignKey('event.event_id'), nullable=False)

    event = relationship("Event", back_populates="recommendation")

