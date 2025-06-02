from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from chatbotBE.db.database import get_db
from chatbotBE.schemas.survey_schema import QuestionSchema, SurveySubmission
from chatbotBE.repositories import survey_repository
from chatbotBE.services import survey_service

router = APIRouter(prefix="/survey", tags=["Survey"])

@router.get("/questions", response_model=list[QuestionSchema])
def fetch_questions(db: Session = Depends(get_db)):
    return survey_repository.get_all_questions(db)

@router.post("/submit")
def submit_survey(submission: SurveySubmission, db: Session = Depends(get_db)):
    result = survey_service.analyze_survey(submission, db)
    return result
