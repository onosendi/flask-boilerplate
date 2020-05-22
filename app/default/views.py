from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_login import current_user, login_user, logout_user
from sqlalchemy import func
from werkzeug.urls import url_parse

from app.default.forms import LoginForm, RegisterForm
from app.users.models import User

default_views = Blueprint('default', __name__)


@default_views.route('/')
def index():
    return render_template('default/index.html')


@default_views.route('/about')
def about():
    return render_template('default/about.html')


@default_views.route('/login', methods=['get', 'post'])
def login():
    # If the user is already authenticated, redirect them to their home page.
    if current_user.is_authenticated:
        return redirect(url_for('users.index'))

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

            # Reload the page to avoid refresh submitting the same data.
            return redirect(url_for('default.login'))

        # Actually login the user.
        login_user(user, remember=remember)

        # Check if the next page to the `next` argument give in the url.
        next_page = request.args.get('next')

        # Redirect the user to `next_page` if an argument was given. If not,
        # redirect them to their home page.
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('users.index')
        return redirect(next_page)
    return render_template('default/login.html', form=form)


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
    return render_template('default/register.html', form=form)
