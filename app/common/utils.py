from typing import Union

from werkzeug.urls import url_parse

from flask import current_app, url_for


def get_next_page(next_page: Union[str, None]) -> str:
    ''' Redirect the user to the next page given in the url if it exists,
    otherwise redirect them to their home page.

    :param next_page: Next page to redirect the user to
    '''
    if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for(current_app.config['LOGIN_REDIRECT_ENDPOINT'])
    return next_page
