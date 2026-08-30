select date_trunc('day', ts) as day, avg(temp_c) as avg_temp_c
from ref('stage_readings') group by 1
