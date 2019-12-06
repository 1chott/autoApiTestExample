import logging
import unittest

from parameterized import parameterized

from apiTestIHRM.api.emp_api import EmpApi
from apiTestIHRM.utils import assert_comment, MysqlUtils, read_add_emp_data, read_search_emp_data, read_modify_emp_data, read_delete_emp_data
from apiTestIHRM import app


class TestEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = EmpApi()
        # cls.sql_utils = MysqlUtils()   # 普通工具类的用的时候使用这行

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @parameterized.expand(read_add_emp_data)
    def test_01_add_emp(self, username, mobile, http_code, success, code, message):
        """添加员工接口测试用例"""
        logging.info('开始测试添加员工接口请求头是： {}'.format(app.HEADERS))
        response = self.emp_api.add_emp(username, mobile)
        logging.info('添加员工接口返回数据： {}'.format(response.json()))

        assert_comment(self, response, {"status_code": http_code, "success": success, "code": code, "message": message})

        app.EMP_ID = response.json().get('data').get('id')
        logging.info('获取员工id为 {}'.format(app.EMP_ID))

    @parameterized.expand(read_search_emp_data())
    def test_02_search_emp(self, http_code, success, code, message):
        """查询员工接口测试用例"""
        response = self.emp_api.search_emp()
        logging.info('查询员工接口返回数据： {}'.format(response.json()))

        assert_comment(self, response, {"status_code": http_code, "success": success, "code": code, "message": message})

    @parameterized.expand(read_modify_emp_data())
    def test_03_modify_emp(self, username, http_code, success, code, message):
        """修改员工接口测试用例"""
        response = self.emp_api.modify_emp(username)
        logging.info('修改员工接口返回数据： {}'.format(response.json()))

        assert_comment(self, response, {"status_code": http_code, "success": success, "code": code, "message": message})

        # 上下文管理工具类的用法
        with MysqlUtils(
                host="182.92.81.159",
                user="readuser",
                password="iHRM_user_2019",
                database="ihrm",
                port=3306,
                charset="utf8"
        ) as db:
            sql = 'select `username` from `bs_user` where `id`={}'.format(app.EMP_ID)
            db.execute(sql)
            self.assertEqual(username, db.fetchone()[0])

        # 查询数据库数据进行断言 数据库工具类 普通写法
        # self.sql_utils.connect_mysql()
        # sql = 'select `username` from `bs_user` where `id`={}'.format(app.EMP_ID)
        # self.sql_utils.execute_sql(sql)
        # res = self.sql_utils.get_one_result()
        # self.sql_utils.close_mysql()
        # logging.info('数据库查询结果：{}'.format(res))
        # self.assertEqual('我是那托4', res[0])

        # response = self.emp_api.search_emp()    # TODO 修改为从数据库查询对比
        # self.assertEqual('我是那托4', response.json().get('data').get('username'))

    @parameterized.expand(read_delete_emp_data())
    def test_04_delete_emp(self, http_code, success, code, message):
        """删除员工接口测试用例"""
        response = self.emp_api.delete_emp()
        logging.info('删除员工接口返回数据： {}'.format(response.json()))
        assert_comment(self, response, {"status_code": http_code, "success": success, "code": code, "message": message})
