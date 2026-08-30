select
    cast(id as integer) as widget_id,
    trim(name) as widget_name,
    cast(price as double) as price
from {{ source('raw', 'widgets') }}
