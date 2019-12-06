import unittest
import logging
import json

from parameterized.parameterized import parameterized

from apiTestIHRM.api.login_api import LoginApi
from apiTestIHRM.utils import assert_comment
from apiTestIHRM import app


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

    data_path = app.BASE_DIR + '/data/login_data.json'
    with open(data_path, 'r')as f:
        login_data = json.load(f)
        print(login_data)

    @parameterized.expand(login_data)
    def test_login(self, login_data, expected_data):
        """
            登陆测试用例，数据：
        """

        logging.info('开始测试登陆接口：请求数据是:【{}】'.format(login_data))
        response = self.login_api.login(login_data)
        logging.info('登陆接口返回的数据是：【{}】'.format(response.json()))

        try:
            token = 'Bearer ' + response.json().get('data')

            app.HEADERS = {'Content-Type': 'application/json',
                   'Authorization': token}

            logging.info('全局变量HEADERS为： {}'.format(app.HEADERS))
        except Exception as e:
            pass

        assert_comment(self, response, expected_data)
        logging.info('登陆接口断言通过。')