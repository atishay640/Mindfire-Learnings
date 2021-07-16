# Create new database
create database ecommerce_schema_db;
use ecommerce_schema_db; 

# Create table Customer
create table Customer (
id int not null primary key auto_increment,
name varchar(40) not null,
email varchar(70) unique not null,
phone char (15) default 'NA',
status enum('Active', 'InActive') default 'InActive'
);

# Create table Product
create table Product (
id int not null primary key auto_increment,
name varchar(40) not null,
price dec (8, 2),
description text, 
image blob not null,	
status enum('Available', 'UnAvailable')
);

# Create table Order Detail
create table OrderDetail (
id int not null primary key auto_increment,
date datetime default now(),
cost dec (8, 2) not null,	
status enum('Pending', 'Accepted', 'Delivered'),
customer_id int not null, 
constraint customer_id_fk
foreign key (customer_id) references Customer(id)
);


# Create table Order Item
create table OrderItem (
id int not null primary key auto_increment,
date datetime default now(),
order_detail_id int not null,
product_id int not null,
constraint order_detail_id_fk
foreign key (order_detail_id) references OrderDetail(id),
constraint product_id_fk
foreign key (product_id) references Product(id)
);

