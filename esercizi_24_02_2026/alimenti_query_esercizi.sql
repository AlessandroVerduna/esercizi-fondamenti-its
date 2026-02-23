use its2026;

# 1-----------------------------------------
select * from alimenti;

# 2-----------------------------------------
select * from alimenti where categoria= 'carne';

# 3-----------------------------------------
select count(*) as numero_di_righe from alimenti;

# 4-----------------------------------------
select * from alimenti where proteine > 10;

# 5-----------------------------------------
select* from alimenti order by energia desc limit 5;

# 6-----------------------------------------
select avg(proteine) as media_proteine_della_colonna_carne from alimenti where categoria = 'carne';

# 7-----------------------------------------
select * from alimenti where carboidrati = 0;

# 8-----------------------------------------
select * from alimenti order by lipidi desc limit 1;

# 9-----------------------------------------
select categoria, count(*) as quantità_alimenti from alimenti group by categoria order by quantità_alimenti desc;

# 10-----------------------------------------
select * from alimenti where carboidrati between 10 and 30;

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1-----------------------------------------
select count(*) as numero_alimenti from alimenti;

# 2-----------------------------------------
select avg(proteine) as media_proteine_alimenti from alimenti;

# 3-----------------------------------------
select min(energia) as valore_minimo_energia, max(energia) as valore_massimo_energia from alimenti;

# 4-----------------------------------------
select sum(lipidi) as totale_lipidi from alimenti;

# 5-----------------------------------------
select categoria, count(*) as numero_elementi_per_categoria from alimenti group by categoria order by numero_elementi_per_categoria desc;

# 6-----------------------------------------
select categoria, avg(carboidrati) as media_carboidrati from alimenti group by categoria order by media_carboidrati desc;

# 7-----------------------------------------
select categoria, avg(energia) as media_energia from alimenti group by categoria order by media_carboidrati desc limit 1;

# 8-----------------------------------------
select * from alimenti order by proteine desc limit 1;

# ^^Correzione. La mia soluzione è quella di sopra. Molto interessante la sintassi della sub-query ^^
select prodotto, proteine from alimenti where proteine = (select max(proteine) from alimenti);

# 9-----------------------------------------
select categoria, sum(energia) as somma_energia from alimenti group by categoria order by somma_energia desc;

# 10-----------------------------------------
select count(*) as prodotti_con_proteine_maggiore_di_10 from alimenti where proteine > 10;
