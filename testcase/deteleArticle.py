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
from testcase.data.detele_article import DELETE_DATA


@ddt
class deteleArticle(unittest.TestCase):
    deteleurl=VBConfig.URL+'/article/dustbin'

    @classmethod
    def setUp(self) :
        print("开始")

    @classmethod
    def tearDown(self) :
        print("结束")

    # state:-1（全部文章）,其他参数正常
    # @data(DELETE_DATA['test_delete_article_001'])
    # @unpack
    # @write_case_log()
    # def test_delete_article_001(self,req_data,res_key,res_value):
    #     print(req_data,res_key,res_value,'我是1')
    #     # insert_category()
    #     result = VBReq.put(url=deteleArticle.deteleurl,data=req_data)
    #
    #     result = json.loads(result.text)
    #
    #     self.assertEqual(result[res_key], res_value)
    #
    # @data(DELETE_DATA['test_delete_article_002'],
    #       DELETE_DATA['test_delete_article_003'], DELETE_DATA['test_delete_article_004'])
    # @unpack
    # @write_case_log()
    # def test_delete_article_002(self, req_data, res_key, res_value):
    #     print(req_data, res_key, res_value, '我是2')
    #     result = VBReq.put(url=deteleArticle.deteleurl, data=req_data)
    #     result = json.loads(result.text)
    #     self.assertEqual(result[res_key], res_value)

    # 不传state
    @data(DELETE_DATA['test_delete_article_005'])
    @unpack
    @write_case_log()
    def test_delete_article_003(self, req_data, res_key, res_value):
        print(req_data, res_key, res_value, '我是2')
        result = VBReq.put(url=deteleArticle.deteleurl, data=req_data)
        result = json.loads(result.text)
        self.assertEqual(result[res_key], res_value)

    # aid: 用户发表的文章编号, 其他参数正常
    # aid: 用户发表的多篇文章编号, 其他参数正常
    @data(DELETE_DATA['test_delete_article_006'],DELETE_DATA['test_delete_article_007'])
    @unpack
    @write_case_log()
    def test_delete_article_004(self, req_data, res_key, res_value):
        print(req_data, res_key, res_value, '我是2')
        result = VBReq.put(url=deteleArticle.deteleurl, data=req_data)
        result = json.loads(result.text)
        self.assertEqual(result[res_key], res_value)

    @data(DELETE_DATA['test_delete_article_008'], DELETE_DATA['test_delete_article_009'])
    @unpack
    @write_case_log()
    def test_delete_article_005(self, req_data, res_key, res_value):
        print(req_data, res_key, res_value, '我是2')
        result = VBReq.put(url=deteleArticle.deteleurl, data=req_data)
        result = json.loads(result.text)
        self.assertEqual(result[res_key], res_value)


if __name__ == '__main__':
    suite=unittest.TestSuite()
    # suite.addTest(deteleArticle("test_delete_article_001"))
    # suite.addTest(deteleArticle("test_delete_article_002"))
    suite.addTest(deteleArticle("test_delete_article_003"))
    suite.addTest(deteleArticle("test_delete_article_004"))
    suite.addTest(deteleArticle("test_delete_article_005"))
    runner=unittest.TextTestRunner()
    test_result=runner.run(suite)