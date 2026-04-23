# 1. Creazione Database e Utente
create database eserciziosql;

create user esercizio_user@localhost identified by 'password123';

grant all on eserciziosql.* to esercizio_user@localhost;

# 2. Creazione Tabelle
use eserciziosql;

create table clienti (
id_cliente int primary key auto_increment,
nome varchar(50) not null,
email varchar(100) unique not null
);

create table prodotti (
	id_prodotto int primary key auto_increment,
    nome varchar(50) not null,
    prezzo decimal(10,2) check (prezzo >0)
);

create table ordini(
	id_ordine int primary key auto_increment,
    id_cliente int, 
    foreign key (id_cliente) references clienti(id_cliente) on delete cascade,
    id_prodotto int,
    foreign key (id_prodotto) references prodotti(id_prodotto) on delete cascade,
    quantita int not null check (quantita > 0),
    data_ordine datetime default current_timestamp
);

# 3. Inserimento Dati (DML - INSERT)
insert into clienti (nome, email) 
values ('francesco', 'francesco.miao@gmail.com'), ('giada','giada.miao@gmail.com');

insert into prodotti (nome, prezzo)
values ('piadina',25),('lavatrice',10.5);

insert into ordini (id_cliente, id_prodotto, quantita)
values (1, 1, 55),(2, 2, 78);

# 4. Query di Lettura (SELECT Avanzate)

# Mostra tutti gli ordini con i dettagli del cliente e del prodotto.
select *
from ordini
join clienti using(id_cliente)
join prodotti using(id_prodotto);

# Conta quanti ordini ha effettuato ogni cliente.

