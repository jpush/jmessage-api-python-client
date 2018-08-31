class Message(object):

    URI = 'https://api.im.jpush.cn/v1/messages/'

    def __init__(self, jmessage):
        self._jmessage = jmessage

    def retract(self, username, msgid):
        uri = Message.URI + username + '/' + str(msgid) + '/retract'
        data = {
            'username': username,
            'msgid': msgid
        }
        resp = self._jmessage.post(uri, data=data)
        return resp

    def send(self, msg):
        if isinstance(msg, Model):
            msg = msg.json()
        resp = self._jmessage.post(Message.URI, data=msg)
        return resp


class Resource(object):

    URI = 'https://api.im.jpush.cn/v1/resource'

    def __init__(self, jmessage):
        self._jmessage = jmessage

    def upload_image(self, image):
        return self.upload('image', image)

    def upload_voice(self, voice):
        return self.upload('voice', voice)

    def upload_file(self, file):
        return self.upload('file', file)

    def upload(self, type, file):
        params = { 'type': type }
        files = { 'filename': file }
        resp = self._jmessage.post(Resource.URI, params=params, files=files)
        return resp

    def download(self, mediaId):
        params = { 'mediaId': mediaId }
        resp = self._jmessage.get(Resource.URI, params=params)
        return resp


class Model(object):

    def __init__(self, version=1):
        self.data = { 'version': version }

    def json(self):
        return self.data

    def text(self, content, extras=None):
        msg_body = { 'text': content }
        if extras and extras is dict:
            msg_body['extras'] = extras
        self.data['msg_body'] = msg_body
        self.data['msg_type'] = 'text'
        return self

    def image(self, images):
        self.data['msg_body'] = images
        self.data['msg_type'] = 'image'
        return self

    def voice(self, voices):
        self.data['msg_body'] = voices
        self.data['msg_type'] = 'voice'
        return self

    def custom(self, content):
        if content is dict:
            self.data['msg_body'] = content
        self.data['msg_type'] = 'custom'
        return self

    def set_target(self, id, type, name=None, appkey=None):
        self.data['target_id'] = id
        if type in ['single', 'group', 'chatroom']:
            self.data['target_type'] = type
        if name:
            self.data['target_name'] = name
        if appkey:
            self.data['target_appkey'] = appkey
        return self

    def set_from(self, id, type, name=None):
        self.data['from_id'] = id
        self.data['from_type'] = type
        if name:
            self.data['from_name'] = name
        return self

    def notification(self, title=None, alert=None):
        notification = {}
        if title:
            notification['title'] = title
        if alert:
            notification['alert'] = alert
        self.data['notification'] = notification
        return self

    def notifiable(self, boo=True):
        '''boo=True 表示在通知栏展示'''
        '''no_notification 消息是否在通知栏展示 true 或者 false，默认为 false，表示在通知栏展示'''
        self.data['no_notification'] = not boo
        return self

    def offline(self, boo=True):
        '''boo=True 表示需要离线存储'''
        '''no_offline 消息是否离线存储 true 或者 false，默认为 false，表示需要离线存储'''
        self.data['no_offline'] = not boo
        return self
