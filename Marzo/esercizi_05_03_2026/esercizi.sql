# Video games exercises
use its2026;

# 1-------------------------------------------------
select * from games;

# 2-------------------------------------------------
select nome from games;

# 3-------------------------------------------------
select * from games where year = 2020;

# 4-------------------------------------------------
select * from games where genere = 'Action';

# 5-------------------------------------------------
select * from games where publisher = 'Nintendo';

# 6-------------------------------------------------
select * from games where genere = 'Role-playing' and publisher = 'Square Enix';

# 7-------------------------------------------------
select * from games where platform = 'PlayStation';

# 8-------------------------------------------------
select * from games where year < 2000;

# 9-------------------------------------------------
select distinct genere from games;

# 10-------------------------------------------------
select * from games order by year asc;

# 11-------------------------------------------------
select * from games where genere != 'Action' or genere != 'Adventure';

# 12-------------------------------------------------
select * from games where year between 2000 and 2010;

# 13-------------------------------------------------
select nome, publisher from games where year > 2015 order by publisher;

# 14-------------------------------------------------
select count(*) numero_giochi from games;

# 15-------------------------------------------------
select genere, count(*) as numero_giochi from games group by genere order by numero_giochi desc;

# 16-------------------------------------------------
select * from games where year = (select max(year) from games);

# 17-------------------------------------------------
select publisher, count(*) as numero_giochi from games group by publisher order by numero_giochi desc;

# 18-------------------------------------------------
select genere, count(*) as numero_giochi from games group by genere order by numero_giochi desc limit 1;

# 19-------------------------------------------------
select year, count(*) as numero_giochi from games group by year order by numero_giochi desc;

# 20-------------------------------------------------
select * from (select nome, count(distinct platform) as occorrenze from games group by nome) as tabella where occorrenze > 1;

# 21-------------------------------------------------
select * from (select nome, year, count(distinct publisher) as occorrenze from games group by nome, year) as tabella where occorrenze > 1;

select nome, year, count(distinct publisher) as occorrenze from games group by nome, year having occorrenze > 1;

# 22-------------------------------------------------
select * from (select publisher, count(distinct platform) as numero_piattaforme from games group by publisher) as tabella where numero_piattaforme > 1 order by numero_piattaforme desc;

select publisher, count(distinct platform) as numero_piattaforme from games group by publisher having numero_piattaforme > 2 order by numero_piattaforme desc;

# 23-------------------------------------------------
select * from (select platform, year, count(*) as numero_giochi from games group by platform, year) as tabella where numero_giochi > 5 order by numero_giochi desc;

select platform, year, count(*) as numero_giochi from games group by platform, year having numero_giochi > 5 order by numero_giochi desc;

# 24-------------------------------------------------
select * from (select nome, count(distinct genere) as numero_giochi from games group by nome) as tabella where numero_giochi > 1 order by numero_giochi desc;

select nome, count(distinct genere) as numero_giochi from games group by nome having numero_giochi > 1 order by numero_giochi desc;

# 25-------------------------------------------------
select distinct genere, max(totale_giochi) as totale_giochi from 
(select genere, publisher, count(*) as totale_giochi from games group by genere, publisher) as tabella 
group by genere order by totale_giochi desc;

# SOLUZIONE PROVVISORIA

# 26-------------------------------------------------
select platform, nome, year from games where (platform, year ) in 
(select platform, min(year) as anno_minimo from games where platform not like '%,%' group by platform);

# 27-------------------------------------------------
select nome, publisher, genere from games where nome in 
(select nome from games group by nome having count(distinct genere) > 1 or count(distinct publisher) >1);

# 28-------------------------------------------------
select genere, round((count(*) * 100)/(select count(*) from games), 2) as totale 
from games group by genere order by totale desc;

# 29-------------------------------------------------
select rank() over (order by count(*) desc) as ranking, publisher, count(*) as numero_giochi
from games group by publisher order by numero_giochi desc;

# 30-------------------------------------------------
select year, genere, count(*) as totale_giochi, rank() over (partition by year order by count(*) desc) as classifica
from games group by year, genere order by year, classifica;
