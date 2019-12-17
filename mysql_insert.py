import pymysql
import mysql_query

# 插入学生信息到学生表
def insert_student_information(student_name, student_id, gender,birth,departments,address):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    id = mysql_query.select_student_information(student_id)
    if id == []:
        try:
            sql = 'INSERT INTO `student_information` (student_id, student_name,gender,birth,departments,address) VALUES ("{}","{}","{}","{}","{}","{}") '.format(student_id, student_name, gender, birth, departments, address)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            print("新增" + student_name + '学生信息成功')
        except:
            print('请按照规范输入')
    else:
        print('学号已存在')


# 插入课程信息到科目信息表
def insert_course(course_title,course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    id = mysql_query.select_course_id(course_id)
    if id == []:
        try:
            sql = 'INSERT INTO `course` (course_id,course_title) VALUES ("{}","{}")'.format(course_id, course_title)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            print("新增" + course_title + '科目信息成功')
        except:
            print('请按规范输入')
    else:
        print('编号已存在')

# 插入成绩信息到成绩表 输入课程编号
def insert_grade_id(student_id, course_id, grade):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'INSERT INTO `grade_table` (student_id, course_id, grade) VALUES ("{}","{}","{}") '.format(student_id, course_id, grade)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("新增"+student_id+'成绩信息成功')

# 插入成绩信息到成绩表 不输入课程编号输入课程名称
def insert_grade_table(student_id, course_id, grade):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    c = mysql_query.select_course_title_id(course_id)
    sql = 'INSERT INTO `grade_table` (Student_id, Course_id, Grade) VALUES ("{}","{}","{}") '.format(student_id, c, grade)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("新增"+student_id+'成绩信息成功')

# if __name__ == '__main__':
#     insert_course("数学","01")