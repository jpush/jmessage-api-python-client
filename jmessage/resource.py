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
