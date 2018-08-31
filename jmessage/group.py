class Group(object):

    URI = 'https://api.im.jpush.cn/v1/groups/'

    def __init__(self, jmessage):
        self._jmessage = jmessage

    def all(self, count, start=0):
        if count > 500:
            count = 500
        params = {
            'start': start,
            'count': count
        }
        resp = self._jmessage.get(Group.URI, params=params)
        return resp

    def get(self, gid):
        uri = Group.URI + str(gid)
        resp = self._jmessage.get(uri)
        return resp

    def delete(self, gid):
        uri = Group.URI + str(gid)
        resp = self._jmessage.delete(uri)
        return resp

    def update_owner(self, gid, username, appkey=None):
        uri = Group.URI + 'owner/'+ str(gid)
        data = { 'username': username }
        if appkey:
            data['appkey'] = appkey
        resp = self._jmessage.put(uri)
        return resp

    def create(self, owner, name, members=None, avatar=None, desc=None, flag=None):
        data = {
            'owner_username': owner,
            'name': name
        }
        if members:
            if not isinstance(members, list):
                members = [members]
            data['members_username'] = members
        if avatar:
            data['avatar'] = avatar
        if desc:
            data['desc'] = desc
        if flag and flag in [1, 2]:
            data['flag'] = flag

        resp = self._jmessage.post(Group.URI, data=data)
        return resp

    def update(self, gid, name=None, avatar=None, desc=None):
        uri = Group.URI + str(gid)
        data = {}
        if name:
            data['name'] = name
        if avatar:
            data['avatar'] = avatar
        if desc:
            data['desc'] = desc

        resp = self._jmessage.put(uri, data=data)
        return resp


    def members(self, gid):
        uri = Group.URI + str(gid) + '/members'
        resp = self._jmessage.get(uri)
        return resp

    def add_members(self, gid, usernames):
        if not isinstance(usernames, list):
            usernames = [usernames]
        data = { 'add': usernames }
        return self._update_members(gid, data)

    def remove_members(self, gid, usernames):
        if not isinstance(usernames, list):
            usernames = [usernames]
        data = { 'remove': usernames }
        return self._update_members(gid, data)

    def _update_members(self, gid, data):
        uri = Group.URI + str(gid) + '/members'
        resp = self._jmessage.post(uri, data=data)
        return resp


    def add_silence(self, gid, usernames):
        params = { 'status': True }
        return self._silence(gid, params, usernames)

    def remove_silence(self, gid, usernames):
        params = { 'status': False }
        return self._silence(gid, params, usernames)

    def _silence(self, gid, params, data):
        if not isinstance(data, list):
            data = [data]
        uri = Group.URI + 'messages/'+ str(gid) + '/silence'
        resp = self._jmessage.put(uri, params=params, data=data)
        return resp
