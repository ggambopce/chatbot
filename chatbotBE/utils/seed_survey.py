from chatbotBE.db.database import SessionLocal
from chatbotBE.models.survey import Question, Answer


def seed_survey():
    db = SessionLocal()

    survey_data = [
        {
            "number": 1,
            "text": "당신이 좋아하는 데이트 스타일은?",
            "answers": [
                ("새로운 곳 탐험! 즉흥 여행! 🌍", "Curious/Energetic"),
                ("단골 카페, 계획된 데이트 ☕", "Cautious/Social Norm Compliant"),
                ("지적인 대화, 독특한 체험 🧩", "Analytical/Tough-minded"),
                ("감성적인 밤 산책, 깊은 대화 🌙", "Prosocial/Empathetic"),
            ]
        },
        {
            "number": 2,
            "text": "연인에게 가장 중요한 건 무엇인가요?",
            "answers": [
                ("함께 성장하고 성취하기 🏆", "3,7"),
                ("서로 돌보고 의지하기 💞", "2,6"),
                ("특별하고 강렬한 감정 공유 🔥", "4,5"),
                ("평화롭고 안정된 일상 🛋️", "1,9"),
                ("믿음직한 리더십, 주도권 💪", "8"),
            ]
        },
        {
            "number": 3,
            "text": "다툼이 생겼을 때 당신의 반응은?",
            "answers": [
                ("먼저 풀자고 다가가 대화한다 🤝", "high_dev"),
                ("원칙이나 논리로 설득한다 📏", "mid_dev"),
                ("속으로 삭이거나 피한다 🕳️", "low_dev"),
            ]
        },
        {
            "number": 4,
            "text": "평소에 가장 신경 쓰는 건 무엇인가요?",
            "answers": [
                ("내 안전, 건강, 돈 🏠", "self-preservation"),
                ("친구, 모임, 평판 🏢", "social"),
                ("연인, 특별한 사람과의 관계 ❤️", "one-to-one"),
            ]
        },
        {
            "number": 5,
            "text": "당신의 가장 큰 두려움은?",
            "answers": [
                ("틀림, 잘못됨 ❗", "1"),
                ("사랑받지 못함 💔", "2"),
                ("실패, 무가치함 🥀", "3"),
                ("평범함, 상실감 🌊", "4"),
                ("무능, 무지 🤯", "5"),
                ("혼돈, 배신 ⚡", "6"),
                ("구속, 지루함 🎭", "7"),
                ("약함, 통제 상실 🛡️", "8"),
                ("갈등, 불협화음 🌫️", "9"),
            ]
        },
        {
            "number": 6,
            "text": "당신에게 더 가까운 성향은? (양날개 감별)",
            "answers": [
                ("강단 있고 단호한 성격 💥", "8w"),
                ("원칙적이고 꼼꼼한 성격 📜", "1w"),
                ("감정에 솔직하고 따뜻한 성격 💓", "2w,4w"),
                ("분석적이고 냉철한 성격 🧠", "5w,6w,7w"),
            ]
        },
    ]

    for item in survey_data:
        q = Question(number=item["number"], text=item["text"])
        db.add(q)
        db.flush()  # q.id 생성 후 answers에 참조 가능
        for answer_text, label in item["answers"]:
            db.add(Answer(text=answer_text, label=label, question_id=q.id))

    db.commit()
    db.close()

if __name__ == "__main__":
    seed_survey()
