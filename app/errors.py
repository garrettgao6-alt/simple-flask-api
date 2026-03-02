import urllib.error
from flask import jsonify


def register_error_handlers(app):

    @app.errorhandler(ValueError)
    def handle_value_error(e):
        return jsonify({
            "error": str(e)
        }), 400


    @app.errorhandler(urllib.error.HTTPError)
    def handle_http_error(e):
        return jsonify({
            "error": "HTTP error",
            "code": e.code,
            "reason": str(e.reason)
        }), 400


    @app.errorhandler(urllib.error.URLError)
    def handle_url_error(e):
        return jsonify({
            "error": "URL error",
            "reason": str(e.reason)
        }), 400


    @app.errorhandler(Exception)
    def handle_generic_error(e):
        app.logger.exception("Unhandled exception")
        return jsonify({
            "error": "internal server error"
        }), 500
