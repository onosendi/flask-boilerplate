def truncate(text: str, max_length: int) -> str:
    ''' Truncate text if greater than `max_length`.

    :param text: Text to truncate
    :param max_length: Max length of text before truncating
    '''
    if len(text) > max_length:
        text = f'{text[0:max_length]}...'
    return text
