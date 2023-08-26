from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

login_manager = LoginManager()
jwt = JWTManager()

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    # Load the user from the database by id
    return User.query.get(int(user_id))

def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        login_user(user)
        return True
    return False

def logout():
    logout_user()

# Other authentication related functions can be added here

def generate_access_token(user):
    access_token = create_access_token(identity=user.username)
    return access_token
