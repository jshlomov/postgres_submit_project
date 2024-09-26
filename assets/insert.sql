insert into countries (name)
select distinct target_country
FROM mission
where target_country is not NULL
on conflict (name) do nothing;

insert into cities (name, country_id)
select distinct
    m.target_city,
    c.id
from mission m
join countries c on m.target_country = c.name
where m.target_city is not null;
-- on conflict (name) do nothing;

insert into target_types (name)
select distinct target_type
from mission
where target_type is not null
on conflict (name) do nothing;

insert into industries (name)
select distinct target_industry
from mission
where target_industry is not null
on conflict (name) do nothing;

insert into locations (latitude, longitude)
select distinct
    m.target_latitude::decimal,
    m.target_longitude::decimal
from mission m
where m.target_latitude is not null and m.target_longitude is not null
on conflict (latitude, longitude) do nothing;

INSERT INTO targets (
	target_id,
    city_id,
    target_type_id,
    target_industry_id,
    location_id,
    priority
)
SELECT DISTINCT
	m.target_id,
    ci.id,
    tt.id,
    i.id,
    l.id,
    m.target_priority
FROM mission m
JOIN cities ci ON m.target_city = ci.name
LEFT JOIN target_types tt ON m.target_type = tt.name
LEFT JOIN industries i ON m.target_industry = i.name
LEFT JOIN locations l ON
    m.target_latitude = l.latitude AND
    m.target_longitude = l.longitude
WHERE m.target_id IS NOT NULL;
--on conflict (target_id) do nothing;