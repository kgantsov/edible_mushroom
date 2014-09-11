import os

from flask import Flask

from edible_mushroom.core import babel
from edible_mushroom.core import csrf
from edible_mushroom.lib.helpers import register_blueprints


def create_app(config=None):
    app = Flask(__name__)
    if not config:
        config = 'development.ini'

    app.config.from_pyfile(config)

    csrf.init_app(app)
    babel.init_app(app)

    register_blueprints(
        app, 'edible_mushroom.modules', [os.path.join(__path__[0], 'modules')]
    )

    return app
