import unittest
from jmessage import users
from jmessage import common
from conf import *
import random
import string

import unittest
from jmessage import users
from jmessage import common
from conf import *
import time
import json

jmessage=common.JMessage(app_key,master_secret)
users=jmessage.create_users()


class TestUser(unittest.TestCase):
    def test_create_group(self):
        user = [users.build_user("user123456", "password")]
        response = users.regist_user(user)
        print (response.content)
        self.assertEqual(response.status_code, 403)

    def test_get_group(self):
        user = {"username": "admin", "password": "passwords"}
        response = users.regist_admin(user)
        print (response.content)
        self.assertEqual(response.status_code, 403)

    def test_get_group_members(self):
        response = users.put_user_password("xiaohuihui", "123456")
        print (response.content)
        self.assertEqual(response.status_code, 204)

    def test_get_groups_by_username(self):
        response = users.get_user_by_username("xiaohuihui")
        print (response.content)
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()