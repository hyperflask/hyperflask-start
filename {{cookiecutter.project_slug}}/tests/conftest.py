from hyperflask.factory import create_app
import pytest
import os


APP_ROOT = os.path.join(os.path.dirname(__file__), "..")


@pytest.fixture
def app():
    return create_app(APP_ROOT)
