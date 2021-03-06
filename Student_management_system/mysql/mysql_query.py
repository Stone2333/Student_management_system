import pymysql

# 封装
def select(sql):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    # cursor = db.cursor()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = '''{}'''.format(sql)
    cursor.execute(sql)
    db.commit()
    content = cursor.fetchall()
    cursor.close()
    db.close()
    return content

def login(name):
    sql = '''
          SELECT username,password 
          FROM user
          WHERE username = "{}"
          '''.format(name)
    user = select(sql)
    print(user)
    return user




# 查询学生总人数
def select_student_total_people():
    sql = '''
          SELECT COUNT(*) 
          FROM student_information
          '''
    number = select(sql)
    return number


# 查询单个院系人数
def select_student_departments_number(departments):
    sql = '''
          SELECT COUNT(*) 
          FROM student_information 
          WHERE departments = "{}"
          '''.format(departments)
    number = select(sql)
    return number


#  查询所有院系人数
def all_dedepartments_number():
    sql = '''
          SELECT departments, count(*) AS number
          FROM student_information
          GROUP BY departments
          '''
    all_dedepartments_number = select(sql)
    return all_dedepartments_number


# 查询单个地区人数
def select_student_address_number(address):
    sql = '''
          SELECT COUNT(*)   
          FROM student_information
          WHERE address LIKE "%{}%"
          '''.format(address)
    number = select(sql)
    return number


# 查询所有地区人数
def select_student_all_address_number():
    sql = '''
          SELECT address, count(*) AS number
          FROM student_information
          GROUP BY address
           '''
    all_address_number = select(sql)
    return all_address_number


# 查询单独年龄段人数
def select_student_age_number(age):
    sql = '''
          SELECT COUNT(*)
          FROM student_information
          WHERE birth = YEAR(NOW()-"{}")
          '''.format(age)
    number = select(sql)
    return number


# 查询所有年龄段人数
def all_age_number():
    sql = '''
          SELECT birth,COUNT(*)
          FROM student_information
          GROUP BY birth
          '''
    all_age_number = select(sql)
    return all_age_number


# 查询单个性别人数
def gender_number(gender):
    sql = '''
          SELECT gender,COUNT(*)
          FROM student_information
          WHERE gender = "{}"
          '''.format(gender)
    gender_number = select(sql)
    return gender_number


# 查询所有性别人数
def all_gender_number():
    sql = '''
          SELECT gender,COUNT(*)
          FROM student_information
          GROUP BY gender
          '''
    all_gender_number = select(sql)
    return all_gender_number


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
          WHERE birth = YEAR(NOW())- "{}"
          '''.format(age)
    print(sql)
    student_information = select(sql)
    return student_information


# 根据院系查询
def select_student_departments(departments):
    sql = '''
          SELECT student_name, student_id, gender, birth, departments, address 
          FROM student_information 
          WHERE departments = "{}"
          '''.format(departments)
    student_departments = select(sql)
    print(student_departments)
    return student_departments


# 查询科目数量
def select_course_all_number():
    sql = '''
          SELECT COUNT(*) 
          FROM course
          '''
    number = select(sql)
    return number


# 查询单个科目选择人数
def selec_coures_people_number(course_id):
    sql = '''
          SELECT COUNT(*) AS number
          FROM course
          LEFT JOIN grade_table ON course.course_id=grade_table.course_id
          WHERE course.course_id = "{}"
          '''.format(course_id)
    number = select(sql)
    return number


# 查询科目选择人数名单
def select_coures_stundentinfo(course_id):
    sql = '''
             SELECT course.course_id,course.course_title,student_information.student_id,student_information.student_name,student_information.gender,student_information.birth,student_information.departments
             FROM course
             LEFT JOIN grade_table ON course.course_id=grade_table.course_id
             LEFT JOIN student_information ON grade_table.student_id=student_information.student_id
             WHERE course.course_id = "{}"
             '''.format(course_id)
    studentinfo = select(sql)
    return  studentinfo


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



# 单个学生总成绩
def course_grade_sum(course_id):
    sql = '''
          SELECT student_information.student_id,student_name,SUM(grade)
          FROM student_information
          LEFT JOIN grade_table ON student_information.student_id=grade_table.student_id  
          WHERE student_information.student_id = "{}"
          '''.format(course_id)
    course_grade_sum= select(sql)
    return course_grade_sum



# 所有学生总成绩  计算总成绩平均值有用
def coures_grade_all_sum():
    sql = '''
          SELECT SUM(grade)
          FROM grade_table
          '''
    course_grade_all_sum = select(sql)
    return course_grade_all_sum



# 单科平均值
def course_grade_avg(course_id ):
    sql = '''
          SELECT AVG(grade) AS '平均成绩'
          FROM grade_table
          WHERE course_id = "{}"
          '''.format(course_id )
    course_grade_avg = select(sql)
    return course_grade_avg


# 单科最高
def course_grade_max(course_id):
    sql = '''
          SELECT MAX(grade) AS '最高成绩'
          FROM grade_table
          WHERE course_id = "{}"
          '''.format(course_id)
    course_grade_max = select(sql)
    return course_grade_max


# 单科最低
def course_grade_min(course_id):
    sql = '''
          SELECT MIN(grade) AS '最高成绩'
          FROM grade_table
          WHERE course_id = "{}"
          '''.format(course_id)
    course_grade_min = select(sql)
    return course_grade_min





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
    # course_id_student('02')
    # course_id_student_number('02')
    # select_student_all()
    select_student_gender('男')
