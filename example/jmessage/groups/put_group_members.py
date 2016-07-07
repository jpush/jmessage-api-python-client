from jmessage import users
from jmessage import common
from conf import *
import time
import json

jmessage=common.JMessage(app_key,master_secret)
groups=jmessage.create_groups()

add= [
    "usernadfsdfme", "xiaouihui"
]

response=groups.put_group_members("10184271",add)
time.sleep(2)
print (response)