#creare utente
CREATE USER user@localhost IDENTIFIED BY 'password';

#creare database
CREATE DATABASE provamicrofono;

#assegnare permessi a utente su database
GRANT ALL ON provamicrofono.* TO user@localhost;

#connessione da utente a database

#-------APPUNTI--------
#mysql -u user -p
#enter password --> in questo caso è: "password". Abbiamo indicata come password nel primo passaggio

#creazione di tabella
CREATE TABLE provamicrofono.citta LIKE world.city;

#inserimento / modifica / lettura / eliminazione record
INSERT INTO provamicrofono.citta SELECT * FROM world.city;

SELECT * FROM provamicrofono.citta;
SELECT DISTINCT CountryCode FROM provamicrofono.citta;
SELECT * FROM provamicrofono.citta WHERE CountryCode = 'ITA' AND District = 'Apulia';

SELECT district, SUM(Population) AS Abitanti 
FROM provamicrofono.citta where countrycode = 'ITA'
GROUP BY district ORDER BY Abitanti DESC;

#eliminazione tabella
drop table provamicrofono.citta;

#revocare privilegi
revoke all on provamicrofono.* from user@localhost;

#eliminare database 
drop database provamicrofono;

#eliminare utente
drop user user@localhost;

#-------------------------------------------

# ISTRUZIONI DDL

use its2026;

create table if not exists products (

    product_id int PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    price decimal(6,2) NOT NULL DEFAULT 0.0,
    category enum('abbigliamento', 'casalinghi')

);

ALTER TABLE products
ADD COLUMN price_after_vat DECIMAL(6,2) NOT NULL DEFAULT 0.0;

describe products;

# CRUD su database

# C - CREATE (INSERT INTO)

INSERT INTO products VALUE (NULL, 'Maglia Verde', DEFAULT, 'abbigliamento');

INSERT INTO products (product_id, name, price, category)
VALUES 
(NULL, 'Maglia Verde', 888, 'abbigliamento'),
(NULL, 'Maglia Rossa', 10, 'abbigliamento');

INSERT INTO products (`name`, category)
values ('Maglia Bucata', 'abbigliamento');

# R: READ - RETRIVE (SELECT)

select * from its2026.products;

select name, price from products;

select name as Nome, price as Prezzo from products
ORDER BY Prezzo DESC, Nome;

# U: UPDATE (UPDATE)

UPDATE products
SET price = 5.5
WHERE price = 0.0;

UPDATE products
SET price_after_vat = price * 1.22;

# D: DELETE (DELETE)

DELETE FROM products
WHERE product_id = 4;


DELETE FROM products
WHERE name = 'Maglia Verde';


DELETE FROM products
WHERE name LIKE '%Maglia%';

#----------------------------------------------------

create table magazzino (
    magazzino_id int PRIMARY KEY AUTO_INCREMENT,
    product_id int not NULL,
    quantita INT NOT NULL DEFAULT 0
);

insert into magazzino (product_id, quantita) VALUE (8, 100);
insert into magazzino (product_id, quantita) VALUE (11, 70);
insert into magazzino (product_id, quantita) VALUE (12, 90);

SELECT * FROM magazzino;

SELECT products.name as nome_prodotto, magazzino.quantita as numero_pezzi
from products, magazzino
where products.product_id = magazzino.product_id;

#-----------------PYTHON-----------------
magazzino = [
    ['Maglia Bucata', 100], 
    ['Maglia Verde', 70], 
    ['Maglia Rossa', 90]
]

f = open('magazzino.html', 'w')

f.write('<html>\n')
f.write('<head>\n')
f.write('</head>\n')
f.write('<body>\n')

f.write('<h1> Magazzino prodotti</h1>\n')

f.write('<ul>\n')

for prodotto in magazzino:
    nome = prodotto[0]
    quantita = prodotto[1]
    
    f.write(f"<li>{nome}: {quantita}</li>")



f.write('</ul>\n')

f.write('</body>')
f.write('</html>\n')

f.close()

print("Elaborazione terminata")

