from flask import make_response

from . import rest_api

@rest_api.representation('text/plain')
def output_plain(data, code, headers=None):
    resp = make_response(str(data), code)
    resp.headers.extend(headers or {})
    return resp
