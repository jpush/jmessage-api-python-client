from pprint import pprint
from context import jmessage, img_path
from jmessage.im import IM
from jmessage.message import Resource, Message, Model as MM

def parser(resp):
    pprint(resp.status_code)
    pprint(resp.headers)
    if resp.text:
        pprint(resp.json())

username = 'user_x'

im = IM(jmessage)

# # 获取敏感词列表
# resp = im.all_words(10)

# # 添加敏感词
# resp = im.add_words('hi')

# # 批量添加敏感词
# resp = im.add_words(['hi', 'hola'])

# # 修改敏感词
# resp = im.change_word(old='hi', new='hello')

# # 删除敏感词
# resp = im.remove_word('hi')

# # 获取敏感词功能状态
# resp = im.word_status()

# # 开启敏感词过滤
# resp = im.open_filter()

# # 关闭敏感词过滤
# resp = im.close_filer()



# # 获得 SDK-API 用户注册开关
# resp = im.sdk_status()

# # 打开 SDK-API 用户注册
# resp = im.open_sdk()

# # 关闭SDK-API用户注册
# resp = im.close_sdk()



# res = Resource(jmessage)
# msg = Message(jmessage)

# img = open(img_path, 'rb')

# mm = MM()
# mm.text('foobar') \
#     .set_from('admin', 'admin') \
#     .set_target(username, 'single') \
#     .notification(title='hello', alert='hola') \
#     .notifiable(True).offline(True)

# def upload():
#     resp = res.upload_image(img)
#     parser(resp)
#     return resp

# def up_down():
#     resp = upload()
#     media_id = resp.json()['media_id']
#     resp = res.download(media_id)
#     return resp

# def text_msg():
#     resp = msg.send(mm)
#     pprint(mm.json())
#     return resp

# def img_msg():
#     resp = upload()
#     images = resp.json()

#     mm.image(images)
#     resp = msg.send(mm)
#     pprint(mm.json())
#     return resp

# def retract_msg():
#     resp = msg.send(mm)

#     msgid = resp.json()['msg_id']
#     resp = msg.retract('admin', msgid)
#     return resp


if __name__ == '__main__':
    # resp = up_down()
    # resp = text_msg()
    # resp = img_msg()
    # resp = retract_msg()
    parser(resp)
