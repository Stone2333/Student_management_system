import pymysql

def insert(sql):
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


# 插入学生信息到学生表
def insert_student_information(student_name, student_id, gender, birth, departments, address):
    sql = '''
          INSERT INTO student_information (student_id, student_name, gender, birth, departments, address) 
          VALUES ("{}", "{}", "{}", "{}", "{}", "{}")
          '''.format(student_id, student_name, gender, birth, departments, address)
    insert(sql)
    # return print("新增姓名:" + student_name + '学生信息成功')


# 插入课程信息到科目信息表
def insert_course(course_title, course_id):
    sql = '''
          INSERT INTO course (course_id, course_title) 
          VALUES ("{}", "{}")
          '''.format(course_id, course_title)
    insert(sql)
    return print("新增科目名称:" + course_title + '科目信息成功')


# 插入成绩信息到成绩表 输入课程编号
def insert_grade_id(student_id, course_id, grade):
    sql = '''
          INSERT INTO grade_table (student_id, course_id, grade)
          VALUES ("{}", "{}", "{}")
          '''.format(student_id, course_id, grade)
    insert(sql)
    return print("新增学号:" + student_id + '成绩信息成功')


# if __name__ == '__main__':
#     insert_course("数学","01")