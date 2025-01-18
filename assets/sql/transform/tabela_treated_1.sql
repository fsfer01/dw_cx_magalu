-----UM EXEMPLO DE UMA MODELAGEM EM SQL QUE SERÁ SALVA NO BANCO DE DADOS.

CREATE SCHEMA IF NOT EXISTS dw_cx_magalu_treated;

DROP TABLE IF EXISTS dw_cx_magalu_treated.tabela_treated_1;

CREATE TABLE dw_cx_magalu_treated.tabela_treated_1 as (

WITH consulta_1 AS (
    SELECT
    CAST(data as date)              AS dimension_date,
    count(distinct coluna_a)        AS qtd_distinct_coluna_a,
    count(distinct coluna_b)        AS qtd_distinct_coluna_b,
    count(distinct coluna_c)        AS qtd_distinct_coluna_c,
    count(distinct coluna_d)        AS qtd_distinct_coluna_d,
    count(distinct coluna_e)        AS qtd_distinct_coluna_e,
    'dw_cx_magalu_raw.consulta1'    AS origem,
    CURRENT_TIMESTAMP               AS data_de_processamento
    FROM dw_cx_magalu_raw.consulta1
    GROUP BY 1
),

consulta_2 AS (
    SELECT
    CAST(data as date)              AS dimension_date,
    count(distinct coluna_a)        AS qtd_distinct_coluna_a,
    count(distinct coluna_b)        AS qtd_distinct_coluna_b,
    count(distinct coluna_c)        AS qtd_distinct_coluna_c,
    count(distinct coluna_d)        AS qtd_distinct_coluna_d,
    count(distinct coluna_e)        AS qtd_distinct_coluna_e,
    'dw_cx_magalu_raw.consulta2'    AS origem,
    CURRENT_TIMESTAMP               AS data_de_processamento
    FROM dw_cx_magalu_raw.consulta2
    GROUP BY 1
),

treated AS (
SELECT * FROM consulta_1

UNION ALL

SELECT * FROM consulta_2
)

SELECT * FROM treated 

);

select * from dw_cx_magalu_treated.tabela_treated_1