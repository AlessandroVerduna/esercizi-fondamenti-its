use its2026;

drop table products;

create table Products(
	code char(8) primary key,
    name varchar(30),
    price decimal(6,2),
    quantity int check(quantity <= 100)
);

describe products;

alter table products add column description varchar(100) after name;

create table orders (
	id int primary key auto_increment,
    order_data date,
    total decimal(10,2),
    shipping enum('delivered', 'shipped', 'ship'),
    shipping_address varchar(100),
    customer_id int
);

create table clienti (
	id int primary key,
    first_name varchar(30),
    last_name varchar(30),
    email varchar(100),
    address varchar(100),
    city VARCHAR(50),
    province char(2),
    region varchar(30),
    registration_date date
);

alter table clienti modify last_name varchar(50), 
add column phone varchar(20) after last_name, 
add column postal_code char(5) after region;

create table america (
	id int primary key,
    state varchar(50),
    capital_id int check( capital_id <= 255),
    population int check(population < 4500000000)
);

create table asia (
	id int primary key,
    state varchar(50),
    capital_id int check( capital_id <= 255),
    population int check(population < 4500000000)
);

create table africa (
	id int primary key,
    state varchar(50),
    capital_id int check( capital_id <= 255),           #tinyint unsigned --> mi occupa 255 caselle
    population int check(population < 4500000000)
);

create table books (
	isbn char(13) primary key,
    title varchar(100),
    price decimal(6,2),
    price_vat decimal(6,2),
    pages int,
    editor_id int
);

rename table clienti to customers;