from pydantic import BaseModel
from typing import Optional

class UserCreateRequest(BaseModel):
    nickname: str
    age: str
    gender: str
    bio: Optional[str]
    image_url: str

    user_name: Optional[str]
    phone_number: Optional[str]
    sns_link: Optional[str]

class UserResponse(BaseModel):
    id: int
    nickname: str
    age: str
    gender: str
    bio: Optional[str]
    image_url: str
    created_at: str

    class Config:
        orm_mode = True
