from flask import abort, render_template
from flask.ext.restful import Resource

from .content import default_kickstart, SERVER_PROFILES, SERVER_STATES
from .models import db, Server

from .utils import output_plain

class KickstartResource(Resource):
    def __init__(self):
        super(KickstartResource, self).__init__()
        self.representations = {'text/plain': output_plain}

    def get(self, profile):
        return render_template('kickstart/kickstart.j2',
                               kickstart=default_kickstart,
                               profile=profile), 200

class ServerKickstartResource(Resource):
    def __init__(self):
        super(ServerKickstartResource, self).__init__()
        self.representations = {'text/plain': output_plain}

    def get(self, mac_address, profile):
        server = Server.query.get(mac_address)
        if server is None:
            abort(404)
        #return marshal(server, server_fields), 200

        return render_template('kickstart/kickstart.j2',
                               kickstart=default_kickstart,
                               profile=profile), 200
