from context import jmessage
from utils import parser
from jmessage.room import Room

client = Room(jmessage)

username = 'user_x'
usernames = [ 'uuu0', 'uuu1', 'uuu2', 'uuu3']
roomid = 111111

# # 创建聊天室
# resp = client.create(username, 'test-room')

# # 获取聊天室详情
# resp = client.get(roomid)

# # 获取应用下聊天室列表
# resp = client.all(10)

# # 更新聊天室信息
# resp = client.update(roomid, owner=username, name='room', desc='desc')

# # 删除聊天室
# resp = client.delete(roomid)

# # 获取聊天室成员列表
# resp = client.members(roomid, 10)

# # 添加聊天室成员
# resp = client.add_members(roomid, 'uuu0')

# # 移除聊天室成员
# resp = client.remove_members(roomid, 'uuu0')

# # 批量添加聊天室成员
# resp = client.add_members(roomid, usernames)

# # 批量移除聊天室成员
# resp = client.remove_members(roomid, usernames)


# # 禁言用户
# resp = client.add_silence(roomid, 'uuu0')

# # 解除用户禁言
# resp = client.remove_silence(roomid, 'uuu0')


parser(resp)
