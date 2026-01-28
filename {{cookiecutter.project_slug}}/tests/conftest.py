from hyperflask.factory import create_app
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
