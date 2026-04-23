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
select clienti.id_cliente, clienti.nome, count(*) as numero_ordini
from clienti 
join ordini using (id_cliente)
group by clienti.id_cliente, clienti.nome;

# Mostra solo i clienti che hanno effettuato più di un ordine.
select clienti.id_cliente, clienti.nome, count(*) as numero_ordini
from clienti 
join ordini using (id_cliente)
group by clienti.id_cliente, clienti.nome
having numero_ordini > 1;

# Calcola il totale speso da ogni cliente.
select clienti.id_cliente, clienti.nome, sum(prodotti.prezzo) as somma_ordini
from clienti 
join ordini using (id_cliente)
join prodotti using (id_prodotto)
group by clienti.id_cliente, clienti.nome;

# 5. Update e Delete con Vincoli
SET SQL_SAFE_UPDATES = 0;

# Aggiorna il prezzo del prodotto "Lavatrice" portandolo a 1300.00.
UPDATE prodotti
SET prezzo = 1300
WHERE nome = 'lavatrice';

# Prova a eliminare un cliente che ha ordini associati. Cosa succede? 
# Riesco a eliminarlo nonostante avesse ordini associati. Vengono eliminati anche gli ordini a suo carico
DELETE FROM clienti
WHERE id_cliente = 1;

# Elimina un ordine specifico dalla tabella Ordini.
# Viene eliminato l'ordine ma non il cliente a suo carico
DELETE FROM ordini
where id_ordine = 2;

# 6. Test dei Vincoli (FOREIGN KEY, CHECK)

# Prova a inserire un ordine con una quantità negativa. Il database lo permette? Perché?
# Non lo consente perché il parametro check (quantita > 0) ne impedisce l'inserimento in quanto la richiesta non è soddisfatta
insert into ordini (id_cliente, id_prodotto, quantita) values (2, 1, -5);

# 7. Eliminazione Dati, Tabelle e Database

# Elimina tutti gli ordini dalla tabella Ordini.
delete from ordini;

# Elimina la tabella Ordini, seguita dalle tabelle Clienti e Prodotti.
drop table ordini;
drop table clienti;
drop table prodotti;

# Rimuovi l'utente 'esercizio_user'.
DROP USER 'esercizio_user'@'localhost';

# Elimina il database EsercizioSQL.
drop database eserciziosql;