from app.common.extensions import db
from app.common.models import BaseMixin, SoftDeleteMixin, TimestampMixin


class Post(
    BaseMixin,
    SoftDeleteMixin,
    TimestampMixin,
    db.Model,
):
    body = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'<Post {self.body}>'
