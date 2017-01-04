from jmessage import users
from jmessage import common
from conf import *
import time

import json
jmessage=common.JMessage(app_key,master_secret)

groups=jmessage.create_groups()

response=groups.get_groups_by_username("xiaohuihui")
time.sleep(2)
print (response.content)