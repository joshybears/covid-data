
with data1 as (

    select * from {{ ref('stg_covid_data') }}

),

final as (

    select
        *
    from 
        data1

)

select * from final
