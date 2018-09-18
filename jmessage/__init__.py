__version__ = '2.0.0'

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
        if data is None:
            headers = { 'content-type': 'application/json; charset=utf-8' }
        return self._session.put(uri, params=params, json=data, headers=headers)

    def delete(self, uri, params=None, data=None):
        if data is None:
            headers = { 'content-type': 'application/json; charset=utf-8' }
        return self._session.delete(uri, params=params, json=data, headers=headers)
