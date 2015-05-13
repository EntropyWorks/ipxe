import os

current_dir = os.path.dirname(os.path.realpath(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/2.db' % current_dir # replace
SQLALCHEMY_ECHO = True
