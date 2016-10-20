from jmessage import *
from jmessage import url
import json
class Message(object):
    def __init__(self,jmessage):
        self.jmessage=jmessage;


    def build_message(self, version=None, target_type=None, from_type=None, msg_type=None, target_id=None, from_id=None,
                   text=None, extras=None,from_name=None,target_name=None):
        message = {}
        message["version"] = version
        message["target_type"] = target_type
        message["from_type"] = from_type
        message["msg_type"] = msg_type
        message["target_id"] = target_id
        message["from_id"] = from_id
        if from_name is not None:
            message["from_name"] = from_name
        if target_name is not None:
            message["target_name"] = target_name
        msg_body={}
        msg_body["text"]=text
        if extras is not None:
            msg_body["extras"]=extras
        message["msg_body"] = msg_body
        return message

    def send_messages(self, messages):
         #print messages
         messages = json.dumps(messages)
         messages_url = url.IM_URL + url.MESSAGES_URL
         #print messages_url
         response = self.jmessage._request("POST", messages, messages_url)
         return response