from pprint import pprint
from context import jmessage
from jmessage.user import User

client = User(jmessage)

user = 'user_x'
admin = 'admin_x'
users = [
    { 'username': 'uuu0', 'password': 'passwd' },
    { 'username': 'uuu1', 'password': 'passwd' },
    { 'username': 'uuu2', 'password': 'passwd' },
    { 'username': 'uuu3', 'password': 'passwd' }
]
usernames = [ 'uuu0', 'uuu1', 'uuu2', 'uuu3']

def parser(resp):
    pprint(resp.status_code)
    pprint(resp.headers)
    if resp.status_code != 204:
        pprint(resp.json())



# # 注册用户
# resp = client.create(user, 'passwd')

# # 批量注册用户
# resp = client.register(users)

# # 注册管理员
# resp = client.create(admin, 'passwd', admin=True)

# # 批量注册管理员
# resp = client.register(users, admin=True)

# # 获取用户列表
# resp = client.all(10)

# # 获取应用管理员列表
# resp = client.all(10, admin=True)

# # 获取用户信息
# resp = client.get(user)

# # 更新用户信息
# resp = client.update(user, nickname='nick_x')

# # 修改密码
# resp = client.update_password(user, 'passwd_x')

# # 删除用户
# resp = client.delete(user)

# # 批量删除用户
# resp = client.delete(usernames)

# # 查询用户在线状态
# resp = client.stat(user)

# # 批量查询用户在线状态
# resp = client.stat(usernames)


# # 黑名单列表
# resp = client.blacklist(user)

# # 添加黑名单
# resp = client.add_blacklist(user, 'uuu0')

# # 移除黑名单
# resp = client.remove_blacklist(user, 'uuu0')

# # 批量添加黑名单
# resp = client.add_blacklist(user, usernames)

# # 批量移除黑名单
# resp = client.remove_blacklist(user, usernames)


# # 添加单聊免打扰设置
# resp = client.add_sigle_nodisturb(user, 'uuu0')

# # 移除单聊免打扰设置
# resp = client.remove_sigle_nodisturb(user, 'uuu0')

# # 打开全局免打扰
# resp = client.open_global_nodisturb(user)

# # 关闭全局免打扰
# resp = client.close_global_nodisturb(user)

# # 禁用用户
# resp = client.block(user)

# # 激活用户
# resp = client.active(user)

# # 获取用户的群组列表
# resp = client.groups(user)

# # 获取用户聊天室列表
# resp = client.chatrooms(user)

parser(resp)
