import os
import config

from app.app_factory import create_app
from app.extensions import db
from app.users.models import User

if os.environ['FLASK_ENV'] == 'production':
    app = create_app(config.ProductionConfig)
else:
    app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        'app': app,
        'db': db,
        'User': User,
    }
