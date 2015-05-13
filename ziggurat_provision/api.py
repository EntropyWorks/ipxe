import re

from datetime import datetime
from flask import abort, jsonify, make_response, render_template, request
from flask.ext.restful import fields, marshal, marshal_with, reqparse, Resource

from . import app, rest_api
from .content import default_kickstart
from .models import db, MAC_RE, Server, SERVER_STATES, SERVER_PROFILES

def mac_address(mac_address):
    matches = MAC_RE.match(mac_address)
    if matches:
        return mac_address
    raise ValueError("%s is not a valid mac address" % mac_address)


def server_profile(profile):
    if profile in SERVER_PROFILES.keys():
        return profile
    raise ValueError("%s is not a valid profile" % profile)


def server_state(state):
    if state in SERVER_STATES:
        return state
    raise ValueError("%s is not a valid state" % state)


create_parser = reqparse.RequestParser()
create_parser.add_argument('mac_address', type=mac_address, required=True,
                           location='json')
create_parser.add_argument('hostname', type=str, required=True,
                           location='json')
create_parser.add_argument('profile', type=server_profile, required=True,
                           location='json')
create_parser.add_argument('state', type=server_state, required=True,
                           location='json')

update_parser = reqparse.RequestParser()
update_parser.add_argument('profile', type=server_profile, required=False,
                           location='json')
update_parser.add_argument('state', type=server_state, required=False,
                           location='json')

server_fields = {
    'mac_address': fields.String,
    'hostname': fields.String,
    'profile': fields.String,
    'state': fields.String,
    'created_at': fields.DateTime(dt_format='iso8601'),
    'updated_at': fields.DateTime(dt_format='iso8601'),
    'uri': fields.Url('server'),
}


@rest_api.representation('text/plain')
def output_plain(data, code, headers=None):
    resp = make_response(str(data), code)
    resp.headers.extend(headers or {})
    return resp

class KickstartAPI(Resource):
    def __init__(self):
        self.reqparse = update_parser
        super(KickstartAPI, self).__init__()
        self.representations = { 'text/plain': output_plain }

    def get(self, profile):
        return render_template('kickstart/kickstart.j2', kickstart=default_kickstart,
                                profile=profile), 200


class ServerAPI(Resource):
    def __init__(self):
        self.reqparse = update_parser
        super(ServerAPI, self).__init__()
        #self.representations = { 'text/plain': output_plain }

    def delete(self, mac_address):
        server = Server.query.get(mac_address)
        if server is not None:
            db.session.delete(server)
            db.session.commit()
        return None, 204

    def get(self, mac_address):
        server = Server.query.get(mac_address)
        if server is None:
            abort(404)
        return marshal(server, server_fields), 200

    def put(self, mac_address):
        args = self.reqparse.parse_args()
        profile = args.get('profile', None)
        state = args.get('state', None)
        server = Server.query.get(mac_address)
        # don't allow updates to non-existant
        if server is None:
            abort(400)

        update = False
        if profile:
            if profile != server.profile:
                server.profile = profile
                update = True
        if state:
            if state != server.state:
                server.state = state
                update = True

        if update:
            server.updated_at = datetime.utcnow()
            db.session.add(server)
            db.session.commit()
            return marshal(server, server_fields), 200

        return marshal(server, server_fields), 202


class ServerListAPI(Resource):
    def __init__(self):
        self.reqparse = create_parser
        super(ServerListAPI, self).__init__()

    def get(self):
        return marshal(Server.query.all(), server_fields), 200

    def post(self):
        args = self.reqparse.parse_args()
        print args
        server = Server(mac_address=args.mac_address.lower(),
                        hostname=args.hostname.lower(),
                        profile=args.profile,
                        state=args.state)
        db.session.add(server)
        db.session.commit()
        return marshal(server, server_fields), 201
