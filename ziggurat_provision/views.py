from flask import abort, flash, jsonify, make_response, redirect, \
    render_template, request

from . import app, db, Server
from .forms import LoginForm


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.route('/api/servers', methods=['POST'])
def create_server():
    if not request.json:
        abort(400)
    return ''


@app.route('/api/servers/<mac_address>', methods=['GET'])
def get_server(mac_address):
    mac_address = Server.validate_mac_address(mac_address)
    if mac_address is None:
        abort(404)
    server = Server.query.filter_by(mac_address=mac_address).first()
    if server is None:
        abort(404)
    return jsonify(server.serialize())


@app.route('/api/servers', methods=['GET'])
def get_servers():
    x = [i.serialize() for i in Server.query.all()]
    return jsonify(servers=x)


@app.route('/api/servers/<mac_address>', methods=['PUT'])
def update_server(mac_address):
    if not request.json:
        abort(400)
    return ''
