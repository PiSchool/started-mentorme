import os


def basic_auth(username, password, required_scopes=None):
    if username == os.environ.get('ADMIN_USERNAME', 'user') and password == os.environ.get('ADMIN_PASSWORD', 'password'):
        return {'user': 'admin'}
    # optional: raise exception for custom error response
    return None