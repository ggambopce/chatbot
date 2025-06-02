from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
import os

# 환경변수 로드
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

from chatbotBE.routes.survey_routes import router as survey_router
from chatbotBE.routes.chatgpt import router as chatgpt_router
from chatbotBE.routes.profile_routes import router as profile_router
from chatbotBE.db.database import init_db



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

# DB 초기화
init_db()

# 라우터 등록
app.include_router(chatgpt_router)
app.include_router(profile_router)
app.include_router(survey_router)


# # 모델 정의
# class ChatLog(Base):
#     __tablename__ = "chat_log"

#     id = Column(Integer, primary_key=True, index=True)
#     user_message = Column(String, nullable=False)
#     bot_response = Column(String, nullable=False)


# # 테이블 생성
# Base.metadata.create_all(bind=engine)


# # 요청 스키마
# class MessageRequest(BaseModel):
#     message: str


# # API 엔드포인트
# @app.post("/chat")
# async def chat(request: MessageRequest):
#     user_input = request.message
#     response_text = f"'{user_input}'에 대한 응답입니다 (예시)"

#     # DB 저장
#     db = SessionLocal()
#     chat_log = ChatLog(user_message=user_input, bot_response=response_text)
#     db.add(chat_log)
#     db.commit()
#     db.close()

#     return {"response": response_text}