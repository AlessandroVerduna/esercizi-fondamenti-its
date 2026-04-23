Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 8.4.8 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database eserciziosql;
Query OK, 1 row affected (0.02 sec)

mysql> 
mysql> create user esercizio_user@localhost identified by 'its2026';
Query OK, 0 rows affected (0.02 sec)

mysql> 
mysql> grant all on eserciziosql.* to esercizio_user@localhost;
Query OK, 0 rows affected (0.01 sec)

mysql> 
mysql> use eserciziosql;
Database changed
mysql> 
mysql> create table clienti (
    -> id_cliente int primary key auto_increment,
    -> nome varchar(50) not null,
    -> email varchar(100) unique not null
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> notee;
