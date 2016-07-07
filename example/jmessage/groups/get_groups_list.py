from jmessage import users
from jmessage import common
from conf import *
import time

import json
jmessage=common.JMessage(app_key,master_secret)

groups=jmessage.create_groups()

response=groups.get_groups_list("1","2")
time.sleep(2)
print (response)