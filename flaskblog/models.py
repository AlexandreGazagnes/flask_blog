from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db, login_manager
from flask_login import UserMixin
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    """load an user when logged"""

    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """table User"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), unique=False, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_toke(self, expire_sec=15 * 60):
        s = Serializer(current_app.config['SECRET_KEY'], expire_sec)
        return s.dumps({'user_id': self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except Exception as e:
            return None
        return User.query.get(user_id)

    def __repr__(self):

        return f"user({self.id}, {self.username}, {self.email}, {self.image_file})"


class Post(db.Model, UserMixin):
    """table Post"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
