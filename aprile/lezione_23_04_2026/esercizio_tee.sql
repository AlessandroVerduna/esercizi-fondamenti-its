Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 12
Server version: 8.4.8 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> # 1. Creazione Database e Utente
Query OK, 0 rows affected (0.00 sec)

mysql> create database eserciziosql;
Query OK, 1 row affected (0.00 sec)

mysql> 
mysql> create user esercizio_user@localhost identified by 'password123';
Query OK, 0 rows affected (0.01 sec)

mysql> 
mysql> grant all on eserciziosql.* to esercizio_user@localhost;
Query OK, 0 rows affected (0.00 sec)

mysql> 
mysql> # 2. Creazione Tabelle
Query OK, 0 rows affected (0.00 sec)

mysql> use eserciziosql;
Database changed
mysql> 
mysql> create table clienti (
    -> id_cliente int primary key auto_increment,
    -> nome varchar(50) not null,
    -> email varchar(100) unique not null
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql> 
mysql> create table prodotti (
    -> 	id_prodotto int primary key auto_increment,
    ->     nome varchar(50) not null,
    ->     prezzo decimal(10,2) check (prezzo >0)
    -> );
Query OK, 0 rows affected (0.01 sec)

mysql> 
mysql> create table ordini(
    -> 	id_ordine int primary key auto_increment,
    ->     id_cliente int, 
    ->     foreign key (id_cliente) references clienti(id_cliente) on delete cascade,
    ->     id_prodotto int,
    ->     foreign key (id_prodotto) references prodotti(id_prodotto) on delete cascade,
    ->     quantita int not null check (quantita > 0),
    ->     data_ordine datetime default current_timestamp
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql> 
mysql> # 3. Inserimento Dati (DML - INSERT)
Query OK, 0 rows affected (0.00 sec)

mysql> insert into clienti (nome, email) 
    -> values ('francesco', 'francesco.miao@gmail.com'), ('giada','giada.miao@gmail.com');
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> 
mysql> insert into prodotti (nome, prezzo)
    -> values ('piadina',25),('lavatrice',10.5);
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> 
mysql> insert into ordini (id_cliente, id_prodotto, quantita)
    -> values (1, 1, 55),(2, 2, 78);
Query OK, 2 rows affected (0.00 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> 
mysql> # 4. Query di Lettura (SELECT Avanzate)
Query OK, 0 rows affected (0.00 sec)

mysql> 
mysql> # Mostra tutti gli ordini con i dettagli del cliente e del prodotto.
Query OK, 0 rows affected (0.00 sec)

mysql> select *
    -> from ordini
    -> join clienti using(id_cliente)
    -> join prodotti using(id_prodotto);
+-------------+------------+-----------+----------+---------------------+-----------+--------------------------+-----------+--------+
| id_prodotto | id_cliente | id_ordine | quantita | data_ordine         | nome      | email                    | nome      | prezzo |
+-------------+------------+-----------+----------+---------------------+-----------+--------------------------+-----------+--------+
|           1 |          1 |         1 |       55 | 2026-04-23 21:46:45 | francesco | francesco.miao@gmail.com | piadina   |  25.00 |
|           2 |          2 |         2 |       78 | 2026-04-23 21:46:45 | giada     | giada.miao@gmail.com     | lavatrice |  10.50 |
+-------------+------------+-----------+----------+---------------------+-----------+--------------------------+-----------+--------+
2 rows in set (0.00 sec)

mysql> 
mysql> # Conta quanti ordini ha effettuato ogni cliente.
Query OK, 0 rows affected (0.00 sec)

mysql> select clienti.id_cliente, clienti.nome, count(*) as numero_ordini
    -> from clienti 
    -> join ordini using (id_cliente)
    -> group by clienti.id_cliente, clienti.nome;
+------------+-----------+---------------+
| id_cliente | nome      | numero_ordini |
+------------+-----------+---------------+
|          1 | francesco |             1 |
|          2 | giada     |             1 |
+------------+-----------+---------------+
2 rows in set (0.00 sec)

mysql> 
mysql> # Mostra solo i clienti che hanno effettuato pi  di un ordine.
Query OK, 0 rows affected (0.00 sec)

mysql> select clienti.id_cliente, clienti.nome, count(*) as numero_ordini
    -> from clienti 
    -> join ordini using (id_cliente)
    -> group by clienti.id_cliente, clienti.nome
    -> having numero_ordini > 1;
Empty set (0.00 sec)

mysql> 
mysql> # Calcola il totale speso da ogni cliente.
Query OK, 0 rows affected (0.00 sec)

mysql> select clienti.id_cliente, clienti.nome, sum(prodotti.prezzo) as somma_ordini
    -> from clienti 
    -> join ordini using (id_cliente)
    -> join prodotti using (id_prodotto)
    -> group by clienti.id_cliente, clienti.nome;
+------------+-----------+--------------+
| id_cliente | nome      | somma_ordini |
+------------+-----------+--------------+
|          1 | francesco |        25.00 |
|          2 | giada     |        10.50 |
+------------+-----------+--------------+
2 rows in set (0.00 sec)

mysql> 
mysql> # 5. Update e Delete con Vincoli
Query OK, 0 rows affected (0.00 sec)

mysql> SET SQL_SAFE_UPDATES = 0;
Query OK, 0 rows affected (0.00 sec)

mysql> 
mysql> # Aggiorna il prezzo del prodotto "Lavatrice" portandolo a 1300.00.
Query OK, 0 rows affected (0.00 sec)

mysql> UPDATE prodotti
    -> SET prezzo = 1300
    -> WHERE nome = 'lavatrice';
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> 
mysql> # Prova a eliminare un cliente che ha ordini associati. Cosa succede? 
Query OK, 0 rows affected (0.00 sec)

mysql> # Riesco a eliminarlo nonostante avesse ordini associati. Vengono eliminati anche gli ordini a suo carico
Query OK, 0 rows affected (0.00 sec)

mysql> DELETE FROM clienti
    -> WHERE id_cliente = 1;
Query OK, 1 row affected (0.00 sec)

mysql> 
mysql> # Elimina un ordine specifico dalla tabella Ordini.
Query OK, 0 rows affected (0.00 sec)

mysql> # Viene eliminato l'ordine ma non il cliente a suo carico
Query OK, 0 rows affected (0.00 sec)

mysql> DELETE FROM ordini
    -> where id_ordine = 2;
Query OK, 1 row affected (0.00 sec)

mysql> 
mysql> # 6. Test dei Vincoli (FOREIGN KEY, CHECK)
Query OK, 0 rows affected (0.00 sec)

mysql> 
mysql> # Prova a inserire un ordine con una quantit  negativa. Il database lo permette? Perch ?
Query OK, 0 rows affected (0.00 sec)

mysql> # Non lo consente perch  il parametro check (quantita > 0) ne impedisce l'inserimento in quanto la richiesta non   soddisfatta
Query OK, 0 rows affected (0.00 sec)

mysql> insert into ordini (id_cliente, id_prodotto, quantita) values (2, 1, -5);
ERROR 3819 (HY000): Check constraint 'ordini_chk_1' is violated.
mysql> 
mysql> # 7. Eliminazione Dati, Tabelle e Database
Query OK, 0 rows affected (0.00 sec)

mysql> 
mysql> # Elimina tutti gli ordini dalla tabella Ordini.
Query OK, 0 rows affected (0.00 sec)

mysql> delete from ordini;
Query OK, 0 rows affected (0.00 sec)

mysql> 
mysql> # Elimina la tabella Ordini, seguita dalle tabelle Clienti e Prodotti.
Query OK, 0 rows affected (0.00 sec)

mysql> drop table ordini;
Query OK, 0 rows affected (0.01 sec)

mysql> drop table clienti;
Query OK, 0 rows affected (0.01 sec)

mysql> drop table prodotti;
Query OK, 0 rows affected (0.01 sec)

mysql> 
mysql> # Rimuovi l'utente 'esercizio_user'.
Query OK, 0 rows affected (0.00 sec)

mysql> DROP USER 'esercizio_user'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql> 
mysql> # Elimina il database EsercizioSQL.
Query OK, 0 rows affected (0.00 sec)

mysql> drop database eserciziosql;
Query OK, 0 rows affected (0.01 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| its2026            |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
7 rows in set (0.00 sec)

mysql> notee
