use its2026;

select * from alimenti;

select categoria, avg(energia) as media_energia from alimenti group by categoria order by media_energia desc limit 1;

select categoria, avg(energia) from alimenti having avg(energia) = max(avg(energia));
#(select * from alimenti where (select categoria, avg(energia) as media_energia from alimenti));

select prodotto, proteine from alimenti where proteine = (select max(proteine) from alimenti);

select count(proteine < 10) as alimenti_pro from alimenti;

select count(*) as prodotti_con_proteine_maggiore_di_10 from alimenti where proteine > 10;

SELECT categoria, AVG(energia) AS media_energia
FROM alimenti
GROUP BY categoria
HAVING AVG(energia) = (
    SELECT MAX(media_cat)
    FROM (
        SELECT AVG(energia) AS media_cat
        FROM alimenti
        GROUP BY categoria
    ) AS t
);

select categoria, max(energia) from (select categoria, avg(energia) as energia from alimenti group by categoria) as miao group by categoria order by energia desc limit 1;     
alimenti where avg(energia) = (select * from alimenti where 

23:06:44	select categoria, max(energia) from (select categoria as categoria, avg(energia) as energia from alimenti group by categoria) as alimenti LIMIT 0, 1000	Error Code: 1140. In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'alimenti.categoria'; this is incompatible with sql_mode=only_full_group_by	0.000 sec


