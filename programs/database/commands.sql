create database python_bank;

use python_bank;

create table customer (account_number int,name varchar(50),balance int, primary key(account_number));

show tables;

select * from customer;

insert into customer (account_number,name,balance,) values (1,'ra',12);


create database onemore_bank;

use onemore_bank;

create table customer (account_number int,name varchar(50),balance int, primary key(account_number));
select * from customer;
insert into customer (account_number,name,balance,) values (1,'some name',12);


create database chase_bank;
create table customer (account_number int,name varchar(50),ssn varchar(4) unique,balance int, primary key(account_number));

-- create table customer_transactions ();
-- create table day_transactions (id int, date_time varchar(10), transaction_type varchar(8),account_number int, primary key(id));
