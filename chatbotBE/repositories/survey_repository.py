from sqlalchemy.orm import Session
from chatbotBE.models.survey import Question, Answer

def get_all_questions(db: Session):
    return db.query(Question).all()

def get_answers_by_question_id(db: Session, question_id: int):
    return db.query(Answer).filter(Answer.question_id == question_id).all()
