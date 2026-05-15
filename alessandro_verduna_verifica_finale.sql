# PARTE A - Progettazione e Creazione Tabelle (DDL)

create database ai_lab_alessandro_verduna;

use ai_lab_alessandro_verduna;

#  Tabella: utente_verduna
create table utente_verduna (
	idUtente int primary key auto_increment,
    nome varchar(100) not null,
    cognome varchar(100) not null,
    dataNascita date not null,
    email varchar(255) not null unique,
    ruolo enum('annotatore','admin','ricercatore') not null,
    dataRegistrazione date not null
);

# Tabella: dataset_verduna
create table dataset_verduna (
	idDataset int primary key auto_increment,
    nomeDataset varchar(200) not null,
	descrizione text,
    lingua varchar(50) not null,
    dataCreazione date not null,
    idCreatore int ,
    licenza varchar(100) not null,
    foreign key (idCreatore) references utente_verduna(idUtente)
		on delete restrict
        on update cascade
);

# Tabella: documento_verduna
create table documento_verduna (
	idDocumento int primary key auto_increment,
    titolo varchar(300) not null,
    testo text,
    dataInserimento date not null,
    idDataset int,
    lunghezzaCaratteri int not null,
    foreign key (idDataset) references dataset_verduna(idDataset)
		on delete cascade
		on update cascade
);

# Tabella: annotazione_verduna
create table annotazione_verduna (
	idAnnotazione int primary key auto_increment,
    idDocumento int,
    idUtente int,
    etichetta enum('positivo','negativo','neutro','spam') not null,
    confidenza decimal(3,2) not null check (confidenza >= 0 and confidenza <= 1),
    dataAnnotazione date not null,
    foreign key (idDocumento) references documento_verduna(idDocumento)
		on delete cascade,
    foreign key (idUtente) references utente_verduna(idUtente)
		on delete restrict
);

# Indici e vincoli aggiuntivi

create index idx_annotazione_etichetta 
ON annotazione_verduna(etichetta);

create index idx_documento_dataset 
ON documento_verduna(idDataset);

create unique index idx_dataset_nome 
on dataset_verduna(nomeDataset);

#PARTE B — Inserimento Dati (DML)

# INSERT INTO: utente_verduna
insert into utente_verduna (nome, cognome, dataNascita, email, ruolo, dataRegistrazione)
values
('Alessandro', 'Verduna', '2001-09-25', 'alessandro.verduna@example.com', 'admin', '2024-01-10'),
('Giulia', 'Rossi', '2005-09-20', 'giulia.rossi@example.com', 'annotatore', '2024-02-01'),
('Marco', 'Bianchi', '2004-12-02', 'marco.bianchi@example.com', 'ricercatore', '2024-03-15');

# INSERT INTO: dataset_verduna
insert into dataset_verduna (nomeDataset, descrizione, lingua, dataCreazione, idCreatore, licenza)
values
('Dataset_A', 'Raccolta di testi brevi per analisi del sentiment', 'italiano', '2024-04-01', 1, 'CC-BY'),
('Dataset_B', 'Documenti tecnici per addestramento NLP', 'inglese', '2024-04-10', 2, 'MIT');

# INSERT INTO: documento_verduna
insert into documento_verduna (titolo, testo, dataInserimento, idDataset, lunghezzaCaratteri)
values
('Documento_1', 'Testo di esempio positivo.', '2024-04-02', 1, 120),
('Documento_2', 'Testo neutro per analisi.', '2024-04-02', 1, 150),
('Documento_3', 'Contenuto negativo di prova.', '2024-04-03', 1, 180),
('Documento_4', 'Documento tecnico introduttivo.', '2024-04-11', 2, 300),
('Documento_5', 'Testo.', '2024-04-11', 2, 90),
('Documento_6', 'Altro documento informativo.', '2024-04-12', 2, 210);

# INSERT INTO: annotazione_verduna
insert into annotazione_verduna (idDocumento, idUtente, etichetta, confidenza, dataAnnotazione)
values
(1, 1, 'positivo', 0.90, '2024-04-05'),
(1, 2, 'positivo', 0.75, '2024-04-05'),
(2, 1, 'neutro', 0.80, '2024-04-06'),
(2, 3, 'neutro', 0.70, '2024-04-06'),
(3, 2, 'negativo', 0.85, '2024-04-07'),
(3, 3, 'negativo', 0.60, '2024-04-07'),
(4, 1, 'positivo', 0.65, '2024-04-12'),
(5, 2, 'spam', 0.95, '2024-04-12'),
(5, 3, 'neutro', 0.55, '2024-04-13'),
(4, 2, 'positivo', 0.72, '2024-04-13');


# PARTE C — Query SQL (JOIN, GROUP BY, Funzioni)

# Q1 - JOIN semplice - Per ogni documento mostra: titolo, nomeDataset, lingua, nome e cognome del creatore del dataset.
select
    doc.titolo, dat.nomeDataset, dat.lingua, ut.nome as nome_creatore, ut.cognome as cognome_creatore
from documento_verduna as doc
	join dataset_verduna as dat using (idDataset)
	join utente_verduna as ut on dat.idCreatore = ut.idUtente;

# Q2 - JOIN + filtro - Elenca tutte le annotazioni con etichetta = 'positivo' mostrando: titolo documento, nome e cognome dell'utente, confidenza.
select
	doc.titolo, ut.nome, ut.cognome, an.confidenza
from annotazione_verduna as an
	join documento_verduna as doc using (idDocumento)
    join utente_verduna	as ut on an.idUtente = ut.idUtente
