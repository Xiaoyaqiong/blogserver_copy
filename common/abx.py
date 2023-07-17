import requests
from config.ProjectConfig import VBConfig
from urllib import parse
from common.testLogin import VBLogin
def mangerUser():
    contentType = "application/x-www-form-urlencoded"
    url = VBConfig.URL + '/article/'
    data ={
                "id": "-1",
                "title": "haha23457899",
                "mdContent": "haha234578",
                "htmlContent": "<p>haha234578</p>\n",
                "state": "1",
                "cid":"91",
                "dynamicTags": "",
            }
    postData = parse.urlencode(data)
    cookie= VBLogin.managerUser()
    header = {
        "Content-Type": contentType,
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64;rv: 109.0) Gecko / 20100101Firefox / 114.0",
    }
    request = requests.post(url=url, data=postData, headers=header,cookies=cookie)
    print(request.text)

if __name__ == '__main__':
    mangerUser()