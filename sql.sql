create table Student_information(
id int auto_increment primary key,
Student_Name varchar(20) not null,
Student_id varchar(100) not null unique,
Gender varchar(20) not null,
update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
INDEX(Student_id)
)ENGINE=INNODB charset=utf8;


create table Subjectinfo(
id int auto_increment primary key,
Course_title varchar(20) not null,
Course_id varchar(20) not null unique,
update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
INDEX(Course_id)
)ENGINE=INNODB charset=utf8;


create table Grade_table(
id int auto_increment primary key,
Student_id varchar(20) not null ,
Course_id varchar(20) not null,
Grade varchar(20) not null,
update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)ENGINE=INNODB charset=utf8;

-- 根据学号查名字和成绩
select student_information.Student_Name,grade_table.Student_id,grade_table.Course_id,grade_table.Grade from student_information left join grade_table on student_information.Student_id=grade_table.Student_id WHERE grade_table.Student_id = '123';

-- 根据学号查名字科目和成绩
select student_information.Student_Name,grade_table.Student_id,subjectinfo.Course_title,grade_table.Grade from student_information
left join grade_table on student_information.Student_id=grade_table.Student_id
left join  subjectinfo on grade_table.Course_id=subjectinfo.Course_id
WHERE grade_table.Student_id = '456';

select Student_id FROM student_information WHERE Student_id = '444';
