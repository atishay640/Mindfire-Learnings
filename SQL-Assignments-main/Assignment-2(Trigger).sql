# Create database user_db
drop database if exists user_db;
create database user_db;
use user_db;

# Create table User
create table if not exists Users (
id int not null primary key auto_increment,
name varchar(40) not null,
email varchar(70) unique not null,
password varchar(20) not null,
create_date datetime default now(),
status enum('Active', 'InActive')
);

# Create table User deleted
create table if not exists UserDeleted (
user_id int not null primary key,
name varchar(40) not null,
email varchar(70) not null,
password varchar(20) not null,
create_date datetime,
delete_date datetime default now(),
status enum('Active', 'InActive') default 'InActive'
);

# Create table User change password logs
create table if not exists UserPasswordChangeLog (
id int not null primary key auto_increment,
old_password varchar(20) not null,
new_password varchar(20) not null,
update_date datetime default now(),
user_id int,
constraint user_id_fk 
foreign key (user_id) references Users(id) ON DELETE SET NULL
);

# Insert 10 users in Users Table
insert into Users (name, email, password, status) 
values
('Harry', 'harry@gmail.com', '123456781@', 'Active'),
('Ron', 'ron@gmail.com', '123456781@', 'Active'),
('Mike', 'mike@gmail.com', '123456781@', 'Active'),
('John', 'john@gmail.com', '123456781@', 'Active'),
('Juli', 'juli@gmail.com', '123456781@', 'Active'),
('James', 'james@gmail.com', '123456781@', 'Active'),
('Jerry', 'jerry@gmail.com', '123456781@', 'Active'),
('Ram', 'ram@gmail.com', '123456781@', 'Active'),
('Sham', 'sham@gmail.com', '123456781@', 'Active'),
('Atishay', 'atishay@gmail.com', '123456781@', 'Active');



# Create User delete event trigger
DELIMITER //
drop trigger if exists UserDeletedTrigger;
create trigger UserDeletedTrigger after delete on Users
for each row
begin
	insert into UserDeleted(user_id, name, email, password, create_date) values(old.id, old.name, old.email, old.password, old.create_date);
end //

# Create User change password event trigger
drop trigger if exists UserPasswordChangeLogTrigger;
create trigger UserPasswordChangeLogTrigger after update on Users
for each row
begin
	if old.password <> new.password then
        insert into UserPasswordChangeLog(user_id, old_password, new_password)
        values(old.id, old.password, new.password);
    END IF;
end //
DELIMITER ;

