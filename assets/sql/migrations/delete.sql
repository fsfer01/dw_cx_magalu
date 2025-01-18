DELETE FROM {schema}.{tabela}
WHERE cast(data as date) >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '2 month');