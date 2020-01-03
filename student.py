import mysql_insert
import mysql_query
import mysql_update
import mysql_delete
import datetime


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
        subfunction = input('请输入需要进行操作的序号：\n1.学生信息的新增\n2.所有学生信息\n3.根据学号查询学生信息\n4.根据名字查询学生信息\n5.根据地区查询学生信息\n6.根据性别查询学生信息\n7.根据年龄查询学生信息\n8.根据院系查询学生信息\n9.学生信息的更改\n10.学生信息的删除\n11.学生总人数\n0.退回主菜单\n')
        frame.student_frame(subfunction)

    def subjectinfo(self):
        print('您选择了科目信息的增删改查')  # 科目信息修改还差 根据编号改名称 和根据名称改编号
        subfunction = input('请输入需要进行操作的序号：\n1.科目信息的新增\n2.所有科目信息的查询\n3.根据课程名称查询科目信息\n4.根据课程编号查询科目信息\n5.科目信息的更改\n6.根据科目名称删除科目信息\n7.根据科目编号删除科目信息\n0.退回主菜单\n')
        frame.course_frame(subfunction)

    def grade(self):
        print('您选择了成绩的增删改查')
        subfunction = input('请输入需要进行操作的序号：\n1.成绩的新增\n2.查询所有学生成绩\n3.根据学号查询成绩\n4.根据学生姓名查询成绩\n5.成绩信息修改\n6.单一科目成绩的删除\n7.学号对应所有成绩删除\n0.退回主菜单\n')
        frame.grade_frame(subfunction)



# 三级菜单
class frame:
    def student_frame(self):
        while True:
            if self == '1':
                student_information = input('请依次输入学生姓名，学号，性别，出生年,院系，地址并用逗号分隔(输入"0"返回上一级)\n')
                Student.student_insert(student_information)
            elif self == '2':
                print('所有学生信息如下')
                Student.student_all(self)
                subfunction.student(self)
            elif self == '3':
                student_information = input('请输入需要查询学生信息的学号(输入"0"返回上一级)\n')
                Student.student_query(student_information)
            elif self == '4':
                student_information = input('请输入需要查询学生信息的姓名(输入"0"返回上一级)\n')
                Student.student_name_query(student_information)
            elif self == '5':
                student_information = input('请输入需要查询学生信息的地区(输入"0"返回上一级)\n')
                Student.student_address(student_information)
            elif self == '6':
                student_information = input('请输入需要查询学生信息的性别(输入"0"返回上一级)\n')
                Student.student_gender(student_information)
            elif self == '7':
                student_information = input('请输入需要查询学生信息的年龄(输入"0"返回上一级)\n')
                Student.student_age(student_information)
            elif self == '8':
                student_information = input('请输入需要查询学生信息的院系(输入"0"返回上一级)\n')
                Student.student_departments(student_information)
            elif self == '9':
                student_information = input('请输入修改信息的学号和新值并选择修改类型姓名、学号、性别、出生年、院系、地址用逗号分割(输入"0"返回上一级)\n')
                Student.student_update(student_information)
            elif self == '10':
                student_information = input('请输入删除学生信息的学号(输入"0"返回上一级)\n')
                Student.student_delect(student_information)
            elif self == '11':
                print('学生人数如下')
                Student.student_total_people(self)
                subfunction.student(self)
            elif self == '0':
                print('退回上一级')
                function()
            else:
                print('请输入正确的功能序号')
                subfunction.student(self)


    def course_frame(self):
        while True:
            if self == '1':
                Course_title = input('请输入您要添加的科目信息名称和课程编号用逗号分隔(输入"0"返回上一级)\n')
                Course.course_insert(Course_title)
            elif self == '2':
                print('全部科目如下：')
                Course.course_all_query(self)
                subfunction.subjectinfo(self)
            elif self == '3':
                Course_title = input('请输入需要查询科目的名称(输入"0"返回上一级)\n')
                Course.course_course_title_query(Course_title)
            elif self == '4':
                Course_id = input('请输入需要查询科目的编号(输入"0"返回上一级)\n')
                Course.course_course_id_query(Course_id)
            elif self == '5':
                Course_title = input('请输入需要修改科目的编号和新值名称用逗号分隔(输入"0"返回上一级)\n')
                Course.course_update(Course_title)
            elif self == '6':
                Course_title = input('请输入需要删除的科目名称(输入"0"返回上一级)\n')
                Course.course_course_title_delect(Course_title)
            elif self == '7':
                Course_id = input('请输入需要删除的科目编号(输入"0"返回上一级)\n')
                Course.course_course_id_delect(Course_id)
            elif self == '0':
                print('退回主菜单')
                function()
            else:
                print('请输入正确的功能序号')
                subfunction.subjectinfo(self)


    def grade_frame(self):
        while True:
            if self == '1':
                grade = input('请输入需要新增成绩信息的学号科目编号和成绩用逗号分隔(输入"0"返回上一级)\n')
                Grade.grade_insert(grade)
            elif self == '2':
                print('所有学生成绩如下:')
                Grade.grade_all_query(self)
                subfunction.grade(self)
            elif self == '3':
                grade = input('请输入需要查询成绩的学号(输入"0"返回上一级)\n')
                Grade.grade_student_id_query(grade)
            elif self == '4':
                grade = input('请输入需要查询成绩的姓名(输入"0"返回上一级)\n')
                Grade.grade_student_name_query(grade)
            elif self == '5':
                grade = input('请输入修改信息的学号和课程名称与新值并选择类型学号、课程编号、成绩逗号分割(输入"0"返回上一级)\n')
                Grade.grade_student_id_update(grade)
            elif self == '6':
                grade = input('请输入需要删除成绩的学号和科目用逗号分隔(输入"0"返回上一级)\n')
                Grade.grade_student_id_delete(grade)
            elif self == '7':
                grade = input('请输入需要删除所有成绩的学号(输入"0"返回上一级)\n')
                Grade.grade_student_id_all_delete(grade)
            elif self == '0':
                print('退回主菜单')
                function()
            else:
                print('请输入正确的功能序号')
                subfunction.grade(self)



