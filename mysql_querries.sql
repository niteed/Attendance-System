#creating database 
create database face_recognition;
use face_recognition;

#creating table for entries
create table entrycsv (
Name varchar(40),
Date varchar(40),
Time varchar(40)
);

use face_recognition;
create table login_data (
Email varchar(40),
password varchar (40)
);

insert into login_data values ('nitee.dhuri@vit.edu.in','19104B0011');
insert into login_data values ('priti.patankar@vit.edu.in','19104B0020');
insert into login_data values ('neelam.bisht@vit.edu.in','19104B0006');