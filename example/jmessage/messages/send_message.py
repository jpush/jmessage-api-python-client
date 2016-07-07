from jmessage import users
from jmessage import common
from conf import *
jmessage=common.JMessage(app_key,master_secret)

messages=jmessage.create_messages()

message=messages.build_message(1,"single","admin","text","xiaohuihui","admin","Hello, JMessage!")

response=messages.send_messages(message)
print response