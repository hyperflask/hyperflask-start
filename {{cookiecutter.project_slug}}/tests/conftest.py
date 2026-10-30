from hyperflask.factory import create_app
from werkzeug.serving import make_server
import threading
import pytest
import os


APP_ROOT = os.path.join(os.path.dirname(__file__), "..")


@pytest.fixture(scope="session")
def app():
    app = create_app(APP_ROOT)
    app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,
    })
    return app


@pytest.fixture(scope="session")
def live_server_url(app):
    """Serves the app over HTTP in a background thread for browser tests"""
    server = make_server("127.0.0.1", 0, app, threaded=True)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()
    thread.join()


@pytest.fixture(scope="session")
def base_url(live_server_url):
    # used by pytest-playwright so that page.goto("/") targets the live server
    return live_server_url
