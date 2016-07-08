from jmessage import *
from jmessage import url
import json
class User(object):
    def __init__(self,jmessage):
        self.jmessage=jmessage;

    def build_user(self, username=None, password=None, nickname=None, star=None, avatar=None, gender=None,
                   signature=None, region=None, address=None, mtime=None, ctime=None):
        user={}
        if username is not None:
            user["username"]=username
        if password is not None:
            user["password"]=password
        if nickname is not None:
            user["nickname"]=nickname
        if star is not None:
            user["star"]=star
        if avatar is not None:
            user["avatar"]=avatar
        if gender is not None:
            user["gender"]=gender
        if signature is not None:
            user["signature"]=signature
        if region is not None:
            user["region"]=region
        if address is not None:
            user["address"]=address
        if mtime is not None:
            user["mtime"]=mtime
        if ctime is not None:
            user["ctime"]=ctime
        return user

    def regist_user(self, users):
         #print users
         users = json.dumps(users)
         #print users
         regist_url = url.IM_URL + url.REGIST_USER_URL
         #print regist_url
         response = self.jmessage._request("POST", users, regist_url)
         return response

    def regist_admin(self, admins):
        #print admins
        admins = json.dumps(admins)
        #print admins
        regist_url = url.IM_URL + url.REGIST_ADMIN_URL
        #print regist_url
        response = self.jmessage._request("POST", admins, regist_url)
        return response

    def get_user_by_username(self,username):
        #print username
        regist_url = url.IM_URL + url.REGIST_USER_URL+username
        #print regist_url
        body=None
        response = self.jmessage._request("GET",body, regist_url)
        return response

    def put_user_password(self, username, password):
        #print username
        regist_url = url.IM_URL + url.REGIST_USER_URL+username+"/password"
        #print regist_url
        new_password={}
        new_password["new_password"]=password
        body=json.dumps(new_password)
        response = self.jmessage._request("PUT",body,regist_url)
        return response

    def delete_user_by_username(self, username):
        #print username
        regist_url = url.IM_URL + url.REGIST_USER_URL+username
        #print regist_url
        body=None
        response = self.jmessage._request("DELETE",body,regist_url)
        return response

    def blacklist_user_by_username(self, username):
        #print username
        regist_url = url.IM_URL + url.REGIST_USER_URL+username+"/blacklist"
        #print regist_url
        body=None
        response = self.jmessage._request("PUT",body,regist_url)
        return response

    def blacklist_user_by_username(self, username):
        #print username
        regist_url = url.IM_URL + url.REGIST_USER_URL+username+"/blacklist"
        #print regist_url
        body=username
        response = self.jmessage._request("PUT",body,regist_url)
        return response


    def delete_blacklist_by_username(self, username):
        #print username
        regist_url = url.IM_URL + url.REGIST_USER_URL+username+"/blacklist"
        #print regist_url
        body=username
        response = self.jmessage._request("DELETE",body,regist_url)
        return response

    def get_blacklist(self, username):
        #print username
        regist_url = url.IM_URL + url.REGIST_USER_URL+username+"/blacklist"
        #print regist_url
        body=username
        response = self.jmessage._request("GET",body,regist_url)
        return response

    def get_users(self, start,count):
        regist_url = url.IM_URL + url.REGIST_USER_URL+"?start="+start+"&count="+count
        #print regist_url
        body=None
        response = self.jmessage._request("GET",body,regist_url)
        return response















