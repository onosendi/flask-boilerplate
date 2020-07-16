import os

from app.app_factory import create_app
from app.common.extensions import db
from app.posts.models import Post
from app.users.models import User
import config

if os.environ['FLASK_ENV'] == 'production':
    app = create_app(config.ProductionConfig)
else:
    app = create_app(config.DevelopmentConfig)


@app.shell_context_processor
def make_shell_context():
    return {
        'app': app,
        'db': db,
        'Post': Post,
        'User': User,
    }
