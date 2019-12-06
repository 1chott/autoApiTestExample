import requests


class LoginApi:
    def __init__(self):
        # 登陆接口 url
        self.login_url = 'http://182.92.81.159' + '/api/sys/login'
        # 请求头
        self.headers = {'Content-Type': 'application/json'}

    # 登陆请求
    def login(self, login_data):
        return requests.post(self.login_url, json=login_data, headers=self.headers)