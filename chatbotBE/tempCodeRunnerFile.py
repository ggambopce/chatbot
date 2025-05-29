from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, ChatLog
from flask_cors import CORS
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# SQLite 설정
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'chat.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 서버 시작 전 최초 한 번만 테이블 생성
@app.before_first_request
def create_tables():
    db.create_all()

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
    app.run(debug=True, port=5000)

