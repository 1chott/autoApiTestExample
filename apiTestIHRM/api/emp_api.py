import requests

from apiTestIHRM import app


class EmpApi:
    def __init__(self):
        self.emp_url = 'http://182.92.81.159' + '/api/sys/user'
        self.emp_id_url = None

    # 添加员工接口
    def add_emp(self, username, mobile):
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

        return requests.post(self.emp_url, json=data, headers=app.HEADERS)

    # 查询员工接口
    def search_emp(self):
        self.emp_id_url = self.emp_url + '/' + app.EMP_ID
        return requests.get(self.emp_id_url, headers=app.HEADERS)

    # 修改员工信息接口
    def modify_emp(self, username):
        return requests.put(self.emp_id_url, json={'username': username}, headers=app.HEADERS)

    # 删除员工接口
    def delete_emp(self):
        return requests.delete(self.emp_id_url, headers=app.HEADERS)