# 学生类
class Student():
    # 学生信息插入
    def student_insert(self):
        if self == '0':
            subfunction.student(self)
        else:
            student_information = self.strip(',').split(',')
            try:
                student_unique = mysql_query.select_student_information(student_information[0])
                if student_unique == ():
                    mysql_insert.insert_student_information(student_information[0], student_information[1], student_information[2], student_information[3], student_information[4], student_information[5])
                else:
                    print('学号已存在')
            except:
                print('请按照规范输入学生信息')


    # 所有学生信息
    def student_all(self):
        if self == '0':
            subfunction.student(self)
        student_information = mysql_query.select_student_all()
        for student_tuple in student_information:
            print('姓名:' + student_tuple[0] + ' 学号:' + student_tuple[1] + ' 性别:' + student_tuple[2] + ' 出生年月:' + str(student_tuple[3]) + ' 院系:' + student_tuple[4] + ' 地址:' + student_tuple[5])


    # 总人数
    def student_total_people(self):
        total_people = mysql_query.select_student_total_people()
        people = str(total_people[0][0])
        print('总人数:' + people + '\n')


    # 根据学生学号查询学生信息显示 姓名，学号，性别
    def student_query(self):
        if self == '0':
            subfunction.student(self)
        student_information = mysql_query.select_student_information(self)
        if student_information == ():
            print('学号不存在')
        else:
            student_tuple = student_information[0]
            student_information_str = '姓名:' + student_tuple[0] + ' 学号:' + student_tuple[1] + ' 性别:' + student_tuple[2] + ' 出生年月:' + str(student_tuple[3]) + ' 院系:' + student_tuple[4] + ' 地址:' + student_tuple[5]
            print(student_information_str)


    # 根据学生名字查询一个或者多个学生信息 显示 姓名，学号，性别
    def student_name_query(self):
        if self == '0':
            subfunction.student(self)
        student_information = mysql_query.select_student_name(self)
        if student_information == ():
            print('姓名不存在')
        else:
            for student_tuple in student_information:
                print('姓名:' + student_tuple[0] + ' 学号:' + student_tuple[1] + ' 性别:' + student_tuple[2] + ' 出生年月:' + str(student_tuple[3]) + ' 院系:' + student_tuple[4] + ' 地址:' + student_tuple[5])


    # 根据地区查询学生信息
    def student_address(self):
        if self == '0':
            subfunction.student(self)
        student_information = mysql_query.select_student_address(self)
        if student_information == ():
            print('地区不存在')
        else:
            for student_tuple in student_information:
                print('姓名:' + student_tuple[0] + ' 学号:' + student_tuple[1] + ' 性别:' + student_tuple[2] + ' 出生年月:' + str(student_tuple[3]) + ' 院系:' + student_tuple[4] + ' 地址:' + student_tuple[5])


    # 根据性别查询学生信息
    def student_gender(self):
        if self == '0':
            subfunction.student(self)
        student_information = mysql_query.select_student_gender(self)
        if student_information == ():
            print('请输入正确的性别')
        else:
            for student_tuple in student_information:
                print('姓名:' + student_tuple[0] + ' 学号:' + student_tuple[1] + ' 性别:' + student_tuple[2] + ' 出生年月:' + str(student_tuple[3]) + ' 院系:' + student_tuple[4] + ' 地址:' + student_tuple[5])


    # 根据年龄查询学生信息
    def student_age(self):
        if self == '0':
            subfunction.student(self)

        year = int(datetime.datetime.now().year) - int(self)
        student_information = mysql_query.select_student_age(year)
        if student_information == ():
            print('该年龄段的学生信息暂无')
        else:
            for student_tuple in student_information:
                print('姓名:' + student_tuple[0] + ' 学号:' + student_tuple[1] + ' 性别:' + student_tuple[2] + ' 出生年月:' + str(student_tuple[3]) + ' 院系:' + student_tuple[4] + ' 地址:' + student_tuple[5])


    # 根据院系查询学生信息
    def student_departments(self):
        if self == '0':
            subfunction.student(self)
        student_information = mysql_query.select_student_departments(self)
        if student_information == ():
            print('请输入正确的院系')
        else:
            for student_tuple in student_information:
                print('姓名:' + student_tuple[0] + ' 学号:' + student_tuple[1] + ' 性别:' + student_tuple[2] + ' 出生年月:' + str(student_tuple[3]) + ' 院系:' + student_tuple[4] + ' 地址:' + student_tuple[5])

    # 根据学生学号 修改 姓名，学号，性别
    def student_update(self):
        if self == '0':
            subfunction.student(self)
        else:
            try:
                subfunction1 = self.strip(',').split(',')
                if subfunction1[2] == '姓名':
                    mysql_update.update_student_name(subfunction1[0], subfunction1[1])
                elif subfunction1[2] == '学号':
                    mysql_update.update_student_id(subfunction1[0], subfunction1[1])
                elif subfunction1[2] == '性别':
                    mysql_update.update_gender(subfunction1[0], subfunction1[1])
                elif subfunction1[2] == '出生年':
                    mysql_update.update_birth(subfunction1[0], subfunction1[1])
                elif subfunction1[2] == '院系':
                    mysql_update.update_departments(subfunction1[0], subfunction1[1])
                elif subfunction1[2] == '地址':
                    mysql_update.update_address(subfunction1[0], subfunction1[1])
            except:
              print('请按照规范输入修改学生信息')

    # 根据学生学号删除学生信息
    def student_delect(self):
        if self == '0':
            subfunction.student(self)
        student_id = mysql_query.select_student_information(self)
        if student_id == ():
            print('该学号不存在')
        else:
            mysql_delete.delete_student_information(self)



