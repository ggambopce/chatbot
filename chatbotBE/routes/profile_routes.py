from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from chatbotBE.db.database import get_db
from chatbotBE.models.user import User
from chatbotBE.schemas.user_schema import UserCreateRequest, UserResponse
import random

router = APIRouter()

@router.post("/api/matcher/profile", response_model=UserResponse)
def create_profile(request: UserCreateRequest, db: Session = Depends(get_db)):
    user = User(**request.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/api/matcher/random-profile", response_model=UserResponse)
def get_random_profile(db: Session = Depends(get_db)):
    # 전체 수 가져오기
    total = db.query(func.count(User.id)).scalar()
    if total == 0:
        raise HTTPException(status_code=404, detail="No profiles found")

    # 랜덤 인덱스 선택
    offset = random.randint(0, total - 1)

    # 무작위 하나 선택
    random_user = db.query(User).offset(offset).limit(1).first()
    return random_user