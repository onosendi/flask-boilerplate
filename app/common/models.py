from datetime import datetime
from typing import Union

from app.common.extensions import db


class BaseMixin:
    id = db.Column(db.Integer, primary_key=True)

    def commit(self) -> Union[object, None]:
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as Error:
            db.session.rollback()
            raise Error


class SoftDeleteMixin:
    active = db.Column(db.Boolean, default=True, nullable=False)
    deleted = db.Column(db.DateTime)

    def delete(self) -> None:
        self.active = False
        self.deleted = datetime.utcnow()


class TimestampMixin:
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow, nullable=False)
