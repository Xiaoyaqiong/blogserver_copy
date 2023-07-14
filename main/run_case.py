import unittest

# 创建测试集合
suite=unittest.TestSuite()
# 识别所有article结尾的py文件作为测试用例
tests=unittest.defaultTestLoader.discover('..\\testcase',pattern='*leArticle.py')

# 运行测试用例
suite.addTest(tests)
runner=unittest.TextTestRunner()
result=runner.run(suite)