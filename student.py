import mysql_insert
import mysql_query
import mysql_update
import mysql_delete



def function():
    type = input("请输入需要使用的功能序号：\n1.学生信息的增删改查\n2.科目信息的增删改查\n3.学生对应科目成绩增删改查\n0.退出\n")
    while True:
        if type == '1':
            print('您选择了学生信息的增删改查')
            subfunction = input('请输入需要进行操作的序号：\n1.学生信息的新增\n2.学生信息的查询\n3.学生信息的更改\n4.学生信息的删除\n0.退回主菜单\n')
            student.student_frame(subfunction)

        elif type == '2':
            print('您选择了科目信息的增删改查')
            subfunction = input('请输入需要进行操作的序号：\n1.科目信息的新增\n2.所有科目信息的查询\n3.根据课程名称查询科目信息\n4.根据课程编号查询科目信息\n5.科目信息的更改\n4.科目信息的删除\n0.退回主菜单\n')
            subjects.subjects_frame(subfunction)

        elif type == '3':
            print('您选择了成绩的增删改查')
            subfunction = input('请输入需要进行操作的序号：\n1.成绩的新增\n2.成绩的查询\n3.成绩的更改\n4.成绩的删除\n0.退回主菜单退回主菜单\n')
            grade.grade_frame(subfunction)

        elif type == '0':
            quit = input('您确认要退出吗(是/否)\n')
            if quit == '是':
                print('欢迎使用本系统，谢谢')
                exit()
        else:
            print('请输入正确的功能序号')


class student():

    def student_insert(self):
        Student_information = self.strip(',').split(',')
        try:
            mysql_insert.Insert_Student_information(Student_information[0], Student_information[1],Student_information[2])
        except:
            print('请按照规范输入学生信息')

    def student_query(self):
        if self == '0':
            student.student_frame(self)
        Student_information = mysql_query.Select_Student_information(self)
        if Student_information != []:
            Student_information_str = '姓名:' + Student_information[0] + ' 学号:' + Student_information[1] + ' 性别:' + Student_information[2]
            print(Student_information_str)
        elif Student_information == []:
            print('学号不存在')

    def student_update(self):
        if self == '0':
            student.student_frame(self)
        subfunction = self.strip(',').split(',')
        if subfunction[2] == '1':
            mysql_update.Update_Student_name(subfunction[0], subfunction[1])
        elif subfunction[2] == '2':
            mysql_update.Update_Student_id(subfunction[0], subfunction[1])
        elif subfunction[2] == '3':
            mysql_update.Update_Gender(subfunction[0], subfunction[1])
        else:
            print('请按照规范输入修改学生信息')

    def student_delect(self):
        if self == '0':
            student.student_frame(self)
        try:
            mysql_delete.Delete_Student_information(self)
        except:
            print('输入的学号不正确')

    def student_frame(self):
        while True:
            if self == '1':
                Student_information = input('请依次输入学生姓名，学号，性别，并用逗号分隔(输入"0"返回上一级)\n')
                student.student_insert(Student_information)
            elif self == '2':
                Student_information = input('请输入需要查询学生信息的学号(输入"0"返回上一级)\n')
                student.student_query(Student_information)
            elif self == '3':
                Student_information = input('请输入修改信息的学号和新值并选择修改类型用逗号分割1.姓名2.学号3.性别(输入"0"返回上一级)\n')
                student.student_update(Student_information)
            elif self == '4':
                Student_information = input('请输入删除学生信息的学号(输入"0"返回上一级)\n')
                student.student_delect(Student_information)
            elif self == '0':
                print('退回主菜单')
                function()
            else:
                print('请输入正确的功能序号')

