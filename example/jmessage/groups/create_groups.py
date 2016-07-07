from jmessage import users
from jmessage import common
from conf import *
import time

import json
jmessage=common.JMessage(app_key,master_secret)

groups=jmessage.create_groups()

group=groups.build_group(owner_username="dev_fang", name="jpush", members_username=["xiaohuihui"], desc="jpush group")
response=groups.create_group(group)
time.sleep(2)
print response


'''
{'members_username': ['xiaohuihui'], 'name': 'jpush', 'owner_username': 'dev_fang', 'desc': 'jpush group'}
https://api.jmessage.jpush.cn/v1/groups/
{"gid":10184253,"owner_username":"dev_fang","name":"jpush","desc":"jpush group","members_username":["xiaohuihui"],"level":3}
'''
