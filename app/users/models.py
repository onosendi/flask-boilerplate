from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.extensions import db, login
from app.common.models import BaseMixin, SoftDeleteMixin, TimestampMixin


class User(
    UserMixin,
    BaseMixin,
    SoftDeleteMixin,
    TimestampMixin,
    db.Model,
):
    username = db.Column(db.String(35), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        # Set given email address to lowercase.
        email = kwargs.get('email')
        kwargs.update({
            'email': email,
        })
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
