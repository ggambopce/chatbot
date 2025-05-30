from sqlalchemy.orm import Session
from chatbotBE.schemas.survey_schema import SurveySubmission
from chatbotBE.models.survey import Answer

def analyze_survey(submission: SurveySubmission, db: Session):
    result_labels = []

    for ans in submission.answers:
        answer = db.query(Answer).filter(Answer.id == ans.answer_id).first()
        if answer:
            result_labels.append(answer.label)

    # TODO: 성향 분석 로직 구현
    result = {
        "user_id": submission.user_id,
        "labels": result_labels,
        "inferred_type": "분석 결과 예시: ENNEA 4w5 / Explorer"
    }

    return result
