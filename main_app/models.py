from main_app import db
from datetime import datetime


class TestLog(db.Model):
    __tablename__ = "TestLog"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=True)
    value = db.Column(db.String(255), nullable=True)
    createDateTime = db.Column(
        db.DateTime, nullable=True, default=datetime.utcnow)
