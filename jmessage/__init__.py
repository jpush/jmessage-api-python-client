__version__ = '0.0.1'

import requests

class JMessage(object):

    def __init__(self, app_key, master_secret):
        session = requests.Session()
        session.auth = (app_key, master_secret)
        self._session = session

    def get(self, uri, params=None):
        return self._session.get(uri, params=params)

    def post(self, uri, params=None, data=None, files=None):
        return self._session.post(uri, params=params, json=data, files=files)

    def put(self, uri, params=None, data=None):
        return self._session.put(uri, params=params, json=data)

    def delete(self, uri, params=None, data=None):
        return self._session.delete(uri, params=params, json=data)
