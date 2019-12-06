import unittest
import time

from BeautifulReport import BeautifulReport

from apiTestIHRM.script.test_a_login import TestLogin
from apiTestIHRM.script.test_b_emp import TestEmp

# 实例化测试套件
suite = unittest.TestSuite()

# 添加测试用例
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))

# 报告路径
report_file = './report/iHRM{}.html'.format(time.strftime('%Y%m%d_%H%M%S'))

# 调用第三方包， 生成测试报告
result = BeautifulReport(suite)
result.report('iHRM测试报告', report_file)
