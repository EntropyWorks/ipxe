from flask import Flask
from flask.ext import restful

from .models import db, Server

app = Flask(__name__)
app.config.from_object('config')

db.app = app
db.init_app(app)

rest_api = restful.Api(app)

from .api import ServerAPI, ServerListAPI

rest_api.add_resource(ServerAPI, '/servers/<mac_address>', endpoint='server')
rest_api.add_resource(ServerListAPI, '/servers', endpoint='servers')
