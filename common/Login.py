import json
from config.ProjectConfig import VBConfig
from urllib import parse
from common.HttpReq import VBReq

class Login(object):
    def managerUser(self):
        url = VBConfig.URL + '/login'
        data = {
            "username": "sang",
            "password": "123"
        }
        postData = parse.urlencode(data)
        request = VBReq.post(url=url, data=postData, cookies=None)
        result = json.loads(request.text)
        print(result)
        if(result['status']=='success'):
            managerCookie = request.cookies.get_dict()
            return managerCookie
        else:
            return


    def ordinaryUser(self):
        url = VBConfig.URL + '/login'
        data = {
            "username": "qiaofeng",
            "password": "123"
        }
        postData = parse.urlencode(data)
        request = VBReq.post(url=url, data=postData, cookies=None)
        result = json.loads(request.text)
        print(result)
        if (result['status'] == 'success'):
            managerCookie = request.cookies.get_dict()
            return managerCookie
        else:
            return


VBLogin = Login()

