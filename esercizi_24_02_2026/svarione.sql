use its2026;

select * from alimenti;

select categoria, avg(energia) as media_energia from alimenti group by categoria order by media_energia desc limit 1;

select categoria, energia from (select categoria, avg(energia) as energia from alimenti group by categoria) as miao where energia = (select max(energia) from (select avg(energia) as energia from alimenti group by categoria) as t);     
