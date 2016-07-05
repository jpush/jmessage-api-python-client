from im import users
from im import common
from conf import *
import time

import json
jmessage=common.JMessage(app_key,master_secret)

users=jmessage.create_users()

user= [users.build_user("usernadfsdfme","password")]
response=users.regist_user(user)
time.sleep(2)
print response

