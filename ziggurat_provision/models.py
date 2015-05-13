import re

from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy

from .content import SERVER_PROFILES, SERVER_STATES

db = SQLAlchemy()


class Server(db.Model):
    mac_address = db.Column(db.String(17), primary_key=True)
    hostname = db.Column(db.String(255), nullable=False, unique=True)
    profile = db.Column(db.String(64), nullable=False)
    state = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(),
                           nullable=False)

    __table_args__ = (db.CheckConstraint(state.in_(SERVER_STATES)),)

    def __init__(self, mac_address=None, hostname=None, state=None,
                 profile=None, created_at=datetime.utcnow(),
                 updated_at=datetime.utcnow()):
        self.mac_address = mac_address
        self.hostname = hostname
        self.state = state
        self.profile = profile
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<Server %r>' % self.mac_address
