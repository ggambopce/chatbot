from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from chatbotBE.db.database import get_db
from chatbotBE.models.user import User
from chatbotBE.schemas.user_schema import UserCreateRequest, UserResponse

router = APIRouter()

@router.post("/api/matcher/profile", response_model=UserResponse)
def create_profile(request: UserCreateRequest, db: Session = Depends(get_db)):
    user = User(**request.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
