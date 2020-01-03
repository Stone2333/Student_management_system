import pymysql

# 封装
def select(sql):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = '''{}'''.format(sql)
    cursor.execute(sql)
    db.commit()
    content = cursor.fetchall()
    cursor.close()
    db.close()
    return content


# 查询学生总人数
def select_student_total_people():
    sql = '''
          SELECT COUNT(*) 
          FROM student_information
          '''
    number = select(sql)
    return number

# 查询院系人数
def select_student_departments_number(departments):
    sql = '''
          SELECT COUNT(*) 
          FROM student_information 
          WHERE departments = "{}"
          '''.format(departments)
    number = select(sql)
    return number


# 查询地区人数
def select_student_address_number(address):
    sql = '''
          SELECT COUNT(*)   
          FROM student_information
          WHERE address LIKE "%{}%"
          '''.format(address)
    number = select(sql)
    return number

# 查询年龄段人数
def select_student_age_number(age):
    sql = '''
          SELECT COUNT(*)
          FROM student_information
          WHERE birth = "{}"
          '''.format(age)
    number = select(sql)
    return number


# 根据学号查询学生信息
def select_student_information(student_id):
    sql = '''
          SELECT student_name, student_id, gender, birth, departments, address 
          FROM student_information
          WHERE student_id = "{}"
          '''.format(student_id)
    student_information = select(sql)
    return student_information


# 查询所有学生信息展示
def select_student_all():
    sql = '''
          SELECT student_name, student_id, gender, birth, departments, address 
          FROM student_information
          '''
    student_all_information = select(sql)
    return student_all_information


# 根据名字查询一个或者多个学生信息
def select_student_name(student_name):
    sql = '''
          SELECT student_name, student_id, gender, birth, departments, address 
          FROM student_information
          WHERE student_name = "{}"
          '''.format(student_name)
    student_information = select(sql)
    return student_information


# 根据地区查询
def select_student_address(address):
    sql = '''
          SELECT student_name, student_id, gender, birth, departments, address 
          FROM student_information
          WHERE address LIKE "%{}%"
          '''.format(address)
    student_address = select(sql)
    return student_address


# 根据性别查询
def select_student_gender(gender):
    sql = '''
          SELECT student_name, student_id, gender, birth, departments, address 
          FROM student_information
          WHERE gender = "{}"
          '''.format(gender)
    student_gender = select(sql)
    return student_gender


# 根据年龄查询
def select_student_age(age):
    sql = '''
          SELECT student_name, student_id, gender, birth, departments, address 
          FROM student_information
          WHERE birth ="{}"
          '''.format(age)
    student_information = select(sql)
    return student_information


# 根据院系查询
def select_student_departments(departments):
    sql = '''
          SELECT student_Name, student_id, gender, birth, departments, address 
          FROM student_information 
          WHERE departments = "{}"
          '''.format(departments)
    student_departments = select(sql)
    return student_departments


# 查询科目数量
def select_course_number():
    sql = '''
          SELECT COUNT(*) 
          FROM course
          '''
    number = select(sql)
    return number


# 查询所有科目信息
def select_all_course_title():
    sql = '''
          SELECT course_title, course_id 
          FROM course
          '''
    all_course = select(sql)
    return all_course


# 根据科目名字查询科目信息
def select_course_title(course_title):
    sql = '''
          SELECT course_title, course_id 
          FROM course 
          WHERE course_title = "{}"
          '''.format(course_title)
    course = select(sql)
    return course


# 根据课程名称查询课程编号
def select_course_title_id(course_title):
    sql = '''
          SELECT course_id 
          FROM course
          WHERE course_title = "{}"
          '''.format(course_title)
    course_title_id = select(sql)
    return course_title_id


# 根据科目编号查询科目信息
def select_course_id(course_id):
    sql = '''
          SELECT course_title, course_id 
          FROM course 
          WHERE course_id = "{}"
          '''.format(course_id)
    course_id = select(sql)
    return course_id


