from jmessage import users
from jmessage import common
from conf import *
jmessage=common.JMessage(app_key,master_secret)
users=jmessage.create_users()
user= [users.build_user("user12345678","password")]
response=users.regist_user(user)
print (response.content)

