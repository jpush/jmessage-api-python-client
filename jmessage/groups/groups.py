from jmessage import *
from jmessage import url
import json
class Group(object):
    def __init__(self,jmessage):
        self.jmessage=jmessage;

    def build_group(self, owner_username=None, name=None, members_username=None, desc=None):
        group = {}
        if owner_username is not None:
            group["owner_username"] = owner_username
        if name is not None:
            group["name"] = name
        if members_username is not None:
            group["members_username"] = members_username
        if desc is not None:
            group["desc"] = desc
        return group

    def create_group(self,group):
        #print group
        group_url=url.IM_URL+url.GROUPS_URL
        #print group_url
        body=json.dumps(group)
        response = self.jmessage._request("POST", body, group_url)
        return response

    def get_group(self,gid):
        #print gid
        group_url=url.IM_URL+url.GROUPS_URL+gid
        #print group_url
        body=None
        response = self.jmessage._request("GET", body, group_url)
        return response

    def put_group(self,gid,group):
        #print gid
        group_url=url.IM_URL+url.GROUPS_URL+gid
        #print group_url
        body=json.dumps(group)
        response = self.jmessage._request("PUT", body, group_url)
        return response

    def delete_group(self, gid):
        #print gid
        group_url=url.IM_URL+url.GROUPS_URL+gid
        #print group_url
        body=None
        response = self.jmessage._request("DELETE", body, group_url)
        return response

    def put_group_members(self, gid, add , remove=None):
        #print gid
        group_url=url.IM_URL+url.GROUPS_URL+gid+"/members"
        #print group_url
        members={}
        members["add"]=add
        body= json.dumps(members)
        #print body
        response = self.jmessage._request("POST", body, group_url)
        return response

    def get_group_members(self, gid):
        #print gid
        group_url=url.IM_URL+url.GROUPS_URL+gid+"/members"
        #print group_url
        body= None
        response = self.jmessage._request("GET", body, group_url)
        return response

    def get_groups_by_username(self, username):
        #print username
        group_url=url.IM_URL+url.REGIST_USER_URL+username+"/groups/"
        #print group_url
        body= None
        response = self.jmessage._request("GET", body, group_url)
        return response

    def get_groups_list(self, start, count):
        group_url=url.IM_URL+url.GROUPS_URL+"?start="+start+"&count="+count
        #print group_url
        body= None
        response = self.jmessage._request("GET", body, group_url)
        return response




















