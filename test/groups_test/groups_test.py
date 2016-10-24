import unittest
from jmessage import users
from jmessage import common
from conf import *
import time
import json

jmessage=common.JMessage(app_key,master_secret)
groups=jmessage.create_groups()

class TestGroups(unittest.TestCase):
    def test_create_group(self):
        group = groups.build_group(owner_username="dev_fang", name="jmessage", members_username=["xiaohuihui"],
                                        desc="jpush group")
        response = groups.create_group(group)
        print (response.content)
        self.assertEqual(response.status_code, 201)

    def test_get_group(self):
        response = groups.get_group("10426345")
        print (response.content)
        self.assertEqual(response.status_code, 200)

    def test_get_group_members(self):
        response = groups.get_group_members("10184277")
        print (response.content)
        self.assertEqual(response.status_code, 200)

    def test_get_groups_by_username(self):
        response = groups.get_groups_by_username("xiaohuihui")
        print (response.content)
        self.assertEqual(response.status_code, 200)

    def test_put_group(self):
        response = groups.get_groups_list("1", "2")
        print (response.content)
        self.assertEqual(response.status_code, 200)

    def test_put_group_members(self):
        add = [
            "usernadfsdfme", "xiaouihui"
        ]
        response = groups.put_group_members("10184271", add)
        print (response.content)
        self.assertEqual(response.status_code, 400)

    def test_delete_group(self):
        response = groups.delete_group("10184263")
        print (response.content)
        self.assertEqual(response.status_code, 403)
    

if __name__ == '__main__':
    unittest.main()