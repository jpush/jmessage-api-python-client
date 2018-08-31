class Room(object):

    URI = 'https://api.im.jpush.cn/v1/chatroom/'

    def __init__(self, jmessage):
        self._jmessage = jmessage

    def all(self, count, start=0):
        params = {
            'start': start,
            'count': count
        }
        resp = self._jmessage.get(Room.URI, params=params)
        return resp

    def get(self, roomids):
        uri = Room.URI + 'batch'
        if not isinstance(roomids, list):
            roomids = [roomids]
        resp = self._jmessage.post(uri, data=roomids)
        return resp

    def create(self, owner, name, members=None, desc=None):
        data = {
            'owner_username': owner,
            'name': name
        }
        if members:
            if not isinstance(members, list):
                members = [members]
            data['members_username'] = members
        if desc:
            data['description'] = desc

        resp = self._jmessage.post(Room.URI, data=data)
        return resp

    def update(self, roomid, *, owner, name, desc):
        uri = Room.URI + str(roomid)
        data = {
            'owner_username': owner,
            'name': name,
            'description': desc
        }
        resp = self._jmessage.put(uri, data=data)
        return resp

    def delete(self, roomid):
        uri = Room.URI + str(roomid)
        resp = self._jmessage.delete(uri)
        return resp

    def members(self, roomid, count, start=0):
        uri = Room.URI + str(roomid) + '/members'
        params = {
            'start': start,
            'count': count
        }
        resp = self._jmessage.get(uri, params=params)
        return resp

    def add_members(self, roomid, members):
        uri = Room.URI + str(roomid) + '/members'
        if not isinstance(members, list):
            members = [members]
        resp = self._jmessage.put(uri, data=members)
        return resp

    def remove_members(self, roomid, members):
        uri = Room.URI + str(roomid) + '/members'
        if not isinstance(members, list):
            members = [members]
        resp = self._jmessage.delete(uri, data=members)
        return resp

    def add_silence(self, roomid, username):
        params = { 'status': 1 }
        return self._forbidden(roomid, username, params)

    def remove_silence(self, roomid, username):
        params = { 'status': 0 }
        return self._forbidden(roomid, username, params)

    def _forbidden(self, roomid, username, params):
        uri = Room.URI + str(roomid) + '/forbidden/' + username
        resp = self._jmessage.put(uri, params=params)
        return resp
