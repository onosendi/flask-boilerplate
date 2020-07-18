def truncate(text: str, max_length: int) -> str:
    ''' Truncate text if greater than `max_length`.

    This function exists as an example on how to configure jinja filters. It is
    not used anywhere in this boilerplate.

    :param text: Text to truncate
    :param max_length: Max length of text before truncating
    '''
    if len(text) > max_length:
        text = f'{text[0:max_length]}...'
    return text
