from pydantic import BaseModel
from typing import List

class AnswerSchema(BaseModel):
    id: int
    text: str
    label: str

    class Config:
        orm_mode = True

class QuestionSchema(BaseModel):
    id: int
    number: int
    text: str
    answers: List[AnswerSchema]

    class Config:
        orm_mode = True

class AnswerSubmission(BaseModel):
    question_id: int
    answer_id: int

class SurveySubmission(BaseModel):
    user_id: str
    answers: List[AnswerSubmission]
