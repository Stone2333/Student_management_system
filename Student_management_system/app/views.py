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
                'msg': '请求失败',
                'code': 404
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
            'msg': '用户名和密码不能为空',
            'code': 13
        }
        return JsonResponse(data)
    if db_user == ():
        data = {
            'msg': '用户不存在',
            'code': 10,
        }
        return JsonResponse(data)
    elif username == db_user[0] and password == db_user[1]:
        data = {
            'username': username,
            'msg': '登录成功',
            'code': 12,
        }
        return JsonResponse(data)
    else:
        data = {
            'msg': '用户名或密码错误',
            'code': 11,
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
def student_info_id(request):
    '''根据id查询学生信息'''
    student_id = request.POST.get('student_id')
    student_info = mysql_query.select_student_information(student_id)
    print(student_info)
    if student_info == ():
        data = {
            'msg': '学号不存在',
            'code': 20,
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