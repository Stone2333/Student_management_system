import requests
import json
def post():
    # join_url = 'student_all'
    # join_url = 'login_check'
    # join_url = 'student_info'
    join_url = 'student_add'
    utl = 'http://127.0.0.1:8000/' + join_url
    print(utl)
    headers = {
        # "Content-Type": "application/form-data",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }



    data = {}
    # data = {
    #     "username": "",
    #     "password": "1",
    #     "student_id": "666",
    #     "student_name": '张三',
    #     "student_address": "成都"
    #
    # }


    data = {
        'student_name': '1',
        'student_id': '1',
        'gender': '1',
        'birth': '1',
        'departments': '1',
        'address': '1'
    }
    # data = {'student_address': '成都'}

    response = requests.post(url=utl, headers=headers, data=data)
    print('请求方式post:')
    print(response.json())


def get():
    # join_url = 'login_check'
    join_url = 'student_info_id'
    utl = 'http://127.0.0.1:8000/api/' + join_url
    headers = {
        # "Content-Type": "application/json;charset=UTF-8",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    response = requests.get(utl, headers)
    print('请求方式get:')
    print(response.json())


def put():
    # join_url = 'login_check'
    join_url = 'student_info_id'
    utl = 'http://127.0.0.1:8000/api/' + join_url
    headers = {
        # "Content-Type": "application/json;charset=UTF-8",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    response = requests.put(utl, headers)
    print('请求方式put:')
    print(response.json())

# string = eval("[[1,2,3],[1,2,2]]")
# print(type(string))
# for a in string:
#     print(a)
#
# a =  "1'1'1'1'1"
# c = a.replace('\'','\"')
# print(c)
if __name__ == '__main__':
   post()
# #    # get()
# #    # put()
