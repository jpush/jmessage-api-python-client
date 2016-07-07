from jmessage import users
from jmessage import common
from conf import *
import time

import json
jmessage=common.JMessage(app_key,master_secret)

users=jmessage.create_users()

response=users.put_user_password("xiaohuihui","123456")
time.sleep(5)
print response

