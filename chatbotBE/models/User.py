from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    nickname = Column(String, nullable=False)
    age = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    mbti = Column(String)
    height = Column(Integer)
    income = Column(Integer)
    bio = Column(Text)
    image_url = Column(String, nullable=False)

    # 조건부 노출 정보
    user_name = Column(String)
    phone_number = Column(String)
    sns_link = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
