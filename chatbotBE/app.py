from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, ChatLog
from flask_cors import CORS
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
# CORS 설정
CORS(app, resources={r"/chat": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500"]}})


# SQLite 설정
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'chat.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB 초기화
db.init_app(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # TODO: RAG + GPT 연동으로 응답 생성
    response_text = f"'{user_input}'에 대한 응답입니다 (예시)"
    
    # DB 저장
    chat_log = ChatLog(user_message=user_input, bot_response=response_text)
    db.session.add(chat_log)
    db.session.commit()
    return jsonify({'response': response_text})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)

