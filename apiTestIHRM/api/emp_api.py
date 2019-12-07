import requests

from apiTestIHRM import app


# 员工管理模块 api接口
class EmpApi:
    def __init__(self):
        # 添加员工的接口 url
        self.emp_url = 'http://182.92.81.159' + '/api/sys/user'
        # 查询、修改、删除员工的接口 url 'http://182.92.81.159' + '/api/sys/user' + user_id
        self.emp_id_url = None

    # 添加员工接口
    def add_emp(self, username, mobile):
        # Post 请求提交的数据  提交的是 json 数据
        data = {
            'username': username,
            'mobile': mobile,
            'timeOfEntry': '2019-11-05',
            'formOfEmployment': 1,
            'workNumber': '111',
            'departmentName': '财务部',
            'departmentId': '1066238836272664576',
            'correctionTime': '2019-11-29T16:00:00.000Z'
        }
        # 发起请求， 返回请求结果 便于测试用例调用，  headers 需要携带 authorization ： token  token依赖登录接口获取
        return requests.post(self.emp_url, json=data, headers=app.HEADERS)

    # 查询员工接口
    def search_emp(self):
        # 构建url
        self.emp_id_url = self.emp_url + '/' + app.EMP_ID
        # 发起请求， 返回请求结果
        return requests.get(self.emp_id_url, headers=app.HEADERS)

    # 修改员工信息接口
    def modify_emp(self, username):
        # TODO 保证健壮性， 最好加上 self.emp_id_url = self.emp_url + '/' + app.EMP_ID （如果修改前没执行过查询的话接口地址为None）
        # 发起请求，返回请求结果
        return requests.put(self.emp_id_url, json={'username': username}, headers=app.HEADERS)

    # 删除员工接口
    def delete_emp(self):
        # TODO 保证健壮性， 最好加上 self.emp_id_url = self.emp_url + '/' + app.EMP_ID （如果修改前没执行过查询的话接口地址为None）
        # 发起请求，返回请求结果
        return requests.delete(self.emp_id_url, headers=app.HEADERS)