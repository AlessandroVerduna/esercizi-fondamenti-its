#create database libreria;
truncate table autori;
use libreria;

create table editori(
	editore_id int primary key auto_increment,
	nome varchar(100),
    contatto varchar(100)
);

create table libri(
	libro_id int primary key auto_increment,
    titolo varchar(100),
	prezzo decimal(6,2),
    pagine int,
    editore_id int
);

create table autori(
	autore_id int primary key auto_increment,
	nome varchar(30),
    cognome varchar(50),
    nazionalita char(2)
);

create table autori_libri(
	autore_id int,
    libro_id int,
	primary key(autore_id, libro_id)
);

truncate table autori_libri;

#INSERT INTO autori_libri VALUES (1,3),(2,8),(3,5),(4,11),(5,6),(6,2),(7,4),(8,12),(9,13),(10,9),(11,1),(12,7),(13,16),(14,18),(14,19),(15,1),(16,14),(17,2),(18,17),(19,15),(20,10),(21,20),(22,21);
#INSERT INTO autori VALUES (1,'John Ronald Reuel','Tolkien','za'),(2,'Dan','Brown','us'),(3,'Paulo','Coelho','br'),(4,'J. D.','Salinger','us'),(5,'Agatha','Christie','en'),(6,'J. K.','Rowling','en'),(7,'Tsao','Chan','cn'),(8,'E. L.','James','en'),(9,'Antoine','de Saint-Exup?ry','fr'),(10,'Charles','Dickens','en'),(11,'Miguel','de Cervantes','es'),(12,'Clive Staples','Lewis','en'),(13,'Tse-tung','Mao','cn'),(14,'Michele','Rech, Zerocalcare','it'),(15,'Andrea','Camilleri','it'),(16,'Ken','Follett','en'),(17,'Kazuo','Ishiguro','jp'),(18,'Carlo','Fruttero','it'),(19,'Franco','Lucentini','it'),(20,'Italo','Calvino','it'),(21,'Stephen','King','us'),(22,'Isabel','Allende','cl');
#INSERT INTO editori VALUES (1,'Mondadori','info-mondadori@gmail.com'),(3,'Einaudi','amm-einaudi@gmail.com'),(4,'Salani','salani-info@gmail.com'),(5,'Edizioni Clandestine','clandestine-info@gmail.com'),(6,'Bao Publishing','bao_editore@gmail.com'),(7,'Sellerio','amm-sellerio@gmail.com'),(8,'BUR','bur_editore@gmail.com'),(9,'Sperling & Kupfer','sperling-info@gmail.com'),(10,'Bompiani','contact-bompiani@gmail.com'),(11,'Adelphi','adelphi-info@gmail.com');
#INSERT INTO libri VALUES (1,'Alchimista (L\')',12.00,10,1),(2,'Cinquanta sfumature di grigio',10.20,560,1),(3,'Dieci piccoli indiani',10.20,208,1),(4,'Don Chisciotte della Mancha',20.40,NULL,3),(5,'Harry Potter e la Pietra Filosofale',8.50,302,4),(6,'Il Codice da Vinci',11.00,512,1),(7,'Il giovane Holden',10.20,251,3),(8,'Il leone, la strega e l\'armadio',7.65,182,1),(9,'Il libretto rosso',7.22,160,5),(10,'Il Piccolo Principe',4.25,95,1),(11,'Il Signore degli Anelli: La compagnia dell\'anello. Le due torri. Il ritorno del re',25.00,1255,10),(12,'Il sogno della camera rossa. Romanzo cinese del XVIII secolo',15.30,721,3),(13,'La colonna di fuoco',27.00,912,1),(14,'La donna della domenica',12.00,434,1),(15,'Lo Hobbit',9.35,417,10),(16,'Macerie prime',14.45,192,6),(17,'Origin',21.25,564,1),(18,'Quel che resta del giorno',12.00,276,3),(19,'Un mese con Montalbano',12.75,512,7),(20,'Una storia tra due citt├á',9.77,600,10),(21,'Marcovaldo',10.00,120,7),(22,'IT',25.00,550,9),(23,'gomorra',12.59,345,1);

insert into libreria.editori
select * from esercizio.editore;

insert into libreria.autori
select * from esercizio.autore;

insert into libreria.autori_libri
select autore_id, libro_id from esercizio.autore_libro;

insert into libreria.libri
select * from esercizio.libro;

use libreria;

select * from libri as l, editori as e where l.editore_id = e.editore_id;

select * from libri as l join editori as e on l.editore_id = e.editore_id;

select l.*, e.nome from libri as l join editori as e on l.editore_id = e.editore_id;

select l.*, e.nome from libri as l right join editori as e on l.editore_id = e.editore_id;

select * from autori;

select l.titolo, concat(a.nome, ' ', a.cognome) as autore,
e.nome as editore from libri l 
left join editori e on l.editore_id = e.editore_id
left join autori_libri al on l.libro_id = al.libro_id
left join autori a on a.autore_id = al.autore_id;

use its2026;

select * from games;

select genere, count(*) as numero_giochi from games group by genere having numero_giochi > 10 order by numero_giochi desc;


