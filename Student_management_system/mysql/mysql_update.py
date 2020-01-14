import pymysql

def upadte(sql):
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


# 根据学号更改学号
def update_student_id(student_id, new_student_id):
    sql = '''
          UPDATE student_information 
          SET student_id = "{b}" 
          WHERE student_id = "{a}"
          '''.format(a=student_id, b=new_student_id)
    upadte(sql)
    return print('学号:' + student_id + '学号修改成功')


# 根据学号更改姓名
def update_student_name(student_id, new_student_name):
    sql = '''
          UPDATE student_information 
          SET student_name = "{b}" 
          WHERE student_id = "{a}"
          '''.format(a=student_id, b=new_student_name)
    upadte(sql)
    return print('学号:' + student_id + '姓名修改成功')


# 根据学号更改性别
def update_gender(student_id, new_gender):
    sql = '''
          UPDATE student_information 
          SET gender = "{b}" 
          WHERE student_id = "{a}"
          '''.format(a=student_id, b=new_gender)
    upadte(sql)
    return print('学号:' + student_id + '性别修改成功')


# 根据学号更改年月
def update_birth(student_id, new_birth):
    sql = '''
          UPDATE student_information
          SET birth = "{b}" 
          WHERE student_id = "{a}"
          '''.format(a=student_id, b=new_birth)
    upadte(sql)
    return print('学号:' + student_id + '年月日修改成功')


# 根据学号更改院系
def update_departments(student_id, new_departments):
    sql = '''
          UPDATE student_information 
          SET departments = "{b}" 
          WHERE student_id = "{a}"
          '''.format(a=student_id, b=new_departments)
    upadte(sql)
    return print('学号:' + student_id + '院系修改成功')


# 根据学号更改地址
def update_address(student_id, new_address):
    sql = '''
          UPDATE student_information 
          SET address = "{b}" 
          WHERE student_id = "{a}"
          '''.format(a=student_id, b=new_address)
    upadte(sql)
    return print('学号:' + student_id + '地址修改成功')


# 根据科目名称更改课程名称
def update_course_title(course_id, new_course_title):
    sql = '''
          UPDATE course
          SET course_title = "{b}" 
          WHERE course_id = "{a}"
          '''.format(a=course_id, b=new_course_title)
    upadte(sql)
    return print('科目编号:' + course_id + '科目名称修改成功')


# 根据课程编号更改课程编号
def update_course_id(course_id, new_course_id):
    sql = '''
          UPDATE course 
          SET  course_id = "{b}" 
          WHERE course_id = "{a}"
          '''.format(a=course_id, b=new_course_id)
    upadte(sql)
    return print('科目编号:' + course_id + '科目编号修改成功')


# 根据学号和课程编号在成绩表修改课程编号
def update_grade_course_id(student_id, course_title, new_course_title):
    sql = '''
          UPDATE grade_table 
          SET course_id = "{c}" 
          WHERE student_id = "{a}" AND course_id= "{b}"
          '''.format(a=student_id, b=course_title, c=new_course_title)
    upadte(sql)
    return print('科目编号' + student_id + '科目编号修改成功')


# 根据学号在成绩表修改所有学号
def update_grade_student_id(student_id, new_student_id):
    sql = '''
          UPDATE grade_table 
          SET  student_id = "{b}" 
          WHERE student_id = "{a}"
          '''.format(a=student_id, b=new_student_id)
    upadte(sql)
    return print('学号:' + student_id + '课程编号修改成功')


# 根据学号和课程编号修改成绩表成绩
def update_grade_grade(student_id, course_id, new_grade):
    sql = '''
          UPDATE grade_table 
          SET  grade = "{c}" 
          WHERE student_id = "{a}" AND course_id= "{b}"
          '''.format(a=student_id, b=course_id, c=new_grade)
    upadte(sql)
    return print('学号:' + student_id + '成绩修改成功')