where etichetta = 'positivo';

# Q3-GROUP BY + COUNT - Per ogni dataset mostra il numero totale di documenti presenti (nomeDataset, totaleDocumenti).
select
	dat.nomeDataset, count(*) as totaleDocumenti
from dataset_verduna as dat
	join documento_verduna using (idDataset)
group by dat.nomeDataset;

# Q4- GROUP BY + AVG - Calcola la confidenza media delle annotazioni per ciascuna etichetta (etichetta, confidenzaMedia).
select
	an.etichetta, avg(an.confidenza) as confidenzaMedia
from annotazione_verduna as an
group by an.etichetta;

# Q5- Funzioni su date - Mostra gli utenti registrati dopo una data a tua scelta; visualizza anche l'anno di registrazione tramite la funzione YEAR().
select 
	ut.idUtente, ut.nome, ut.cognome, year(ut.dataRegistrazione) as annoRegistrazione
from utente_verduna as ut
where ut.dataRegistrazione > '2024-04-12';

# Q6 - Subquery (NOT IN / NOT EXISTS) - Trova i documenti che non hanno ancora nessuna annotazione associata.
select 
	doc.idDocumento, doc.titolo
from documento_verduna as doc
 left join (
			select
				doc.idDocumento, doc.titolo
			from documento_verduna as doc 
				inner join annotazione_verduna as an using (idDocumento)
			group by doc.idDocumento, doc.titolo
		) as tabella using (idDocumento)
where tabella.idDocumento is null;

# Q7 - Subquery con aggregazione - Trova l'utente che ha effettuato il maggior numero di annotazioni (nome, cognome, totaleAnnotazioni).
select
	ut.nome, ut.cognome, count(*) totaleAnnotazioni
from utente_verduna as ut
	join annotazione_verduna as an using (idUtente)
group by ut.nome, ut.cognome
order by totaleAnnotazioni desc
	limit 1;

# Q8 - JOIN + GROUP BY + HAVING - Mostra i dataset che hanno almeno 3 documenti e la loro lunghezza media dei caratteri (AVG lunghezzaCaratteri).
select 
	dat.idDataset, dat.nomeDataset, count(*) as numeroDocumenti, round(avg(doc.lunghezzaCaratteri),2) as mediaCaratteri
from dataset_verduna as dat
	join documento_verduna as doc using (idDataset)
group by dat.idDataset, dat.nomeDataset
having numeroDocumenti >= 3;

# Q9 - INVERSA
select 
	doc.titolo, an.etichetta, an. confidenza
from documento_verduna as doc
	join annotazione_verduna as an using (idDocumento);

# Q10 - INVERSA
select 
    dat.nomeDataset, count(an.idAnnotazione) as totaleAnnotazioni
from dataset_verduna as dat
    join documento_verduna as doc using (idDataset)
    join annotazione_verduna as an using (idDocumento)
group by dat.nomeDataset
order by dat.nomeDataset;

# PARTE D - Domande Teoriche

# 1. Qual è la differenza tra chiave primaria e chiave esterna?

/*
 La chiave primaria (PRIMARY KEY) è un attributo o un insieme di attributi
 che identifica in modo univoco ogni record all'interno della propria tabella.
 Non può contenere valori NULL e non può avere duplicati.

 La chiave esterna (FOREIGN KEY), invece, è un attributo che crea un legame
 tra due tabelle, facendo riferimento alla chiave primaria di un'altra tabella.
 Serve a garantire l'integrità referenziale, assicurando che i valori inseriti
 corrispondano a record realmente esistenti nella tabella collegata.
*/

# 2. A cosa serve un indice? In quali casi può peggiorare le prestazioni?

/*
 Un indice è una struttura dati che accelera la ricerca dei record
 all'interno di una tabella, permettendo al database di evitare
 la scansione completa (full table scan) e di individuare più rapidamente
 le righe che soddisfano una certa condizione.

 Tuttavia, un indice può peggiorare le prestazioni in alcuni casi:
 - quando la tabella subisce molti INSERT, UPDATE o DELETE, perché
   ogni modifica richiede anche l’aggiornamento dell’indice;
 - quando viene creato su colonne con bassa selettività (es. valori ripetuti),
   dove il costo di mantenimento supera il beneficio in lettura;
 - quando esistono troppi indici sulla stessa tabella, aumentando
   il lavoro del DBMS durante le operazioni di scrittura.
*/

# 3. Qual è la differenza tra WHERE e HAVING?

/*
 La clausola WHERE viene utilizzata per filtrare i record
 prima che avvengano raggruppamenti o aggregazioni. Agisce
 direttamente sulle righe della tabella e seleziona solo quelle
 che soddisfano una certa condizione.

 La clausola HAVING, invece, viene applicata dopo il GROUP BY
 ed è utilizzata per filtrare i gruppi risultanti da un'aggregazione.
 WHERE non può essere usato con funzioni di aggregazione, mentre
 HAVING sì (ad esempio COUNT, SUM, AVG).
*/

# 4. Cos'è una subquery correlata? Fornisci un breve esempio.
/*
 Una subquery correlata è una sottoquery che dipende dai valori
 della query esterna e viene rieseguita per ogni riga della query principale.
*/
 
# Esempio: trovare gli utenti che hanno creato più di 1 dataset.

select ut.idUtente, ut.nome, ut.cognome
from Utente_verduna as ut
where (
    select count(*)
    from dataset_verduna as dat
    where dat.idCreatore = ut.idUtente
) > 1;

