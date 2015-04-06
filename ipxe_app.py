#!/usr/bin/python

import datetime
import time

from flask import Flask, jsonify, render_template, request, url_for
from ipxe_logic import db_connection, db_transaction, ServerForm


app = Flask(__name__)


INSERT_SQL = """
INSERT INTO server
(mac, hostname, state, profile, created, updated)
values(?, ?, ?, ?, ?, ?)
"""


SELECT_SQL = """SELECT mac, hostname, state, profile, created, updated FROM server"""


UPDATE_SQL = """
UPDATE server SET
hostname = ?,
state = ?,
profile = ?,
updated = ?
WHERE mac = ? and updated = ?
"""


VALID_PROFILES = []


VALID_STATES = []


def create_server(): pass


@app.route('/servers/<mac>', methods=['GET'])
def get_server(mac):
    with db_connection('./ipxe.sqlite3') as conn:
        with db_transaction(conn) as cursor:
            sql = "%s WHERE mac=?"
            server = cursor.execute(sql % SELECT_SQL, (mac,)).fetchone()
            if server is None: return jsonify({}), 404
            server_dict = dict(mac=server[0],
                               hostname=server[1],
                               state=server[2],
                               profile=server[3],
                               created=server[4]*1000,
                               updated=server[5]*1000)
            return jsonify(server_dict)


def update_server(mac): pass


@app.route('/servers', methods=['GET'])
def servers():
    with db_connection('./ipxe.sqlite3') as conn:
        with db_transaction(conn) as cursor:
            servers = cursor.execute(SELECT_SQL).fetchall()
            servers_list = []
            for server in servers:
                server_dict = dict(mac=server[0],
                                   hostname=server[1],
                                   state=server[2],
                                   profile=server[3],
                                   created=server[4]*1000,
                                   updated=server[5]*1000)
                servers_list.append(server_dict)
            return jsonify(servers=servers_list)


port = 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port), debug=True)
