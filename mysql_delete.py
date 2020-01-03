import pymysql

def delete(sql):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = '''{}'''.format(sql)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


# 根据学号删除学生表信息
def delete_student_information(student_id):
    sql = '''
          DELETE 
          FROM student_information 
          WHERE student_id = "{}"
          '''.format(student_id)
    delete(sql)
    print("删除学号:" + student_id + '学生信息成功')


# 根据课程名称删除科目信息
def delete_course_title(course_title):
    sql = '''
          DELETE 
          FROM course 
          WHERE course_title = "{}"
          '''.format(course_title)
    delete(sql)
    print("删除科目名称:" + course_title + '科目信息成功')


# 根据课程编号删除科目信息
def delete_course_id(course_id):
    sql = '''
          DELETE 
          FROM course
          WHERE course_id = "{}"
          '''.format(course_id)
    delete(sql)
    print("删除科目编号:" + course_id + '科目信息成功')


# 根据学号删除成绩表所有信息
def delete_student_all_grade(student_id):
    sql = '''
          DELETE 
          FROM grade_table 
          WHERE student_id = "{}"
          '''.format(student_id)
    delete(sql)
    return print("删除学号:" + student_id + '所有成绩信息成功')


# 根据学号和课程编号删除成绩表成绩
def delete_student_grade(student_id, course_id):
    sql = '''
          DELETE 
          FROM grade_table 
          WHERE student_id = "{}" AND course_id = "{}"
          '''.format(student_id, course_id)
    delete(sql)
    return print("删除学号:" + student_id + '成绩成功')