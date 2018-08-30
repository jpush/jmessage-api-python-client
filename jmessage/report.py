class Report(object):

    URI = 'https://report.im.jpush.cn/v2/'

    def __init__(self, jmessage):
        self._jmessage = jmessage

    def messages(self, *, count, begin, end):
        uri = Report.URI + 'messages'
        params = {
            'begin_time': begin,
            'end_time': end,
            'count': count
        }
        resp = self._jmessage.get(uri, params=params)
        return resp

    def messages_by_cursor(self, cursor):
        uri = Report.URI + 'messages'
        params = { 'cursor': cursor }
        resp = self._jmessage.get(uri, params=params)
        return resp

    def users_messages(self, username, *, count, begin, end):
        return self.get_messages('users', username, count=count, begin=begin, end=end)

    def users_messages_by_cursor(self, username, cursor):
        return self.get_messages_by_cursor('users', username, cursor)

    def groups_messages(self, gid, *, count, begin, end):
        return self.get_messages('groups', gid, count=count, begin=begin, end=end)

    def groups_messages_by_cursor(self, gid, cursor):
        return self.get_messages_by_cursor('groups', username, cursor)

    def rooms_messages(self, roomid, *, count, begin, end):
        return self.get_messages('chatrooms', roomid, count=count, begin=begin, end=end)

    def rooms_messages_by_cursor(self, roomid, cursor):
        return self.get_messages_by_cursor('chatrooms', roomid, cursor)

    def get_messages(self, type, id, *, count, begin, end):
        uri = Report.URI + type + '/' + id + '/messages'
        params = {
            'begin_time': begin,
            'end_time': end,
            'count': count
        }
        resp = self._jmessage.get(uri, params=params)
        return resp

    def get_messages_by_cursor(self, type, id, cursor):
        uri = Report.URI + type + '/' + id + '/messages'
        params = { 'cursor': cursor }
        resp = self._jmessage.get(uri, params=params)
        return resp


    def users_statistic(self, unit='DAY', start, duration):
        return self.statistic('users', unit=unit, start=start, duration=duration)

    def messages_statistic(self, unit='DAY', start, duration):
        return self.statistic('messages', unit=unit, start=start, duration=duration)

    def groups_statistic(self, unit='DAY', start, duration):
        return self.statistic('groups', unit=unit, start=start, duration=duration)

    def statistic(self, type, *, unit='DAY', start, duration)
        uri = Report.URI + 'statistic/' + type
        params = {
            'time_unit': unit,
            'start': start,
            'duration': duration
        }
        resp = self._jmessage.get(uri, params=params)
        return resp
