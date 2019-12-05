import pymysql
import mysql_query

def Insert_Student_information(Student_Name, Student_id, Gender):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    try:
        sql = 'INSERT INTO `Student_information` (Student_Name, Student_id, Gender) VALUES ("{}","{}","{}") '.format(Student_Name, Student_id, Gender)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        print("新增" + Student_Name + '学生信息成功')
    except:
        print('学号已存在')


def Insert_Subjectinfo(Course_title,Course_id):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="student_practice")
    cursor = db.cursor()
    sql = 'INSERT INTO `Subjectinfo` (Course_title,Course_id) VALUES ("{}","{}") '.format(Course_title, Course_id)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print("新增"+Course_title+'科目信息成功')


def Insert_Grade_table(Student_id, Course_id, Grade):
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