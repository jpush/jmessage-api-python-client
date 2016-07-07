import requests
from .users import *
from .messages import *
from .groups import *
class JMessage(object):
    def __init__(self,key,secret):
        self.key = key
        self.secret = secret
        self.session = requests.Session()
        self.session.auth = (key, secret)

    def _request(self, method, body, request_url, content_type=None, version=None, params=None):
        headers = {}
        headers['user-agent'] = 'jpush-api-python-client'
        headers['connection'] = 'keep-alive'
        headers['content-type'] = 'application/json;charset:utf-8'
        response = self.session.request(method, request_url,data=body, params=params, headers=headers)
        return response

    def create_users(self):
        return User(self)

    def create_messages(self):
        return Message(self)

    def create_groups(self):
        return Group(self)
