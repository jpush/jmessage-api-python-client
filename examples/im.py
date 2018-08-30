from pprint import pprint
from context import jmessage
from jmessage.sensitiveword import SensitiveWord

def parser(resp):
    pprint(resp.status_code)
    pprint(resp.headers)
    if resp.text:
        pprint(resp.json())


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

if __name__ == '__main__':
     parser(resp)
