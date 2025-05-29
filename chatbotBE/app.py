from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

# FastAPI 앱 생성
app = FastAPI()

# CORS 설정
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # CORS 허용 origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# SQLite 설정
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(basedir, 'chat.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 모델 정의
class ChatLog(Base):
    __tablename__ = "chat_log"

    id = Column(Integer, primary_key=True, index=True)
    user_message = Column(String, nullable=False)
    bot_response = Column(String, nullable=False)


# 테이블 생성
Base.metadata.create_all(bind=engine)


# 요청 스키마
class MessageRequest(BaseModel):
    message: str


# API 엔드포인트
@app.post("/chat")
async def chat(request: MessageRequest):
    user_input = request.message
    response_text = f"'{user_input}'에 대한 응답입니다 (예시)"

    # DB 저장
    db = SessionLocal()
    chat_log = ChatLog(user_message=user_input, bot_response=response_text)
    db.add(chat_log)
    db.commit()
    db.close()

    return {"response": response_text}