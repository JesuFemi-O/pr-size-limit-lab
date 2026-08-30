select
    count(*) as widget_count,
    avg(price) as avg_price
from {{ ref('stg_widgets') }}
