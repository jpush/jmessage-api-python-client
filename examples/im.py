from pprint import pprint
from context import jmessage, img_path
from jmessage.sensitiveword import SensitiveWord
from jmessage.resource import Resource
from jmessage.message import Message, Model as MM

def parser(resp):
    pprint(resp.status_code)
    pprint(resp.headers)
    if resp.text:
        pprint(resp.json())

username = 'user_x'

sw = SensitiveWord(jmessage)

# # 获取敏感词列表
# resp = sw.all(10)

# # 添加敏感词
# resp = sw.add('hi')

# # 批量添加敏感词
# resp = sw.add(['hi', 'hola'])

# # 修改敏感词
# resp = sw.change(old='hi', new='hello')

# # 删除敏感词
# resp = sw.remove('hi')

# # 获取敏感词功能状态
# resp = sw.status()

# # 开启敏感词过滤
# resp = sw.open()

# # 关闭敏感词过滤
# resp = sw.close()

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
