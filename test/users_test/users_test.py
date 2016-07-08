import unittest
from jmessage import users
from jmessage import common
from conf import *
import random
import string

class TestUsers(unittest.TestCase):
  username = string.join(random.sample(['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e','d', 'c', 'b', 'a'], 8)).replace(' ', '')
  jmessage = common.JMessage(app_key, master_secret)
  users = jmessage.create_users()

  def test_user(self):
      print (self.username)
      user = [self.users.build_user(self.username, "password")]
      response = self.users.regist_user(user)
      print (dir(response))
      print (response.text)
      self.assertEqual(response.status_code, 201)