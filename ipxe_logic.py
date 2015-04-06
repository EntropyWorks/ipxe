import re
import sqlite3

from contextlib import contextmanager
from wtforms import Form, BooleanField, TextField, PasswordField, validators

mac_regex = re.compile(r'^([0-9A-F]{2})(\-[0-9A-F]{2}){5}$', re.IGNORECASE)

class ServerForm(Form):
    mac = TextField('MAC Address', [validators.Regexp(regex=mac_regex)])
    hostname = TextField('Hostname', [validators.Length(min=1, max=255)])
    state = TextField('State', [validators.Length(min=1, max=64)])
    profile = TextField('Profile', [validators.Length(min=1, max=64)])

@contextmanager
def db_connection(path):
    connection = sqlite3.connect(path)
    try:
        yield connection
    finally:
        connection.close()

@contextmanager
def db_transaction(connection):
    cursor = connection.cursor()
    try:
        yield cursor
    except:
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        cursor.close()
