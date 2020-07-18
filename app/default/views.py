from flask import (
    Blueprint, current_app, flash, redirect, render_template, request, url_for,
)

from flask_login import current_user, login_user, logout_user
from sqlalchemy import func
from app.common.utils import get_next_page
from app.default.forms import LoginForm, RegisterForm
from app.users.models import User

default_views = Blueprint('default', __name__)


@default_views.route('/')
def index():
    return render_template('default/index.jinja')


@default_views.route('/about')
def about():
    return render_template('default/about.jinja')


@default_views.route('/login', methods=['get', 'post'])
def login():
    # If the user is already authenticated, redirect them to their home page.
    if current_user.is_authenticated:
        return redirect(url_for(current_app.config['LOGIN_REDIRECT_ENDPOINT']))

    form = LoginForm()

    if form.validate_on_submit():
        # Set the data sent through the form.
        login = form.login.data.lower()
        password = form.password.data
        remember = form.remember_me.data

        # Check if user exists by email.
        user_by_email = User.query.filter_by(email=login).first()

        # Check if login exists by username.
        user_by_username = User.query\
            .filter(func.lower(User.username) == login).first()

        # Set `user` to either email or username.
        user = user_by_email if user_by_email else user_by_username

        # Validate `user` with the given `password`, and make sure they are
        # still active (have not been soft deleted).
        if (user is None or not user.check_password(password)
                or not user.active):
            flash('Invalid email or password.')

            # Reload the page to avoid resubmit.
            return redirect(url_for('default.login'))

        # Actually login the user.
        login_user(user, remember=remember)

        # Redirect the user to the next page if it exists, otherwise redirect
        # them to their home page.
        return redirect(get_next_page(request.args.get('next')))
    return render_template('default/login.jinja', form=form)


@default_views.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('default.login'))


@default_views.route('/register', methods=['get', 'post'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data)
        user.set_password(form.password.data)
        user.commit()
        login_user(user)
        return redirect(url_for('users.index'))
    return render_template('default/register.jinja', form=form)
