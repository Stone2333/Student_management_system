from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from mysql import mysql_query, mysql_insert, mysql_update, mysql_delete
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

def add(request):
    return render(request, 'add/add.html')

def delete(request):
    return render(request, 'delete/delete.html')


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
        elif request.method == 'GET':
            data = {
                'errCode': 500,
                'errDesc': "请求方式错误",
            }
            return JsonResponse(data)
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
    if username == '' or password == '':
        data = {
            "errCode": "11",
            "errDesc": "用户名或密码不能为空"
        }
        return JsonResponse(data)
    else:
        try:
            db_user = mysql_query.login(username)[0]
        except:
            db_user = db_user = mysql_query.login(username)
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
        "errCode": "0",
        "errDesc": "操作成功",
        "data":student_info
    }
    return JsonResponse(data)



# @request_check
# class Student:
#     def __init__(self, student_id, student_name, student_address):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_address = student_address
#
#     def studetn_info_student_id(self, request):
#         student_id = request.POST.get('student_id')
#         student_info_id = mysql_query.select_student_information(student_id)

@request_check
def student_info_student_id(request):
    '''根据id查询学生信息'''
    student_id = request.POST.get('student_id')
    if student_id == None:
        data = {
            "errCode": "50",
            "errDesc": "请求信息错误",
        }
        return JsonResponse(data)
    else:
        student_info_id = mysql_query.select_student_information(student_id)
        if student_info_id == ():
            data = {
                "errCode": "20",
                "errDesc": "学生学号不存在",
            }
            return JsonResponse(data)
        else:
            data = {
                "errCode": "0",
                "errDesc": "操作成功",
                "data": student_info_id
            }
            return JsonResponse(data)


@request_check
def student_info_student_name(request):
    '''根据name查询学生信息'''
    student_name = request.POST.get('student_name')
    if student_name == None:
        data = {
            "errCode": "50",
            "errDesc": "请求信息错误",
        }
        return JsonResponse(data)
    else:
        student_info_name = mysql_query.select_student_name(student_name)
        if student_info_name == ():
            data = {
                "errCode": "21",
                "errDesc": "学生姓名不存在",
            }
            return JsonResponse(data)
        else:
            data = {
                "errCode": "0",
                "errDesc": "操作成功",
                "data": student_info_name
            }
            return JsonResponse(data)

@request_check
def student_info_student_address(request):
    '''根据address查询学生信息'''
    student_address = request.POST.get('student_address')
    print(student_address)
    if student_address == None:
        data = {
            "errCode": "50",
            "errDesc": "请求信息错误",
        }
        return JsonResponse(data)
    else:
        student_info_address = mysql_query.select_student_address(student_address)
        if student_info_address == ():
            data = {
                "errCode": "22",
                "errDesc": "地址不存在",
            }
            return JsonResponse(data)
        else:
            data = {
                "errCode": "0",
                "errDesc": "操作成功",
                "data": student_info_address
            }
            return JsonResponse(data)


@request_check
def student_info_student_departments(request):
    '''根据departments查询学生信息'''
    student_departments = request.POST.get('student_departments')
    print(student_info_student_departments)
    if student_departments == None:
        data = {
            "errCode": "50",
            "errDesc": "请求信息错误",
        }
        return JsonResponse(data)
    else:
        student_info_departments = mysql_query.select_student_departments(student_departments)
        if student_info_departments == ():
            data = {
                "errCode": "22",
                "errDesc": "地址不存在",
            }
            return JsonResponse(data)
        else:
            data = {
                "errCode": "0",
                "errDesc": "操作成功",
                "data": student_info_departments
            }
            return JsonResponse(data)



def student_add(request):
    '''新增'''
    student_id = request.POST.get('student_id')
    student_name = request.POST.get('student_name')
    gender = request.POST.get('gender')
    birth = request.POST.get('birth')
    departments = request.POST.get('departments')
    address = request.POST.get('address')
    db_student_id = mysql_query.select_student_information(student_id)
    if student_id == None or student_name == None or gender == None or birth == None or departments == None or address == None:
        data = {
            "errCode": "50",
            "errDesc": "请求信息错误"
        }
        return JsonResponse(data)
    if db_student_id != ():
        data = {
            "errCode": "60",
            "errDesc": "学号已存在"
        }
        return JsonResponse(data)
    else:
        mysql_insert.insert_student_information(student_name, student_id, gender, birth, departments, address)
        data = {
            "errCode": "0",
            "errDesc": "操作成功"
        }
        return JsonResponse(data)


def student_delete(request):
    '''删除'''
    student_id = request.POST.get('student_id')
    db_student_id = mysql_query.select_student_information(student_id)
    if db_student_id == ():
        data = {
            "errCode": "20",
            "errDesc": "学生学号不存在",
        }
        return JsonResponse(data)
    else:
        mysql_delete.delete_student_information(student_id)
        data = {
            "errCode": "0",
            "errDesc": "操作成功"
        }
        return JsonResponse(data)
