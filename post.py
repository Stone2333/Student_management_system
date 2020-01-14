import requests
import json
def post():
    # join_url = 'student_all'
    join_url = 'login_check'
    # join_url = 'student_info_address'
    utl = 'http://127.0.0.1:8000/api/' + join_url
    headers = {
        # "Content-Type": "application/form-data",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }

    data = {
        'username': 'stone',
        'password': '1',
        'student_address':'成都'
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

if __name__ == '__main__':
   post()
   # get()
   # put()