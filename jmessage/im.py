class IM(object):

    SDK_URI = 'https://api.im.jpush.cn/v1/sdkregister/status'
    WORD_URI = 'https://api.im.jpush.cn/v1/sensitiveword/'

    def __init__(self, jmessage):
        self._jmessage = jmessage

    def all_words(self, count, start=0):
        if count > 200:
            count = 200
        params = {
            'start': start,
            'count': count
        }
        resp = self._jmessage.get(IM.WORD_URI, params=params)
        return resp

    def add_words(self, words):
        if not isinstance(words, list):
            words = [words]
        resp = self._jmessage.post(IM.WORD_URI, data=words)
        return resp

    def change_word(self, *, old, new):
        data = {
            'new_word': new,
            'old_word': old
        }
        resp = self._jmessage.put(IM.WORD_URI, data=data)
        return resp

    def remove_word(self, word):
        data = { 'word': word }
        resp = self._jmessage.delete(IM.WORD_URI, data=data)
        return resp

    def word_status(self):
        uri = IM.WORD_URI + 'status'
        resp = self._jmessage.get(uri)
        return resp

    def open_filter(self):
        return self._status(1)

    def close_filter(self):
        return self._status(0)

    def _status(self, status):
        uri = IM.WORD_URI + 'status'
        params = { 'status': status }
        resp = self._jmessage.put(uri, params=params)
        return resp


    def open_sdk(self):
        params = { 'status': 1 }
        resp = self._jmessage.put(IM.SDK_URI, params=params)
        return resp

    def close_sdk(self):
        params = { 'status': 0 }
        resp = self._jmessage.put(IM.SDK_URI, params=params)
        return resp

    def sdk_status(self):
        resp = self._jmessage.get(IM.SDK_URI)
        return resp
