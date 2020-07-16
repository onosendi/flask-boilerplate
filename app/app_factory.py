from flask import Flask, render_template


def create_app(config: object) -> object:
    app = Flask(__name__)
    with app.app_context():
        configure_app(app, config)
        configure_extensions(app)
        configure_blueprints(app)
        configure_jinja(app)
        configure_error_handlers(app)
        configure_logging(app)
    return app


def configure_app(app: object, config: object) -> None:
    app.config.from_object(config)


def configure_extensions(app: object) -> None:
    from app.common.extensions import db, migrate, login
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'default.login'


def configure_blueprints(app: object) -> None:
    from app.default.views import default_views
    from app.posts.views import posts_views
    from app.users.views import users_views
    for blueprint in [default_views, posts_views, users_views]:
        app.register_blueprint(blueprint)


def configure_jinja(app: object) -> None:
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.trim_blocks = True

    # Globals
    app.jinja_env.globals['APP_NAME'] = app.config['APP_NAME']

    # Filters
    from app.common.filters import truncate
    app.jinja_env.filters['truncate'] = truncate


def configure_error_handlers(app: object) -> None:
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500


def configure_logging(app: object) -> None:
    if not app.debug and not app.testing:
        ''' Logging logic goes here. '''