# 科目信息类
class Course:
    # 插入科目信息 输入科目名称和科目编号
    def course_insert(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            Course_title = self.strip(',').split(',')
            try:
                course_uniqu = mysql_query.select_course_id(Course_title[0])
                if course_uniqu == ():
                    mysql_insert.insert_course(Course_title[0], Course_title[1])
                else:
                    print('该项目编号已存在')
            except:
                print('请按照规范输入')

    # 查询所有科目的科目名称和科目编号并展示
    def course_all_query(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            all_course_content_list = mysql_query.select_all_course_title()
            for course in all_course_content_list:
                print('科目:' + course[0] + ' 编号:' + course[1])

    # 根据科目名称查询科目名称和科目编号
    def course_course_title_query(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            course_title = mysql_query.select_course_title(self)
            if course_title == ():
                print('该科目名称不存在')
            else:
                course_content_list = mysql_query.select_course_title(self)
                for course in course_content_list:
                    print('科目:' + course[0] + ' 编号:' + course[1])

    # 根据科目编号查询科目名称和科目编号
    def course_course_id_query(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            course_id = mysql_query.select_course_id(self)
            if course_id == ():
                print('该科目编号不存在')
            else:
                course_content_list = mysql_query.select_course_id(self)
                for course in course_content_list:
                    print('科目:' + course[0] + ' 编号:' + course[1])

    # 通过科目名称更改科目名称
    def course_update(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            Course_title = self.strip(',').split(',')
            try:
                mysql_update.update_course_title(Course_title[0], Course_title[1])
            except:
                print('请按照规范填写')

    # 通过科目编号更改科目编号
    def course_course_id_update(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            Course_title = self.strip(',').split(',')
            try:
                mysql_update.update_course_title(Course_title[0], Course_title[1])
            except:
                print('请按照规范填写')

    # 通过科目名称删除科目信息
    def course_course_title_delect(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            course_title_unique = mysql_query.select_course_title(self)
            if course_title_unique == ():
                print('该科目不存在')
            else:
                mysql_delete.delete_course_title(self)

    # 通过科目编号删除科目信息
    def course_course_id_delect(self):
        if self == '0':
            subfunction.subjectinfo(self)
        else:
            course_id_unique = mysql_query.select_course_id(self)
            if course_id_unique == ():
                print('该编号不存在')
            else:
                mysql_delete.delete_course_id(self)


# 成绩类
class Grade:
    # 插入成绩 学号,课程编号,成绩
    def grade_insert(self):
        if self == '0':
            subfunction.grade(self)
        else:
            grade = self.strip(',').split(',')
            try:
                course_id = mysql_query.select_course_title_id(grade[1])
                grade_uniqu = mysql_query.select_grade_uniqu(grade[0], course_id)
                if grade_uniqu == ():
                    mysql_insert.insert_grade_id(grade[0], course_id, grade[2])
                else:
                    print('该成绩已存在')
            except:
                print('请按照规范输入')

    # 查询所有成绩并展示
    def grade_all_query(self):
        if self == '0':
            subfunction.grade(self)
        else:
            grade = mysql_query.select_all_grade()
            for grade_list in grade:
                print('姓名:' + str(grade_list[0]) + ' 学号:' + str(grade_list[1]) + ' 科目:' + str(grade_list[2]) + ' 成绩:' + str(grade_list[3]))

    # 根据学号查询成绩
    def grade_student_id_query(self):
        student_id = mysql_query.select_student_id_grade(self)
        if self == '0':
            subfunction.grade(self)
        elif student_id == ():
            print('学号不存在')
        else:
            grade = mysql_query.select_student_id_grade(self)
            for grade_list in grade:
                print('姓名:' + str(grade_list[0]) + ' 学号:' + str(grade_list[1]) + ' 科目:' + str(grade_list[2]) + ' 成绩:' + str(grade_list[3]))

    # 根据学生名字查询成绩并展示
    def grade_student_name_query(self):
        if self == '0':
            subfunction.grade(self)
        else:
            grade = mysql_query.select_student_name_grade(self)
            for grade_list in grade:
                print('姓名:' + str(grade_list[0]) + ' 学号:' + str(grade_list[1]) + ' 科目:' + str(grade_list[2]) + ' 成绩:' + str(grade_list[3]))

    # 根据学生id修改学生id并同步修改学生表id
    def grade_student_id_update(self):
        if self == '0':
            subfunction.grade(self)
        else:
            grade = self.strip(',').split(',')
            try:
                if grade[2] == '学号':
                    mysql_update.update_grade_student_id(grade[0], grade[1])
                    mysql_update.update_student_id(grade[0], grade[1])
                elif grade[3] == '课程编号':
                    course_id = mysql_query.select_course_title_id(grade[1])
                    new_course_id = mysql_query.select_course_title_id(grade[2])
                    mysql_update.update_grade_course_id(grade[0], course_id, new_course_id)
                elif grade[3] == '成绩':
                    course_id = mysql_query.select_course_title_id(grade[1])
                    mysql_update.update_grade_grade(grade[0], course_id, grade[2])
            except:
                print('请按照规范输入')

    # 根据学号删除对应学生所有成绩
    def grade_student_id_all_delete(self):
        if self == '0':
            subfunction.grade(self)
        else:
            student_grade_unique = mysql_query.select_student_information(self)
            print(student_grade_unique)
            if student_grade_unique == ():
                print('学号不存在')
            else:
                mysql_delete.delete_student_all_grade(self)

    # 根据学号和课程编号(输入课程名称)删除成绩表成绩
    def grade_student_id_delete(self):
        if self == '0':
            subfunction.grade(self)
        else:
            grade = self.strip(',').split(',')
            try:
                student_unique = mysql_query.select_synchronous(grade[0])
                course_unique = mysql_query.select_course_title_id(grade[1])
                if student_unique == ():
                    print('学号不在成绩表存在')
                elif course_unique == ():
                    print('科目不存在')
                elif student_unique and course_unique !=():
                    mysql_delete.delete_student_grade(grade[0], course_unique)
            except:
                print('请按照规范输入')


if __name__ == '__main__':
    function()