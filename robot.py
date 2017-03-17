import itchat
from itchat.content import *
from datetime import datetime
import requests
import json

OPENROBOT = False


@itchat.msg_register(TEXT,  isFriendChat=True)
def tuling(msg):
    global OPENROBOT
    info = itchat.search_friends(userName=msg.get('FromUserName'))
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    try:
        inputdata = {
            "perception": {
                "inputText": {
                    "text": msg['Content']
                },
            },
            "userInfo": {
                "apiKey": "a2843c0831274db8af25eafb2ab09036",
                "userId": 1
            }
        }
        hour = datetime.now().hour
        minute = datetime.now().minute
        response = requests.post(url, data=json.dumps(inputdata))
        data = json.loads(response.text)
        reply = data['results'][-1]['values']['text']
    except Exception as e:
        return '额。。被玩坏了'
    if msg['Content'] == '滚蛋吧机器人':
        OPENROBOT = False
        return '%s,再见！' % info['NickName']
    if msg['Content'] == '召唤机器人' or OPENROBOT is True:
        OPENROBOT = True
        if msg['Content'] == '召唤机器人':
            return '召唤成功！回复[滚蛋吧机器人]，唤醒人工服务'
        else:
            return reply
    if hour >= 23 or hour <= 5:
        return '半智能机器人：现在是%d点%d分，%s晚安，机器人也是要休息的' % (hour, minute, info['NickName'])


@itchat.msg_register(PICTURE, isFriendChat=True)
def relpy_pic(msg):
    hour = datetime.now().hour
    minute = datetime.now().minute
    info = itchat.search_friends(userName=msg.get('FromUserName'))
    if hour >= 23 or hour <= 5:
        return '半智能机器人：现在是%d点%d分，%s晚安，机器人也是要休息的' % (hour, minute, info['NickName'])


itchat.auto_login()
itchat.run()
