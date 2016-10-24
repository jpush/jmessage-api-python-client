import unittest
from jmessage import users
from jmessage import common
from conf import *
import time
import json

jmessage=common.JMessage(app_key,master_secret)
messages=jmessage.create_messages()


class TestMessages(unittest.TestCase):
    def test_create_group(self):
        message = messages.build_message(1, "single", "admin", "text", "xiaohuihui", "admin", "Hello, JMessage!")
        response = messages.send_messages(message)
        print (response.content)
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()