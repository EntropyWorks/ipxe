import os

current_dir = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/2.db' % current_dir
SQLALCHEMY_ECHO = True

WTF_CSRF_ENABLED = True
