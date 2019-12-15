import pymysql
import mysql_query

# 插入学生信息到学生表
def Insert_Student_information(Student_Name, Student_id, Gender,birth,departments,address):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    try:
        sql = 'INSERT INTO `Student_information` (Student_Name, Student_id, Gender,birth,departments,address) VALUES ("{}","{}","{}","{}","{}","{}") '.format(Student_Name, Student_id, Gender, birth, departments, address)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("新增" + Student_Name + '学生信息成功')
    except:
        print('学号已存在')

# 插入课程信息到科目信息表
def Insert_Subjectinfo(Course_title,Course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    try:
        sql = 'INSERT INTO `Subjectinfo` (Course_title,Course_id) VALUES ("{}","{}") '.format(Course_title, Course_id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("新增" + Course_title + '科目信息成功')
    except:
        print('编号已存在')


# 插入成绩信息到成绩表 输入课程编号
def Insert_Grade_id(Student_id, Course_id, Grade):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'INSERT INTO `grade_table` (Student_id, Course_id, Grade) VALUES ("{}","{}","{}") '.format(Student_id, Course_id, Grade)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("新增"+Student_id+'成绩信息成功')

# 插入成绩信息到成绩表 不输入课程编号输入课程名称
def Insert_Grade_table(Student_id, Course_id, Grade):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    c = mysql_query.Select_Course_title_id(Course_id)
    sql = 'INSERT INTO `grade_table` (Student_id, Course_id, Grade) VALUES ("{}","{}","{}") '.format(Student_id, c, Grade)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("新增"+Student_id+'成绩信息成功')

# if __name__ == '__main__':
#     Insert_Grade_table()