class subjects:
    def subjects_insert(self):
        if self == '0':
            subjects.subjects_frame()
        Course_title = self.strip(',').split(',')
        mysql_insert.Insert_Subjectinfo(Course_title[0], Course_title[1])

    def subjects_all_query(self):
        if self == '0':
            subjects.subjects_frame()
        print('科目如下：')
        mysql_query.Select_All_Course_title()
        print('\n')

    def subjects_course_title_query(self):
        if self == '0':
            subjects.subjects_frame()
        mysql_query.Select_Course_title(self)

    def subjects_course_id_query(self):
        if self == '0':
            subjects.subjects_frame()
        mysql_query.Select_Course_id(self)

    def subjects_update(self):
        if self == '0':
            subjects.subjects_frame()
        Course_title = self.strip(',').split(',')
        try:
            mysql_update.Update_Course_title(Course_title[0], Course_title[1])
        except:
            print('请按照规范填写')

    def subjects_course_title_delect(self):
        if self == '0':
            subjects.subjects_frame()
        mysql_delete.Delete_Course_title(self)

    def subjects_course_id_delect(self):
        if self == '0':
            subjects.subjects_frame()
        mysql_delete.Delete_Course_id(self)

    def subjects_frame(self):
            if self == '1':
                Course_title = input('请输入您要添加的科目信息名称和课程编号用逗号分隔(输入"0"返回上一级)\n')
                subjects.subjects_insert(Course_title)

            elif self == '2':
                print('全部科目如下：')
                mysql_query.Select_All_Course_title()
                print('\n')

            elif self == '3':
                Course_title = input('请输入需要查询科目的名称(输入"0"返回上一级)\n')
                mysql_query.Select_Course_title(Course_title)

            elif self == '4':
                Course_id = input('请输入需要查询科目的编号(输入"0"返回上一级)\n')
                mysql_query.Select_Course_id(Course_id)

            elif self == '5':
                Course_title = input('请输入需要修改科目的名称和新值用逗号分隔(输入"0"返回上一级)\n')
                subjects.subjects_update(Course_title)

            elif self == '6':
                Course_title = input('请输入需要删除的科目名称(输入"0"返回上一级)\n')
                subjects.subjects_course_title_delect(Course_title)

            elif self == '7':
                Course_id = input('请输入需要删除的科目名称(输入"0"返回上一级)\n')
                subjects.subjects_course_id_delect(Course_id)

            elif self == '0':
                print('退回主菜单')
                function()
            else:
                print('请输入正确的功能序号')

class grade:
    def grade_insert(self):
        if self == '0':
            grade.grade_frame()
        Grade = self.strip(',').split(',')
        try:
            mysql_insert.Insert_Grade_table(Grade[0], Grade[1], Grade[2])
        except:
            print('请按照规范输入')


    def grade_all_query(self):
        if self == '0':
            grade.grade_frame()
        Grade = mysql_query.Select_All_Grade()
        for a in Grade:
            print('姓名:' + a[0] + ' 学号:' + a[1] + ' 科目:' + a[2] + ' 成绩:' + a[3])

    def grade_student_id_query(self):
        if self == '0':
            grade.grade_frame()
        Grade = mysql_query.Select_Student_id_Grade(self)
        for a in Grade:
            print('姓名:' + a[0] + ' 学号:' + a[1] + ' 科目:' + a[2] + ' 成绩:' + a[3])

    def grade_student_name_query(self):
        if self == '0':
            grade.grade_frame()
        Grade = mysql_query.Select_Student_name_Grade(self)
        for a in Grade:
            print('姓名:' + a[0] + ' 学号:' + a[1] + ' 科目:' + a[2] + ' 成绩:' + a[3])

    def grade_student_id_update(self):
        if self == '0':
            grade.grade_frame()
        Grade = self.strip(',').split(',')
        try:
            if Grade[3] == '1':
                mysql_update.Update_Grade_student_id(Grade[0], Grade[1])
            elif Grade[3] == '2':
                mysql_update.Update_Grade_course_id(Grade[0], Grade[1])
            elif Grade[3] == '3':
                mysql_update.Update_Grade_grade(Grade[0], Grade[1])
            else:
                print("请选择正确的类型")
        except:
            print('请按照规范输入')

    def grade_student_id_delete(self):
        if self == '0':
            grade.grade_frame()
        Grade = self.strip(',').split(',')
        try:
            mysql_delete.Delete_Grade(Grade[0], Grade[1])
        except:
            print('请按照规范输入')


    def grade_frame(self):
            if self == '1':
                Grade = input('请输入需要新增成绩信息的学号科目编号和成绩用逗号分隔(输入"0"返回上一级)\n')
                grade.grade_insert(Grade)

            elif self == '2':
                Grade = input('请输入需要查询成绩的学号(输入"0"返回上一级)')
                grade.grade_student_id_query(Grade)

            elif self == '3':
                Grade = input('请输入修改信息的学号和新值并选择修改类型用逗号分割1.学号2.科目编号3.成绩(输入"0"返回上一级)\n')
                grade.grade_student_id_update(Grade)

            elif self == '4':
                Grade = input('请输入需要删除成绩的学号和科目用逗号分隔(输入"0"返回上一级)\n')
                grade.grade_student_id_delete(Grade)


            elif self == '0':
                print('退回主菜单')
                function()

            else:
                print('请输入正确的功能序号')
#
if __name__ == '__main__':
    function()