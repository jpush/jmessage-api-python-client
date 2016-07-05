from im import users
from im import common
from conf import *
jmessage=common.JMessage(app_key,master_secret)

users=jmessage.create_users()

user= {"username": "admin", "password": "passwords"}
response= users.regist_admin(user)
print response
