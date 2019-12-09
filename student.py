import mysql_insert
import mysql_query
import mysql_update
import mysql_delete


# 主程序 一级菜单
def function():
    type = input("请输入需要使用的功能序号：\n1.学生信息的增删改查\n2.科目信息的增删改查\n3.学生对应科目成绩增删改查\n0.退出\n")
    while True:
        if type == '1':
           subfunction.student(type)
        elif type == '2':
            subfunction.subjectinfo(type)
        elif type == '3':
            subfunction.grade(type)
        elif type == '0':
            quit = input('您确认要退出吗(是/否)\n')
            if quit == '是':
                print('欢迎使用本系统，谢谢')
                exit()
            else:
                function()
        else:
            print('请输入正确的功能序号')
            function()


# 二级菜单
class subfunction:
    def student(self):
        print('您选择了学生信息的增删改查')
        subfunction = input('请输入需要进行操作的序号：\n1.学生信息的新增\n2.所有学生信息\n3.根据学号查询学生信息\n4.根据名字查询学生信息\n5.学生信息的更改\n6.学生信息的删除\n0.退回主菜单\n')
        student.student_frame(subfunction)

    def subjectinfo(self):
        print('您选择了科目信息的增删改查')  # 科目信息修改还差 根据编号改名称 和根据名称改编号
        subfunction = input('请输入需要进行操作的序号：\n1.科目信息的新增\n2.所有科目信息的查询\n3.根据课程名称查询科目信息\n4.根据课程编号查询科目信息\n5.科目信息的更改\n6.根据科目名称删除科目信息\n7.根据科目编号删除科目信息\n0.退回主菜单\n')
        subjects.subjects_frame(subfunction)

    def grade(self):
        print('您选择了成绩的增删改查')
        subfunction = input('请输入需要进行操作的序号：\n1.成绩的新增\n2.查询所有学生成绩\n3.根据学号查询成绩\n4.根据学生姓名查询成绩\n5.成绩的更改\n6.成绩的删除\n0.退回主菜单退回主菜单\n')
        grade.grade_frame(subfunction)

# 学生类
class student():
    # 学生信息插入
    def student_insert(self):
        if self == '0':
            subfunction.student(self)
        else:
            Student_information = self.strip(',').split(',')
            try:
                mysql_insert.Insert_Student_information(Student_information[0], Student_information[1], Student_information[2])
            except:
                print('请按照规范输入学生信息')

    # 所有学生信息
    def student_all(self):
        if self == '0':
            subfunction.student(self)
        Student_information = mysql_query.Select_Student_all()
        for a in Student_information:
            print('姓名:' + a[0] + ' 学号:' + a[1] + ' 性别:' + a[2])

    # 总人数
    def student_total_people(self):
        total_people = str(mysql_query.Select_Student_total_people())
        print('总人数:'+ total_people)


    # 根据学生学号查询学生信息显示 姓名，学号，性别
    def student_query(self):
        if self == '0':
            subfunction.student(self)
        Student_information = mysql_query.Select_Student_information(self)
        if Student_information != []:
            Student_information_str = '姓名:' + Student_information[0] + ' 学号:' + Student_information[1] + ' 性别:' + Student_information[2]
            print(Student_information_str)
        elif Student_information == []:
            print('学号不存在')

    # 根据学生名字查询一个或者多个学生信息 显示 姓名，学号，性别
    def student_name_query(self):
        if self == '0':
            subfunction.student(self)
        Student_information = mysql_query.Select_Student_Name(self)
        if Student_information != []:
            for a in Student_information:
                print('姓名:' + a[0] + ' 学号:' + a[1] + ' 性别:' + a[2])
        elif Student_information == []:
            print('姓名不存在')

    # 根据学生学号 修改 姓名，学号，性别
    def student_update(self):
        if self == '0':
            subfunction.student(self)
        else:
            try:
                subfunction1 = self.strip(',').split(',')
                if subfunction1[2] == '1':
                    mysql_update.Update_Student_name(subfunction1[0], subfunction1[1])
                elif subfunction1[2] == '2':
                    mysql_update.Update_Student_id(subfunction1[0], subfunction1[1])
                elif subfunction1[2] == '3':
                    mysql_update.Update_Gender(subfunction1[0], subfunction1[1])
            except:
              print('请按照规范输入修改学生信息')

    # 根据学生学号删除学生信息
    def student_delect(self):
        if self == '0':
            subfunction.student(self)
        id = mysql_query.Select_Student_information(self)
        if id == []:
            print('该学号不存在')
        else:
            mysql_delete.Delete_Student_information(self)

    # 三级模块
    def student_frame(self):
        while True:
            if self == '1':
                Student_information = input('请依次输入学生姓名，学号，性别，并用逗号分隔(输入"0"返回上一级)\n')
                student.student_insert(Student_information)

            elif self == '2':
                print('所有学生信息如下')
                student.student_all(self)
                subfunction.student(self)

            elif self == '3':
                Student_information = input('请输入需要查询学生信息的学号(输入"0"返回上一级)\n')
                student.student_query(Student_information)

            elif self == '4':
                Student_information = input('请输入需要查询学生信息的姓名(输入"0"返回上一级)\n')
                student.student_name_query(Student_information)

            elif self == '5':
                Student_information = input('请输入修改信息的学号和新值并选择修改类型用逗号分割1.姓名2.学号3.性别(输入"0"返回上一级)\n')
                student.student_update(Student_information)

            elif self == '6':
                Student_information = input('请输入删除学生信息的学号(输入"0"返回上一级)\n')
                student.student_delect(Student_information)

            elif self == '7':
                print('学生人数如下')
                student.student_total_people(self)
                subfunction.student(self)

            elif self == '0':
                print('退回上一级')
                function()

            else:
                print('请输入正确的功能序号')
                subfunction.student(self)

