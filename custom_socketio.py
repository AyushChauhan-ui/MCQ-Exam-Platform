from flask_socketio import SocketIO, emit, join_room, leave_room
from auth import jwt_required, get_jwt_identity
from database import db, Exam, Question

socketio = SocketIO()

@socketio.on('join')
@jwt_required()
def on_join(data):
    exam_id = data['exam_id']
    join_room(exam_id)
    emit('message', f'Welcome, {get_jwt_identity()}!', room=exam_id)

@socketio.on('start')
@jwt_required()
def on_start(data):
    exam_id = data['exam_id']
    questions = Question.query.filter_by(exam_id=exam_id).all()
    # Implement question selection logic
    # Emit the first question to the room

@socketio.on('answer')
@jwt_required()
def on_answer(data):
    exam_id = data['exam_id']
    question_id = data['question_id']
    answer = data['answer']
    # Implement answer validation and scoring logic
    # Emit feedback and next question

@socketio.on('timer')
@jwt_required()
def on_timer(data):
    exam_id = data['exam_id']
    remaining = data['remaining']
    emit('timer', remaining, room=exam_id)
    if remaining == 0:
        # Implement timer expiration logic
        emit('end', 'Time is up!', room=exam_id)

@socketio.on('leave')
@jwt_required()
def on_leave(data):
    exam_id = data['exam_id']
    leave_room(exam_id)
    emit('message', f'Goodbye, {get_jwt_identity()}!', room=exam_id)
