from flask import Flask
from flask.ext import restful

app = Flask(__name__)
app.config.from_object('config')

# circular dependency with content if before app
from .models import db, Server

db.app = app
db.init_app(app)

rest_api = restful.Api(app)

# circular dependency if before rest_api
from .api import KickstartAPI, ServerAPI, ServerListAPI
from .api_kickstart import KickstartResource, ServerKickstartResource

# ipxe related endpoints

# kickstart related endpoints
rest_api.add_resource(KickstartResource,
                      '/kickstarts/<profile>',
                      endpoint='kickstart')
rest_api.add_resource(ServerKickstartResource,
                      '/servers/<mac_address>/<profile>',
                      endpoint='server_kickstart')

# server related endpoints
rest_api.add_resource(ServerAPI, '/servers/<mac_address>', endpoint='server')
rest_api.add_resource(ServerListAPI, '/servers', endpoint='servers')
