import pymysql
import mysql_query

def Delete_Student_information(Student_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    id = mysql_query.Query_Student_information(Student_id)
    if id == []:
        print('该学号不存在')
    else:
        sql = 'DELETE FROM `Student_information` WHERE Student_id = "{}"'.format(Student_id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("删除"+Student_id+'学生信息成功')

def Delete_Course_title(Course_title):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    id = mysql_query.Select_Course_title(Course_title)
    if id == []:
        print('该科目不存在')
    else:
        sql = 'DELETE FROM `subjectinfo` WHERE Course_title = "{}"'.format(Course_title)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("删除"+Course_title+'科目信息成功')

def Delete_Course_id(Course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    id = mysql_query.Select_Course_title(Course_id)
    if id == []:
        print('该科目编号不存在')
    else:
        sql = 'DELETE FROM `subjectinfo` WHERE Course_id = "{}"'.format(Course_id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("删除编号"+Course_id+'科目信息成功')

def Delete_Grade(Student_id,Course_title):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    id = mysql_query.Query_Student_information(Student_id)
    course = mysql_query.Select_Course_title(Course_title)
    if id == []:
        print('该学号不存在')
    elif course == []:
        print('该科目不存在')
    else:
        sql = 'DELETE FROM `grade_table` WHERE Student_id = "{}" and Course_title = "{}"'.format(Student_id,Course_title)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("删除"+Student_id+'成绩信息成功')