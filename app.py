from flask import Flask, render_template
from flask_login import LoginManager, current_user
from auth import login_manager
from custom_socketio import SocketIO, emit, join_room, leave_room

from database import db
from auth import login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam.db'
db.init_app(app)
login_manager.init_app(app)
SocketIO.init_app(app)

# Import your models
from auth import User
from database import Exam, Question, UserExam

# Import your views
from auth import auth_bp
from custom_socketio import SocketIO, emit, join_room, leave_room

app.register_blueprint(auth_bp)
app.register_blueprint(socketio_bp)

# Define routes and views
@app.route('/')
def index():
    return render_template('index.html')

# Implement other routes...

if __name__ == '__main__':
    SocketIO.run(app, debug=True)
