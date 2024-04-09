with source as (

    select * from public.raw_covid_data

),

renamed as (

    select
        load_date as date,
        province_state as state,
        country_region as country,
        confirmed,
        deaths,
        recovered,
        active,
        incident_rate,
        testing_rate,
        people_tested,
        mortality_rate
    from source

)

select * from renamed
