from flask import Blueprint, redirect, render_template, url_for

from flask_login import current_user, login_required

from app.posts.forms import PostForm
from app.posts.models import Post

users_views = Blueprint('users', __name__, url_prefix='/users')


@users_views.route('/', methods=['get', 'post'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(author=current_user, body=form.body.data)
        post.commit()
        # Reload the page to avoid resubmit.
        return redirect(url_for('users.index'))
    posts = Post.query\
        .filter_by(author=current_user, active=True)\
        .order_by(Post.created.desc())\
        .all()
    return render_template('users/index.jinja', form=form, posts=posts)
