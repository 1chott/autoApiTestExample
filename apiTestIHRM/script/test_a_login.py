import unittest
import logging
import json

from parameterized import parameterized

from apiTestIHRM.api.login_api import LoginApi
from apiTestIHRM.utils import assert_comment
from apiTestIHRM import app


# 登陆接口的测试用例集
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    # 文件数据读取，可封装到utils模块，进行调用
    data_path = app.BASE_DIR + '/data/login_data.json'
    with open(data_path, 'r')as f:
        login_data = json.load(f)
        print(login_data)

    # 参数化第三方模块 传入的数据需要是一个可迭代对象
    @parameterized.expand(login_data)
    def test_login(self, login_data, expected_data):
        """
            登陆测试用例，数据：
        """

        logging.info('开始测试登陆接口：请求数据是:【{}】'.format(login_data))
        # 调用接口， 发起请求
        response = self.login_api.login(login_data)

        logging.info('登陆接口返回的数据是：【{}】'.format(response.json()))

        # 因为加了参数化， 所以加了条件判断， 只有登录成功的时候才能获取到 token不为None
        token_data = response.json().get('data')
        if token_data:
            # 获取到了token才进行token构建
            token = 'Bearer ' + token_data
            # 设置全局变量， 保存请求头
            app.HEADERS = {'Content-Type': 'application/json',
                           'Authorization': token}

            logging.info('全局变量HEADERS为： {}'.format(app.HEADERS))
        # 调用封装好的断言工具
        assert_comment(self, response, expected_data)
        logging.info('登陆接口断言通过。')
