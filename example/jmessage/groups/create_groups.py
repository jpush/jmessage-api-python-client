from jmessage import users
from jmessage import common
from conf import *
import time

import json
jmessage=common.JMessage(app_key,master_secret)

groups=jmessage.create_groups()

group=groups.build_group(owner_username="dev_fang", name="jmessage", members_username=["xiaohuihui"], desc="jpush group")
response=groups.create_group(group)
time.sleep(2)
print (response.content)