# 查询所有成绩
def select_all_grade():
    sql = '''
          SELECT student_information.student_name, student_information.student_id, course.course_title, grade_table.grade 
          FROM student_information 
          LEFT JOIN grade_table ON student_information.student_id = grade_table.student_id 
          LEFT JOIN course ON grade_table.course_id = course.course_id
          '''
    all_grade = select(sql)
    return all_grade


# 根据学号查询学生成绩
def select_student_id_grade(student_id):
    sql = '''
          SELECT student_information.student_name, student_information.student_id, course.course_title, grade_table.grade
          FROM student_information 
          LEFT JOIN grade_table ON student_information.student_id = grade_table.student_id 
          LEFT JOIN course ON grade_table.course_id = course.course_id 
          WHERE student_information.student_id = "{}"
          '''.format(student_id)
    student_id_grade = select(sql)
    return student_id_grade


# 根据学生姓名查询学生成绩
def select_student_name_grade(student_name):
    sql = '''
          SELECT student_information.student_name, student_information.student_id, course.course_title, grade_table.grade 
          FROM student_information 
          LEFT JOIN grade_table ON student_information.student_id = grade_table.student_id 
          LEFT JOIN course ON grade_table.course_id=course.course_id 
          WHERE student_information.student_Name = "{}"
          '''.format(student_name)
    student_name_grade = select(sql)
    return student_name_grade


# 根据学号和课程编号查询单一科目成绩唯一性
def select_grade_uniqu(student_id, course_id):
    sql = '''
          SELECT * 
          FROM grade_table 
          WHERE student_id = "{}" AND course_id = "{}"
          '''.format(student_id, course_id)
    grade_uniqu = select(sql)
    return grade_uniqu


# 利用学号连表查询获取两张表都存在的学号的信息
def select_synchronous(student_id):
    sql = '''
          SELECT * 
          FROM student_information 
          JOIN grade_table ON student_information.student_id = grade_table.student_id 
          WHERE student_information.student_id = "{}"
          '''.format(student_id)
    synchronous = select(sql)
    return synchronous

# 根据科目编号查询选择科目学生名单
def course_id_student(course_id):
    sql = '''
          SELECT student_information.student_name,grade_table.student_id
          FROM student_information
          JOIN grade_table ON student_information.student_id = grade_table.student_id
          WHERE course_id = "{}"
          '''.format(course_id)
    student_information = select(sql)
    return student_information


# 根据科目编号查询选择科目学生人数
def course_id_student_number(course_id):
    sql = '''
          SELECT COUNT(*)
          FROM student_information
          JOIN grade_table ON student_information.student_id = grade_table.student_id
          WHERE course_id = "{}"
          '''.format(course_id)
    student_number = select(sql)
    return student_number


# 参加考试学生名单
def take_an_exam_student():
    sql = '''
          SELECT DISTINCT student_information.student_name,grade_table.student_id
          FROM student_information
          JOIN grade_table ON student_information.student_id = grade_table.student_id
          '''
    take_an_exam_student = select(sql)
    return take_an_exam_student


# 参加考试学生数量
def ake_an_exam_student_number():
    sql = '''
          SELECT COUNT(DISTINCT student_information.student_id)
          FROM student_information
          JOIN grade_table ON student_information.student_id = grade_table.student_id
          '''
    student_number = select(sql)
    return student_number


# 没有参加考试的学生名单
def no_take_the_exam_student():
    sql = '''
          SELECT DISTINCT student_information.student_name,student_information.student_id
          FROM student_information
          LEFT JOIN grade_table ON student_information.student_id = grade_table.student_id
          WHERE grade_table.student_id IS NULL     
          '''
    no_take_the_exam_student = select(sql)
    return no_take_the_exam_student


# 没有参加学生考试的学生数量
def no_take_the_exam_student_number():
    sql = '''
          SELECT COUNT(DISTINCT student_information.student_id)
          FROM student_information
          LEFT JOIN grade_table ON student_information.student_id = grade_table.student_id
          WHERE grade_table.student_id IS NULL
          '''
    student_number = select(sql)
    return student_number

if __name__ == '__main__':
    course_id_student('02')
    course_id_student_number('02')

