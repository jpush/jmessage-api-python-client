class User(object):

    URI = 'https://api.im.jpush.cn/v1/users/'
    ADMIN_URI = 'https://api.im.jpush.cn/v1/admins/'

    def __init__(self, jmessage):
        self._jmessage = jmessage

    def all(self, count, start=0, admin=False):
        uri = User.URI
        if isinstance(admin, bool) and admin:
            uri = User.ADMIN_URI
        if count > 500:
            count = 500
        params = {
            'start': start,
            'count': count
        }
        resp = self._jmessage.get(uri, params=params)
        return resp

    def get(self, username):
        uri = User.URI + username
        resp = self._jmessage.get(uri)
        return resp

    def stat(self, usernames):
        if isinstance(usernames, list):
            uri = User.URI + 'userstat'
            resp = self._jmessage.post(uri, data=usernames)
        else:
            uri = User.URI + usernames +'/userstat'
            resp = self._jmessage.get(uri)
        return resp

    def groups(self, username):
        uri = User.URI + username + '/groups'
        resp = self._jmessage.get(uri)
        return resp

    def chatrooms(self, username):
        uri = User.URI + username + '/chatroom'
        resp = self._jmessage.get(uri)
        return resp

    def update_password(self, username, password):
        uri = User.URI + username + '/password'
        data = {
            'new_password': password
        }
        resp = self._jmessage.put(uri, data=data)
        return resp

    def delete(self, usernames):
        uri = User.URI
        data = None
        if isinstance(usernames, list):
            data = usernames
        else:
            uri = User.URI + usernames
        resp = self._jmessage.delete(uri, data=data)
        return resp

    def create(self, username, password,
        nickname=None, avatar=None, birthday=None, signature=None, gender=None, region=None, address=None, extras=None, admin=False):
        data = {
            'username': username,
            'password': password,
        }
        if nickname:
            data['nickname'] = nickname
        if avatar:
            data['avatar'] = avatar
        if birthday:
            data['birthday'] = birthday
        if signature:
            data['signature'] = signature
        if gender and gender in [0, 1, 2]:
            data['gender'] = gender
        if region:
            data['region'] = region
        if address:
            data['address'] = address
        if extras and isinstance(extras, dict):
            data['extras'] = extras

        return self.register(data, admin=admin)

    def register(self, users, admin=False):
        uri = User.URI
        if isinstance(admin, bool) and admin:
            uri = User.ADMIN_URI
        if not isinstance(users, list):
            users = [users]
        resp = self._jmessage.post(uri, data=users)
        return resp

    def update(self, username,
        nickname=None, avatar=None, birthday=None, signature=None, gender=None, region=None, address=None, extras=None):
        uri = User.URI + username
        data = {}
        if nickname:
            data['nickname'] = nickname
        if avatar:
            data['avatar'] = avatar
        if birthday:
            data['birthday'] = birthday
        if signature:
            data['signature'] = signature
        if gender and gender in [0, 1, 2]:
            data['gender'] = gender
        if region:
            data['region'] = region
        if address:
            data['address'] = address
        if extras and isinstance(extras, dict):
            data['extras'] = extras

        resp = self._jmessage.put(uri, data=data)
        return resp

    def friends(self, username):
        uri = User.URI + username + '/friends'
        resp = self._jmessage.get(uri)
        return resp

    def add_friends(self, username, friends):
        uri = User.URI + username + '/friends'
        if not isinstance(friends, list):
            friends = [friends]
        resp = self._jmessage.post(uri, data=friends)
        return resp

    def remove_friends(self, username, friends):
        uri = User.URI + username + '/friends'
        if not isinstance(friends, list):
            friends = [friends]
        resp = self._jmessage.delete(uri, data=friends)
        return resp

    def update_friend(self, username, friendname, remark=None, others=None):
        data = { 'username': friendname }
        if remark:
            data['note_name'] = remark
        if others:
            data['others'] = others
        return self.update_friends(username, data)

    def update_friends(self, username, data):
        uri = User.URI + username + '/friends'
        if not isinstance(data, list):
            data = [data]
        resp = self._jmessage.put(uri, data=data)
        return resp


    def blacklist(self, username):
        uri = User.URI + username + '/blacklist'
        resp = self._jmessage.get(uri)
        return resp

    def add_blacklist(self, username, users):
        uri = User.URI + username + '/blacklist'
        if not isinstance(users, list):
            users = [users]
        resp = self._jmessage.put(uri, data=users)
        return resp

    def remove_blacklist(self, username, users):
        uri = User.URI + username + '/blacklist'
        if not isinstance(users, list):
            users = [users]
        resp = self._jmessage.delete(uri, data=users)
        return resp


    def add_groups_shield(self, username, gids):
        if not isinstance(gids, list):
            gids = [gids]
        data = { 'add': gids }
        return self._groups_shield(username, data)

    def remove_groups_shield(self, username, gids):
        if not isinstance(gids, list):
            gids = [gids]
        data = { 'remove': gids }
        return self._groups_shield(username, data)

    def _groups_shield(self, username, data):
        uri = User.URI + username + '/groupsShield'
        return self._jmessage.post(uri, data=data)


    def add_sigle_nodisturb(self, username, users):
        if not isinstance(users, list):
            users = [users]
        data = { 'single': { 'add': users } }
        return self._nodisturb(username, data)

    def remove_sigle_nodisturb(self, username, users):
        if not isinstance(users, list):
            users = [users]
        data = { 'single': { 'remove': users } }
        return self._nodisturb(username, data)

    def add_group_nodisturb(self, username, gids):
        if not isinstance(gids, list):
            gids = [gids]
        data = { 'group': { 'add': gids } }
        return self._nodisturb(username, data)

    def remove_group_nodisturb(self, username, gids):
        if not isinstance(gids, list):
            gids = [gids]
        data = { 'group': { 'remove': gids } }
        return self._nodisturb(username, data)

    def open_global_nodisturb(self, username):
        data = { 'global': 1 }
        return self._nodisturb(username, data)

    def close_global_nodisturb(self, username):
        data = { 'global': 0 }
        return self._nodisturb(username, data)

    def _nodisturb(self, username, data):
        uri = User.URI + username + '/nodisturb'
        resp = self._jmessage.post(uri, data=data)
        return resp


    def block(self, username):
        return self._forbidden(username, True)

    def active(self, username):
        return self._forbidden(username, False)

    def _forbidden(self, username, forbidden):
        uri = User.URI + username + '/forbidden'
        params = { 'disable': forbidden }
        resp = self._jmessage.put(uri, params=params)
        return resp
