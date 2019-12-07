import pymysql
import json

from requests import Response
from apiTestIHRM import app

# 本项目登陆通用断言方法
def assert_comment(self, response: Response, expected_data: dict):
    self.assertEqual(expected_data.get('status_code'), response.status_code)
    self.assertEqual(expected_data.get('code'), response.json().get('code'))
    self.assertEqual(expected_data.get('success'), response.json().get('success'))
    self.assertIn(expected_data.get('message'), response.json().get('message'))


# 数据库工具类， 高级写法 使用 上下文管理器 __enter__  和  __exit__
# 调用 with MysqlUtils(host, user, password, database, port, charset) as db:
#     db.execute()     db.fetchone()
class MysqlUtils:
    def __init__(self, host, user, password, database, port, charset):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            charset=charset
        )

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


# 读取添加员工测试数据
def read_add_emp_data():
    data_path = app.BASE_DIR + '/data/emp_data.json'
    with open(data_path, 'r', encoding='utf-8')as f:
        add_emp_data = json.load(f).get('add_emp')
        add_emp_data = list(add_emp_data.values())
        params = []
        add_emp_data.pop(0)   # TODO 被删除的数据为测试数据标题
        params.append(add_emp_data)
        print(params)
        return params   # [['那托5', '13300133005', 200, True, 10000, '操作成功！']]


# 读取查询员工测试数据
def read_search_emp_data():
    data_path = app.BASE_DIR + '/data/emp_data.json'
    with open(data_path, 'r', encoding='utf-8')as f:
        search_emp_data = json.load(f).get('search_emp')
        search_emp_data = list(search_emp_data.values())
        params = []
        search_emp_data.pop(0)   # TODO 被删除的数据为测试数据标题
        params.append(search_emp_data)
        print(params)
        return params   # [[200, True, 10000, '操作成功！']]


# 读取修改员工测试数据
def read_modify_emp_data():
    data_path = app.BASE_DIR + '/data/emp_data.json'
    with open(data_path, 'r', encoding='utf-8')as f:
        modify_emp_data = json.load(f).get('modify_emp')
        modify_emp_data = list(modify_emp_data.values())
        params = []
        modify_emp_data.pop(0)   # TODO 被删除的数据为测试数据标题
        params.append(modify_emp_data)
        print(params)
        return params   # [['我是那托5', 200, True, 10000, '操作成功！']]


# 读取删除员工测试数据
def read_delete_emp_data():
    data_path = app.BASE_DIR + '/data/emp_data.json'
    with open(data_path, 'r', encoding='utf-8')as f:
        delete_emp_data = json.load(f).get('delete_emp')
        delete_emp_data = list(delete_emp_data.values())
        params = []
        delete_emp_data.pop(0)   # TODO 被删除的数据为测试数据标题
        params.append(delete_emp_data)
        print(params)
        return params   # [[200, True, 10000, '操作成功！']]


# 调试用
if __name__ == '__main__':
    read_delete_emp_data()


# # 数据库工具类 普通低级写法
# class MysqlUtils():
#     def __init__(self):
#         self.conn = None
#         self.cursor = None
#
#     # 连接数据库
#     def connect_mysql(self):
#         self.conn = pymysql.connect(
#             host="182.92.81.159",
#             user="readuser",
#             password="iHRM_user_2019",
#             database="ihrm",
#             port=3306,
#             charset="utf8"
#         )
#
#         self.cursor = self.conn.cursor()
#
#     # 执行sql语句
#     def execute_sql(self, sql):
#         self.cursor.execute(sql)
#
#     # 获取一条查询结果
#     def get_one_result(self):
#         return self.cursor.fetchone()
#
#     # 获取所有查询结果
#     def get_all_result(self):
#         return self.cursor.fetchall()
#
#     # 关闭资源
#     def close_mysql(self):
#         if self.cursor:
#             self.cursor.close()
#             self.cursor = None
#
#         if self.conn:
#             self.conn.close()
#             self.conn = None
