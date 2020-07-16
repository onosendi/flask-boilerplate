from flask import Blueprint, redirect, request

from flask_login import current_user, login_required

from app.common.utils import get_next_page
from app.posts.models import Post

posts_views = Blueprint('posts', __name__, url_prefix='/posts')


@posts_views.route('/<int:post_id>/delete')
@login_required
def delete(post_id):
    ''' The database should never be modified by a GET request. This is here
    purely for example on how to structure your application. This would be a
    good place to put your APIs called via JavaScript.

    :param post_id: The post ID to delete.
    '''
    post = Post.query.filter_by(author=current_user, id=post_id).first_or_404()
    post.delete()
    post.commit()
    return redirect(get_next_page(request.args.get('next')))
