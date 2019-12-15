import pymysql

# 查询学生总人数
def Select_Student_total_people():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT COUNT(*) FROM student_information'
    cursor.execute(sql)
    db.commit()
    Server_content =cursor.fetchall()
    # 将元组转换成列表
    Server_content_list = list(Server_content[0])[0]
    cursor.close()
    db.close()
    return Server_content_list


# 根据学号查询学生信息
def Select_Student_information(Student_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT Student_Name, Student_id, Gender,birth,departments,address FROM `Student_information` WHERE Student_id = "{}"'.format(Student_id)
    cursor.execute(sql)
    db.commit()
    Server_content =cursor.fetchall()
    # 将元组转换成列表
    try:
        Server_content_list = list(Server_content[0])
        cursor.close()
        db.close()
    except:
        Server_content_list = list(Server_content)
        cursor.close()
        db.close()
    return Server_content_list


# 查询所有学生信息展示
def Select_Student_all():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT Student_Name, Student_id, Gender,birth,departments,address FROM `Student_information`'
    cursor.execute(sql)
    db.commit()
    Server_content =cursor.fetchall()
    # 将元组转换成列表
    Server_content_list = list(Server_content)
    cursor.close()
    db.close()
    return Server_content_list


# 根据名字查询一个或者多个学生信息
def Select_Student_Name(Student_name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT Student_Name, Student_id, Gender,birth,departments,address FROM `Student_information` WHERE Student_name = "{}"'.format(Student_name)
    cursor.execute(sql)
    db.commit()
    Server_content =cursor.fetchall()
    student = list(Server_content)
    return student

# 根据地区查询
def Select_Student_address(address):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT Student_Name, Student_id, Gender,birth,departments,address FROM `Student_information` WHERE address like "%{}%"'.format(
        address)
    cursor.execute(sql)
    db.commit()
    Server_content = cursor.fetchall()
    student = list(Server_content)
    return student

# 根据性别查询
def Select_Student_gender(gender):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT Student_Name, Student_id, Gender,birth,departments,address FROM `Student_information` WHERE gender = "{}"'.format(
        gender)
    cursor.execute(sql)
    db.commit()
    Server_content = cursor.fetchall()
    student = list(Server_content)
    return student

# 根据年龄查询
def Select_Student_age(age):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT Student_Name, Student_id, Gender,birth,departments,address FROM `Student_information` WHERE age = "2019-{}"'.format(
        age)
    cursor.execute(sql)
    db.commit()
    Server_content = cursor.fetchall()
    student = list(Server_content)
    return student

# 根据院系查询
def Select_Student_departments(departments):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'SELECT Student_Name, Student_id, Gender,birth,departments,address FROM `Student_information` WHERE departments = "{}"'.format(
        departments)
    cursor.execute(sql)
    db.commit()
    Server_content = cursor.fetchall()
    student = list(Server_content)
    return student


# 查询所有科目信息
def Select_All_Course_title():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT Course_title,Course_id FROM `subjectinfo`'
    cursor.execute(sql)
    db.commit()
    All_Course_title_content = cursor.fetchall()
    # 讲遍历出的内容拼接成列表
    All_Course_title_content_list = list(All_Course_title_content)
    cursor.close()
    db.close()
    return All_Course_title_content_list


# 根据科目名字查询科目信息
def Select_Course_title(Course_title):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT Course_title,Course_id FROM `subjectinfo` where Course_title = "{}"'.format(Course_title)
    cursor.execute(sql)
    db.commit()
    All_Course_title_content = cursor.fetchall()
    # 讲遍历出的内容拼接成列表
    All_Course_title_content_list = list(All_Course_title_content)
    cursor.close()
    db.close()
    return All_Course_title_content_list

# 根据课程名称查询课程编号
def Select_Course_title_id(Course_title):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT Course_id FROM `subjectinfo` where Course_title = "{}"'.format(Course_title)
    cursor.execute(sql)
    db.commit()
    All_Course_title_content = cursor.fetchall()
    # 讲遍历出的内容拼接成列表
    All_Course_title_content_list = list(All_Course_title_content)[0]
    c = All_Course_title_content_list[0]
    cursor.close()
    db.close()
    return c

# 根据科目编号查询科目信息
def Select_Course_id(Course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT Course_title,Course_id FROM `subjectinfo` where Course_id = "{}"'.format(Course_id)
    cursor.execute(sql)
    db.commit()
    All_Course_title_content = cursor.fetchall()
    # 讲遍历出的内容拼接成列表
    All_Course_title_content_list = list(All_Course_title_content)
    cursor.close()
    db.close()
    return All_Course_title_content_list


# 查询所有成绩
def Select_All_Grade():
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    # sql = 'SELECT Student_id,Course_title,Grade FROM `grade_table` WHERE  Student_id = "{}"'.format(Student_id)

    sql = 'select student_information.Student_Name,grade_table.Student_id,subjectinfo.Course_title,grade_table.Grade from student_information left join grade_table on student_information.Student_id=grade_table.Student_id left join  subjectinfo on grade_table.Course_id=subjectinfo.Course_id'
    cursor.execute(sql)
    db.commit()
    All_Course_title_content = cursor.fetchall()
    # 讲遍历出的内容拼接成列表
    All_Course_title_content_list = list(All_Course_title_content)
    return All_Course_title_content_list

# 根据学号查询学生成绩
def Select_Student_id_Grade(Student_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    # sql = 'SELECT Student_id,Course_title,Grade FROM `grade_table` WHERE  Student_id = "{}"'.format(Student_id)
    sql = 'select student_information.Student_Name,grade_table.Student_id,subjectinfo.Course_title,grade_table.Grade from student_information left join grade_table on student_information.Student_id=grade_table.Student_id left join  subjectinfo on grade_table.Course_id=subjectinfo.Course_id WHERE grade_table.Student_id = "{}"'.format(Student_id)
    cursor.execute(sql)
    db.commit()
    All_Course_title_content = cursor.fetchall()
    # 讲遍历出的内容拼接成列表
    All_Course_title_content_list = list(All_Course_title_content)
    return All_Course_title_content_list

# 根据学生姓名查询学生成绩
def Select_Student_name_Grade(Student_Name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    # 获取结果为字典
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    # sql = 'SELECT Student_id,Course_title,Grade FROM `grade_table` WHERE  Student_id = "{}"'.format(Student_id)
    sql = 'select student_information.Student_Name,grade_table.Student_id,subjectinfo.Course_title,grade_table.Grade from student_information left join grade_table on student_information.Student_id=grade_table.Student_id left join  subjectinfo on grade_table.Course_id=subjectinfo.Course_id WHERE student_information.Student_Name = "{}"'.format(Student_Name)
    cursor.execute(sql)
    db.commit()
    All_Course_title_content = cursor.fetchall()
    # 讲遍历出的内容拼接成列表
    All_Course_title_content_list = list(All_Course_title_content)
    return All_Course_title_content_list

if __name__ == '__main__':
    Select_Student_address('成都')
