select date_trunc('day', ts) as day, avg(temp_c) as avg_temp_c
from {{ ref('stg_readings') }} group by 1
