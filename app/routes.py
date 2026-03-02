import urllib.error
from flask import request, jsonify
from .services.fetch_service import fetch_url_content
from .utils import validate_url


def register_routes(app):

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"})


    @app.route("/fetch", methods=["GET"])
    def fetch():
        url = request.args.get("url")

        if not url:
            return jsonify({"error": "missing url parameter"}), 400

        app.logger.info(f"/fetch called url={url}")

        # 🔒 SSRF protection
        validate_url(url)

        result = fetch_url_content(url)

        return jsonify({
            "url": url,
            **result
        })
