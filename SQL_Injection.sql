create database sql_i;

use sql_i;
create table student(
	id varchar(20), 
    Stud_name varchar(20), 
    reg_no varchar(20) primary key not null, 
    branch varchar(20));

insert into student values ("1", "gayathri", "19a001", "ds");
insert into student values ("2", "devi", "19b002", "civil");
insert into student values ("3", "neeraja", "19c003", "mech");
insert into student values ("4", "meenu", "19d004", "eee");
insert into student values ("5", "bhums", "19e005", "it");
select * from student;

create table marks(
	s_no varchar(20) primary key,
	mark1 int,
    mark2 int,
    mark3 int,
    reg_no varchar(20),
    foreign key (reg_no) references student(reg_no));

insert into marks values ("1", 50, 60, 70, "19a003");
insert into marks values ("2", 85, 90, 95, "19b005");

create table register(
	reg_no varchar(20) primary key not null,
    pass varchar(20));

insert into register values ("19x006", "abcd");
insert into register values ("19z007", "cdef");

select * from register;
