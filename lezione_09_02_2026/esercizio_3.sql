SELECT * FROM its2026.studenti;

#1
select cognome, nome, email, data_nascita from studenti where cognome = 'Verdi' order by nome;

#2
select cognome, nome, email, data_nascita from studenti where genere = 'F' order by cognome and nome;

#3
select cognome, nome, citta, email, data_nascita from studenti where citta != 'Torino' order by citta, cognome, nome;

#4
select cognome, nome, email, data_nascita from studenti where data_nascita >= '2000-01-01' order by data_nascita desc;

#5
select cognome, nome, email, data_nascita from studenti where genere = 'm'  and provincia = 'al' order by provincia, cognome, nome;

#6
select cognome, nome, email, data_nascita, provincia from studenti where provincia  = 'at' or provincia ='no' order by provincia, cognome, nome;

#7
select cognome, nome, email, data_nascita, provincia from studenti where provincia in ('cn', 'at', 'no', 'al') order by provincia, cognome, nome; 

#8
select cognome, nome, email, data_nascita from studenti where data_nascita between '1990-01-01' and '1999-12-31' and genere = 'f' order by data_nascita desc, cognome, nome;

#9
select cognome, nome, email, data_nascita from studenti where data_nascita not between '1990-01-01' and '1999-12-31' and genere = 'f' order by data_nascita desc, cognome, nome;

#10
select cognome, nome, email, data_nascita from studenti where cognome like 'r%' order by cognome, nome;

#11
select cognome, nome, email, data_nascita from studenti where cognome regexp '^(ve|de)' order by cognome, nome;