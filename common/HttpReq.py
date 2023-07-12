import requests
from common.logger import write_log
class HttpReq(object):
    def __init__(self):
        self.headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "JSESSIONID=170B0D1923A96E115DEEE687245F511D",
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64;rv: 109.0) Gecko / 20100101Firefox / 114.0",
        }
    # get
    def get(self,url='',params='',cookies=None):
        response=requests.get(url=url,params=params,cookies=cookies,headers=self.headers)
        return response

    # post
    def post(self,url='',data='',cookies=None):
        try:
            response = requests.post(url=url, data=data, cookies=cookies, headers=self.headers)
            return response
        except Exception as e:
            write_log.error("post请求失败".format(e))

    # put
    def put(self, url='',params='',data='', cookies=None):
        response = requests.put(url=url,params=params, data=data, cookies=cookies, headers=self.headers)
        return response

    #delete
    def delete(self,url='',params='',cookies=None):
        response =requests.delete(url=url,params=params,cookies=cookies,headers=self.headers)
        return response

VBReq=HttpReq()