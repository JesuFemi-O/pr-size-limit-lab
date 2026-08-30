select
    count(*) as record_count,
    avg(value) as avg_value
from ref('stage_records')
