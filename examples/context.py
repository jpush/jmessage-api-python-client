import os, sys


BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE)


from config import app_key, master_secret
from jmessage import JMessage

jmessage = JMessage(app_key, master_secret)

img_path = os.path.join(BASE, 'jiguang.png')
