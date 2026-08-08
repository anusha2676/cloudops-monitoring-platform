from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from app.database import Base


class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    disk_usage = Column(Float)
    bytes_sent = Column(Integer)
    bytes_received = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_type = Column(String)
    severity = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="active")


class HealingEvent(Base):
    __tablename__ = "healing_events"

    id = Column(Integer, primary_key=True, index=True)
    problem = Column(String)
    action = Column(String)
    result = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
