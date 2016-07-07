from jmessage import users
from jmessage import common
from conf import *
jmessage=common.JMessage(app_key,master_secret)

users=jmessage.create_users()

response=users.get_user_by_username("xiaohuihui")
print (response)

