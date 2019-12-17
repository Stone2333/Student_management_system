create table student_information(
student_id varchar(100) not null primary key,
student_name varchar(20) not null,
Gender varchar(20) not null,
birth year,
departments varchar(50) not null,
address varchar(50) not null,
update_time timestamp not null DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)ENGINE=INNODB charset=utf8;


create table course(
course_id varchar(20) not null primary key,
course_title varchar(20) not null,
update_time timestamp not null DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)ENGINE=INNODB charset=utf8;


create table grade_table(
student_id varchar(20) not null,
course_id varchar(20) not null,
grade varchar(20) not null,
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
