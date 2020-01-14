from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from mysql import mysql_query
import json


# Create your views here.
def login(request):
    return render(request, 'user/login.html')
    # check = login_check(request)
    # print(check.json)
    # if check['code'] == 10:
    #     data = '用户不存在'
    #     return HttpResponse(data)
    # elif check['code'] == 12:
    #     return render(request, 'index/index.html')
    # else:
    #     data = '用户名或密码错误'
    #     return HttpResponse(data)
    #

def index(request):
    return render(request, 'index/index.html',)



def request_check(func):
    '''请求装饰器，可改为中间件'''
    def request(request):
        if request.method == 'POST':
            # username = request.POST.get('username')
            # data = {
            #     'msg': '请求成功',
            #     'code': 200,
            #     'username': username
            # }
            return func(request)
        # elif request.method == 'GET':
        #     data = {
        #         'msg': '请求方法错误',
        #         'code': 500
        #     }
        #     return JsonResponse(data)
        else:
            data = {
                'errCode': 404,
                'errDesc': "网页不存在",
            }
            return JsonResponse(data)
    return request


@request_check
def login_check(request):
    '''登录验证'''
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        db_user = mysql_query.login(username)[0]
    except:
        data = {
            "errCode": "11",
            "errDesc": "用户名和密码不能为空"
        }
        return JsonResponse(data)
    if db_user == ():
        data = {
            "errCode": "10",
            "errDesc": "用户不存在",
        }
        return JsonResponse(data)
    elif username == db_user['username'] and password == db_user['password']:
        data = {
            "errCode": "0",
            "errDesc": "操作成功",
            "data": username
        }
        return JsonResponse(data)
    else:
        data = {
            "errCode": "12",
            "errDesc": "用户名或密码错误",
        }
        return JsonResponse(data)


@request_check
def student_all(request):
    '''获取所有学生信息'''
    student_info = mysql_query.select_student_all()
    data = {
        'msg': '成功',
        'code': 200,
        'data': student_info
    }
    return JsonResponse(data)


@request_check
def student_info(request):
    '''根据id、name、address查询学生信息'''
    student_id = request.POST.get('student_id')
    student_name = request.POST.get('student_name')
    student_address = request.POST.get('student_address')
    student_info_id = mysql_query.select_student_information(student_id)
    student_info_name = mysql_query.select_student_name(student_name)
    student_info_address = mysql_query.select_student_name(student_address)
    if student_info_id == ():
        data = {
            "errCode": "0",
            "errDesc": "操作成功",
            "data": 'null'
        }
        return JsonResponse(data)
    elif student_info_name == ():
        data = {
            'msg': '姓名不存在',
            'code': 30,
        }
        return JsonResponse(data)
    elif student_info_address == ():
        data = {
            'msg': '地址不存在',
            'code': 40,
        }
        return JsonResponse(data)

    else:
        data ={
            'msg': '成功',
            'code': 200,
            'data': student_info
        }
        return JsonResponse(data)



def student_info_name(request):
    '''根据名字查询学生信息'''
    student_name = request.POST.get('student_name')
    student_info = mysql_query.select_student_name(student_name)
    if student_info == ():
        data = {
            'msg': '学生姓名不存在',
            'code': 21,
        }
        return JsonResponse(data)
    else:
        data = {
            'msg': '成功',
            'code': 200,
            'data': student_info
        }
        return JsonResponse(data)


def student_info_address(request):
    '''根据地址查询学生信息'''
    student_address = request.POST.get('student_address')
    student_info = mysql_query.select_student_address(student_address)
    if student_info == ():
        data = {
            'msg': '地区不存在',
            'code': 30,
        }
        return JsonResponse(data)
    else:
        data = {
            'msg': '成功',
            'code': 200,
            'data': student_info
        }
        return JsonResponse(data)