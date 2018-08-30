from context import jmessage
from im import parser
from jmessage.group import Group

client = Group(jmessage)

username = 'user_x'
usernames = [ 'uuu0', 'uuu1', 'uuu2', 'uuu3']
gid = 111111

# # 创建群组
# resp = client.create(username, 'test-group')

# # 删除群组
# resp = client.delete(gid)

# # 获取群组详情
# resp = client.get(gid)

# # 更新群组信息
# resp = client.update(gid, desc='group-desc')

# # 获取当前应用的群组列表
# resp = client.all(10)

# # 获取群组成员列表
# resp = client.members(gid)

# # 增加群组成员
# resp = client.add_members(gid, 'uuu0')

# # 删除群组成员
# resp = client.remove_members(gid, 'uuu0')

# # 批量增加群组成员
# resp = client.add_members(gid, usernames)

# # 批量删除群组成员
# resp = client.remove_members(gid, usernames)


# # 添加禁言成员
# resp = client.add_silence(gid, 'uuu0')

# # 移除禁言成员
# resp = client.remove_silence(gid, 'uuu0')

# # 批量添加禁言成员
# resp = client.add_silence(gid, usernames)

# # 批量移除禁言成员
# resp = client.remove_silence(gid, usernames)


parser(resp)
