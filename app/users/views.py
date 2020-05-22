from flask import Blueprint, render_template

from flask_login import login_required

users_views = Blueprint('users', __name__, url_prefix='/users')


@users_views.route('/')
@login_required
def index():
    return render_template('users/index.jinja')
