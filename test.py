import pytest
from application import index

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    
@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
