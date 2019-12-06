import json

from apiTestIHRM.app import BASE_DIR

# login_data = [
#     ({'mobile': '13800000002', 'password': '123456'},
#      {'status_code': 200, 'success': True, 'code': 10000, 'message': '操作成功！'}),
#     ({'mobile': '13800001112', 'password': '123456'},
#      {'status_code': 200, 'success': False, 'code': 20001, 'message': '用户名或密码错误'}),
#     ({'mobile': '13800000002', 'password': 'error'},
#      {'status_code': 200, 'success': False, 'code': 20001, 'message': '用户名或密码错误'}),
#     ({},{'status_code': 200, 'success': False, 'code': 99999, 'message': '抱歉，系统繁忙，请稍后重试！'}),
#     ({'mobile': '', 'password': '123456'},
#      {'status_code': 200, 'success': False, 'code': 20001, 'message': '用户名或密码错误'}),
#     ({'mobile': '13800001112', 'password': ''},
#      {'status_code': 200, 'success': False, 'code': 20001, 'message': '用户名或密码错误'}),
#     ({'mobile': '13800000002', 'password': '123456', 'extra_param': '8888'},
#      {'status_code': 200, 'success': True, 'code': 10000, 'message': '操作成功！'}),
#     ({'password': '123456'},
#      {'status_code': 200, 'success': False, 'code': 99999, 'message': '抱歉，系统繁忙，请稍后重试！'})
# ]

login_data = [
    ({'mobile': '13800000002', 'password': '123456'},
     {'status_code': 200, 'success': True, 'code': 10000, 'message': '操作成功！'})
    ]

json_data = json.dumps(login_data)

print(json_data)

data_file = BASE_DIR + '/data/login_data.json'

with open(data_file, 'w', encoding='utf-8') as f:
    f.write(json_data)