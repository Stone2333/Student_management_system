import pymysql
import mysql_query
# 根据学号删除学生表信息
def delete_student_information(student_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'DELETE FROM `student_information` WHERE student_id = "{}"'.format(student_id)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("删除"+student_id+'学生信息成功')

# 根据课程名称删除科目信息
def delete_course_title(course_title):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    id = mysql_query.select_course_title(course_title)
    if id == []:
        print('该科目不存在')
    else:
        sql = 'DELETE FROM `course` WHERE course_title = "{}"'.format(course_title)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("删除"+course_title+'科目信息成功')


# 根据课程编号删除科目信息
def delete_course_id(course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    id = mysql_query.select_course_id(course_id)
    if id == []:
        print('该科目编号不存在')
    else:
        sql = 'DELETE FROM `course` WHERE course_id = "{}"'.format(course_id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("删除编号"+course_id+'科目信息成功')

# 根据学号和课程编号删除成绩表成绩
def delete_grade(student_id,course_title):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    id = mysql_query.select_student_information(student_id)
    course = mysql_query.select_course_title(course_title)
    if id == []:
        print('该学号不存在')
    elif course == []:
        print('该科目不存在')
    else:
        sql = 'DELETE FROM `grade_table` WHERE student_id = "{}" and course_title = "{}"'.format(student_id,course_title)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("删除"+student_id+'成绩信息成功')