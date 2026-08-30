select
    cast(id as integer) as record_id,
    trim(label) as label,
    cast(value as double) as value
from source('raw', 'records')
