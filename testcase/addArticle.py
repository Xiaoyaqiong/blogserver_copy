import unittest
import json
import requests
from urllib import parse
# from common.db_funcs import init_db_category,insert_category
from common.HttpReq import VBReq
from common.wrapers import skip_related_case,write_case_log
from config.ProjectConfig import VBConfig
from ddt import ddt,data,unpack
from testcase.data.add_article import ADD_DATA

# @ddt
# class addArticle(unittest.TestCase):
#     addurl=VBConfig.URL+'/article/'
#
#     @classmethod
#     def setUp(self) :
#         print("开始")
#
#     @classmethod
#     def tearDown(self) :
#         print("结束")
#
#     # 选择一个已存在的栏目分类，输入有效的文章标题和内容
#     @data(ADD_DATA['test_add_art_001'])
#     @unpack
#     @write_case_log()
    # def test_add_art_001(self,req_data,res_key,res_value):
    #     print(req_data,res_key,res_value,'我是1')
    #     # insert_category()
    #     # 新增一篇文章
    #     postData = parse.urlencode(req_data)
    #     result = VBReq.post(url=addArticle.addurl,data=postData)
    #     # print(result.text)
    #     # print(type(result))
    #     result = json.loads(result.text)
    #     # print(type(result))
    #     # print(result['status'])
    #     self.assertEqual(result[res_key], res_value)

    # 输入同样的文章标题和内容和栏目
    # @skip_related_case(related_case_name='test_add_art_001')
    # @data(ADD_DATA['test_add_art_002'])
    # @unpack
    # @write_case_log()
    # def test_add_art_002(self,req_data,res_key,res_value):
    #     print(req_data,res_key,res_value,'我是2')
    #     # 重复新增同一文章
    #     postData = parse.urlencode(req_data)
    #     result = VBReq.post(url=addArticle.addurl, data=postData)
    #     print('cuowu')
    #     result = json.loads(result.text)
    #     # print(type(result))
    #     # print(result['status'])
    #     self.assertEqual(result[res_key], res_value)
    #
    # # 不选择栏目，其他参数正常输入
    # # 不输入文章标题,其他参数正常输入
    # # 不输入文章内容,其他参数正常输入
    # @data(ADD_DATA['test_add_art_003'],ADD_DATA['test_add_art_004'],ADD_DATA['test_add_art_005'])
    # @unpack
    # @write_case_log()
    # def test_add_art_003(self,req_data,res_key,res_value):
    #     print(req_data, res_key, res_value, '我是3')
    #     postData = parse.urlencode(req_data)
    #     result = VBReq.post(url=addArticle.addurl, data=postData)
    #     result = json.loads(result.text)
    #     self.assertEqual(result[res_key], res_value)
    #
    # @data(ADD_DATA['test_add_art_006'],ADD_DATA['test_add_art_007'],ADD_DATA['test_add_art_008'])
    # @unpack
    # @write_case_log()
    # def test_add_art_004(self,req_data,res_key,res_value):
    #     print(req_data, res_key, res_value, '我是4')
    #     postData = parse.urlencode(req_data)
    #     result = VBReq.post(url=addArticle.addurl, data=postData)
    #     result = json.loads(result.text)
    #     self.assertEqual(result[res_key], res_value)

# if __name__ == '__main__':
#     suite=unittest.TestSuite()
#     suite.addTest(addArticle("test_add_art_001"))
#     # suite.addTest(addArticle("test_add_art_002"))
#     # suite.addTest(addArticle("test_add_art_003"))
#     # suite.addTest(addArticle("test_add_art_004"))
#     runner=unittest.TextTestRunner()
#     test_result=runner.run(suite)