# 科目信息类
class subjects:
    # 插入科目信息 输入科目名称和科目编号
    def subjects_insert(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            Course_title = self.strip(',').split(',')
            try:
                mysql_insert.Insert_Subjectinfo(Course_title[0], Course_title[1])
            except:
                print('请按照规范输入')

    # 查询所有科目的科目名称和科目编号并展示
    def subjects_all_query(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            All_Course_title_content_list = mysql_query.Select_All_Course_title()
            for a in All_Course_title_content_list:
                print('科目:' + a[0] + ' 编号:' + a[1])

            # print('\n')

    # 根据科目名称查询科目名称和科目编号
    def subjects_course_title_query(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            course_title = mysql_query.Select_Course_title(self)
            if course_title == []:
                print('该科目名称不存在')
            else:
                All_Course_title_content_list = mysql_query.Select_Course_title(self)
                for a in All_Course_title_content_list:
                    print('科目:' + a[0] + ' 编号:' + a[1])

    # 根据科目编号查询科目名称和科目编号
    def subjects_course_id_query(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            Course_id = mysql_query.Select_Course_id(self)
            if Course_id == []:
                print('该科目编号不存在')
            else:
                All_Course_title_content_list = mysql_query.Select_Course_id(self)
                for a in All_Course_title_content_list:
                    print('科目:' + a[0] + ' 编号:' + a[1])

    # 通过科目名称更改科目名称
    def subjects_update(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            Course_title = self.strip(',').split(',')
            try:
                mysql_update.Update_Course_title(Course_title[0], Course_title[1])
            except:
                print('请按照规范填写')
    # 通过科目编号更改科目编号
    def subjects_course_id_update(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            Course_title = self.strip(',').split(',')
            try:
                mysql_update.Update_Course_title(Course_title[0], Course_title[1])
            except:
                print('请按照规范填写')

    # 通过科目名称删除科目信息
    def subjects_course_title_delect(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            mysql_delete.Delete_Course_title(self)

    # 通过科目编号删除科目信息
    def subjects_course_id_delect(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            try:
                mysql_delete.Delete_Course_id(self)
            except:
                print('请输入正确序号')

    # 三级模块
    def subjects_frame(self):
        while True:
            if self == '1':
                Course_title = input('请输入您要添加的科目信息名称和课程编号用逗号分隔(输入"0"返回上一级)\n')
                subjects.subjects_insert(Course_title)

            elif self == '2':
                print('全部科目如下：')
                subjects.subjects_all_query(self)
                subfunction.subjectinfo(self)

            elif self == '3':
                Course_title = input('请输入需要查询科目的名称(输入"0"返回上一级)\n')
                subjects.subjects_course_title_query(Course_title)

            elif self == '4':
                Course_id = input('请输入需要查询科目的编号(输入"0"返回上一级)\n')
                subjects.subjects_course_id_query(Course_id)

            elif self == '5':
                Course_title = input('请输入需要修改科目的名称和新值用逗号分隔(输入"0"返回上一级)\n')
                subjects.subjects_update(Course_title)

            elif self == '6':
                Course_title = input('请输入需要删除的科目名称(输入"0"返回上一级)\n')
                subjects.subjects_course_title_delect(Course_title)

            elif self == '7':
                Course_id = input('请输入需要删除的科目编号(输入"0"返回上一级)\n')
                subjects.subjects_course_id_delect(Course_id)

            elif self == '0':
                print('退回主菜单')
                function()

            else:
                print('请输入正确的功能序号')
                subfunction.subjectinfo(self)

# 成绩类
class grade:
    # 插入成绩 学号,课程编号,成绩
    def grade_insert(self):
        if self == '0':
            subfunction.grade(self)
        else:
            Grade = self.strip(',').split(',')
            try:
                mysql_insert.Insert_Grade_table(Grade[0], Grade[1], Grade[2])
            except:
                print('请按照规范输入')

    # 查询所有成绩并展示
    def grade_all_query(self):
        if self == '0':
            subfunction.grade(self)
        else:
            Grade = mysql_query.Select_All_Grade()
            for a in Grade:
                print('姓名:' + a[0] + ' 学号:' + a[1] + ' 科目:' + a[2] + ' 成绩:' + a[3])

    # 根据学号查询成绩
    def grade_student_id_query(self):
        if self == '0':
            subfunction.grade(self)
        else:
            Grade = mysql_query.Select_Student_id_Grade(self)
            for a in Grade:
                print('姓名:' + a[0] + ' 学号:' + a[1] + ' 科目:' + a[2] + ' 成绩:' + a[3])

    # 根据学生名字查询成绩并展示
    def grade_student_name_query(self):
        if self == '0':
            subfunction.grade(self)
        else:
            Grade = mysql_query.Select_Student_name_Grade(self)
            for a in Grade:
                print('姓名:' + a[0] + ' 学号:' + a[1] + ' 科目:' + a[2] + ' 成绩:' + a[3])

    # 根据学号修改 学号,科目，成绩
    def grade_student_id_update(self):
        if self == '0':
            subfunction.grade(self)
        else:
            Grade = self.strip(',').split(',')
            try:
                if Grade[2] == '1':
                    mysql_update.Update_Grade_student_id(Grade[0], Grade[1])
                elif Grade[2] == '2':
                    mysql_update.Update_Grade_course_id(Grade[0], Grade[1])
                elif Grade[2] == '3':
                    mysql_update.Update_Grade_grade(Grade[0], Grade[1])
                else:
                    print("请选择正确的类型")
            except:
                print('请按照规范输入')

    # 根据学号删除学生成绩
    def grade_student_id_delete(self):
        if self == '0':
            subfunction.grade(self)
        else:
            Grade = self.strip(',').split(',')
            try:
                mysql_delete.Delete_Grade(Grade[0], Grade[1])
            except:
                print('请按照规范输入')

    # 三级模块
    def grade_frame(self):
        while True:
            if self == '1':
                Grade = input('请输入需要新增成绩信息的学号科目编号和成绩用逗号分隔(输入"0"返回上一级)\n')
                grade.grade_insert(Grade)

            elif self == '2':
                print('所有学生成绩如下:')
                grade.grade_all_query(self)
                subfunction.grade(self)

            elif self == '3':
                Grade = input('请输入需要查询成绩的学号(输入"0"返回上一级)')
                grade.grade_student_id_query(Grade)

            elif self == '4':
                Grade = input('请输入需要查询成绩的姓名(输入"0"返回上一级)')
                grade.grade_student_name_query(Grade)

            elif self == '5':
                Grade = input('请输入修改信息的学号和新值并选择修改类型用逗号分割1.学号2.科目编号3.成绩(输入"0"返回上一级)\n')
                grade.grade_student_id_update(Grade)

            elif self == '6':
                Grade = input('请输入需要删除成绩的学号和科目用逗号分隔(输入"0"返回上一级)\n')
                grade.grade_student_id_delete(Grade)

            elif self == '0':
                print('退回主菜单')
                function()

            else:
                print('请输入正确的功能序号')
                subfunction.grade(self)
#
if __name__ == '__main__':
    function()