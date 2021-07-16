# Create new database
drop database if exists ecommerce_db;
create database ecommerce_db;
use ecommerce_db; 

# Create table Customer
create table if not exists Customer (
id int not null primary key auto_increment,
name varchar(40) not null,
email varchar(70) unique not null,
phone char (15) default 'NA',
status enum('Active', 'InActive') default 'InActive'
);

# Create table Product
create table if not exists Product (
id int not null primary key auto_increment,
name varchar(40) not null,
product_code varchar(50) not null unique,
price dec (8, 2),
product_description varchar (500), 
status enum('Available', 'UnAvailable') default 'Available'
);

create index product_code_description_index on Product (product_code, product_description);

# Create table Order Detail
create table if not exists OrderDetail (
id int not null primary key auto_increment,
order_id varchar(50) not null unique,
date datetime default now(),
cost dec (8, 2) not null,	
status enum('Pending', 'Accepted', 'Delivered'), 
customer_id int not null, 
constraint customer_id_fk
foreign key (customer_id) references Customer(id) on delete cascade
);


# Create table Order Item
create table if not exists OrderItem (
id int not null primary key auto_increment,
date datetime default now(),
order_detail_id int not null,
product_id int not null,
constraint order_detail_id_fk
foreign key (order_detail_id) references OrderDetail(id) on delete cascade,
constraint product_id_fk
foreign key (product_id) references Product(id) on delete cascade
);


# Insert 10 products
insert into Product (name, product_code, price, product_description) 
values 
('Toothpaste', 5221, 162.00, 'Dabur Red Toothpaste - Buy 3 Get 1 Free'),
('Vaseline', 277, 277.00, 'Vaseline Total Moisture Body Lotion'),
('Hair Oil', 248, 248.00, 'Nihar Naturals Shanti Amla Hair Oil - Pack of 2'),
('Razor', 322, 322.00, 'Gillette Mach 3 Men''s Razor (1 Cartridge)'),
('Soap', 263, 263.00, '17% OFF Santoor Sandal & Turmeric Soap - Pack of 8'),
('Face Wash', 193, 192.00, 'Lakme Blush & Glow Freshness Gel with Lemon Extracts Face Wash'),
('Vaseline 2', 2772, 1277.00, '2 Vaseline Total Moisture Body Lotion'),
('Hair Oil 2', 2482, 1248.00, '2 Nihar Naturals Shanti Amla Hair Oil - Pack of 2'),
('Razor 2', 3222, 1322.00, '2 Gillette Mach 3 Men''s Razor (1 Cartridge)'),
('Soap 2', 2623, 2163.00, '2 Santoor Sandal & Turmeric Soap - Pack of 8');

# Insert 10 users in Users Table
insert into Customer (name, email, phone, status) 
values
('Harry', 'harry@gmail.com', '9981812837', 'Active'),
('Ron', 'ron@gmail.com', '9981812837', 'Active'),
('Mike', 'mike@gmail.com', '9981812837', 'Active'),
('John', 'john@gmail.com', '9981812837', 'Active'),
('Juli', 'juli@gmail.com', '9981812839', 'Active'),
('James', 'james@gmail.com', '9981812837', 'Active'),
('Jerry', 'jerry@gmail.com', '9981812837', 'Active'),
('Ram', 'ram@gmail.com', '9981812837', 'Active'),
('Shyam', 'shyam@gmail.com', '9981812837', 'Active'),
('Atishay', 'atishay@gmail.com', '9981812837', 'Active');


# Insert order details
insert into OrderDetail (order_id, cost, status, customer_id)
values
('ord11100', 5000, 'Accepted', 1 ),
('ord11103', 500, 'Accepted', 3 ),
('ord11105', 3000, 'Accepted', 5 ),
('ord11106', 1000, 'Accepted', 6 ),
('ord11108', 7000, 'Accepted', 9 )
;


# Insert order items
insert into OrderItem (order_detail_id, product_id)
values
(1, 1),
(1, 3),
(1, 7),
(2, 8),
(3, 4),
(3, 5),
(3, 6),
(4, 1),
(5, 1),
(5, 2),
(5, 3),
(5, 4),
(5, 5);

# Search by product description 
explain select * from Product where product_description like '%hair%';

# Find 2nd highest product name, price
explain select name, price from Product where price = (select MAX(price) from Product where price <> (select MAX(price) from Product));

# Find all orders and product details.
explain select OrderItem.id, OrderItem.order_detail_id, Product.name from Product right join OrderItem on Product.id = OrderItem.product_id;

