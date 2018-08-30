class SensitiveWord(object):

    URI = 'https://api.im.jpush.cn/v1/sensitiveword/'

    def all(self, count, start=0):
        if count > 200:
            count = 200
        params = {
            'start': start,
            'count': count
        }
        resp = self._jmessage.get(SensitiveWord.URI, params=params)
        return resp

    def __init__(self, jmessage):
        self._jmessage = jmessage

    def add(self, words):
        if not isinstance(words, list):
            words = [words]
        resp = self._jmessage.post(SensitiveWord.URI, data=words)
        return resp

    def change(self, old, new):
        data = {
            'new_word': new,
            'old_word': old
        }
        resp = self._jmessage.put(SensitiveWord.URI, data=data)
        return resp

    def remove(self, word):
        data = { 'word': word }
        resp = self._jmessage.delete(SensitiveWord.URI, data=data)
        return resp

    def status(self):
        uri = SensitiveWord.URI + 'status'
        resp = self._jmessage.get(uri)
        return resp

    def open(self):
        return self._status(1)

    def close(self):
        return self._status(0)

    def _status(Self, status)
        uri = SensitiveWord.URI + 'status'
        params = { 'status': status }
        resp = self._jmessage.put(uri, params=params)
        return resp
