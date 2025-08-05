from sqlalchemy import Column, BigInteger, DateTime, Integer, String
from datetime import datetime

from core.database import Base

class User(Base):
    __tablename__ = "users"
    id_tg = Column(BigInteger, primary_key=True, index=True)
    username = Column(String(255), nullable=True)
    first_activity = Column(DateTime, default=datetime.utcnow)
    last_activity = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    total_activity = Column(Integer, default=1)
