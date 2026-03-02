from flask import Flask, request
from .routes import register_routes
from .errors import register_error_handlers
import time


def create_app():
    app = Flask(__name__)

    register_routes(app)
    register_error_handlers(app)

    @app.before_request
    def start_timer():
        request.start_time = time.time()

    @app.after_request
    def log_request(response):
        if hasattr(request, "start_time"):
            duration = round((time.time() - request.start_time) * 1000, 2)
            app.logger.info(
                f"{request.method} {request.path} "
                f"status={response.status_code} "
                f"duration={duration}ms"
            )
        return response

    return app
