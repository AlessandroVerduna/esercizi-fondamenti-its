SELECT * FROM its2026.alimenti where proteine between 10 and 20;

SELECT * FROM its2026.alimenti where proteine > 10 and proteine < 20;

SELECT * FROM its2026.alimenti where proteine between 10 and 20 and lipidi between 10 and 20
order by energia desc;

select * from alimenti as a where a.prodotto like '%grissini%' or prodotto like '%tofu%';

select '90% del prodotto' as prodotto, (proteine * 0.9) as proteine_grissini,
(carboidrati * 0.9) as carboidrati_grissini, (lipidi * 0.9) as lipidi_grissini,
(energia * 0.9) as energia_grissini
from alimenti where prodotto like '%grissini%' or prodotto = 'tofu'
;

select categoria, count(*) as numero_prodotti from alimenti 
group by categoria order by numero_prodotti desc;

select * from alimenti where categoria not in ('carne','pesce');

create table dolci_esagerati as select * from alimenti where categoria = 'dolci' 
order by energia desc limit 10;

select * from dolci_esagerati;

create table dolci select * from alimenti where categoria = 'dolci';

select * from dolci union select * from dolci_esagerati;

select categoria, count(prodotto) as 'Numero_prodotti' from alimenti 
group by categoria order by Numero_prodotti desc;

select categoria, count(prodotto) as 'Numero_prodotti', avg(energia) as 'valore_energetico_medio' from alimenti 
group by categoria order by valore_energetico_medio desc;