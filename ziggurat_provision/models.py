import re

from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

MAC_RE = re.compile(r'^([0-9A-F]{2})(:[0-9A-F]{2}){5}$', re.IGNORECASE)

SERVER_STATES = ('IN_USE', 'MAINTENANCE', 'REBUILD')

SERVER_PROFILES = {}


def unix_time(dt):
    epoch = datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return long(delta.total_seconds())


def unix_time_millis(dt):
    return long(unix_time(dt) * 1000.0)


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

        is_valid = (Server.validate_mac_address(self.mac_address) and
                    Server.validate_server_profile(self.profile) and
                    Server.validate_server_state(self.state))

        if not is_valid: raise ValueError("invalid values passed...")

    def serialize(self):
        return {
            u"mac_address": self.mac_address,
            u"hostname": self.hostname,
            u"profile": self.profile,
            u"state": self.state,
            u"created_at": unix_time(self.created_at),
            u"updated_at": unix_time(self.updated_at)
        }

    @staticmethod
    def validate_mac_address(mac_address):
        #mac_address = mac_address.replace('-', ':')
        matches = MAC_RE.match(mac_address)
        return True if matches else False

    @staticmethod
    def validate_server_profile(profile):
        return True if profile in SERVER_PROFILES.keys() else False

    @staticmethod
    def validate_server_state(state):
        return True if state in SERVER_STATES else False

    def __repr__(self):
        return '<Server %r>' % self.mac_address
