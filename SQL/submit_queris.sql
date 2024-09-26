

EXPLAIN ANALYZE SELECT DISTINCT ON (target_city) target_city, air_force, c
FROM (
    SELECT target_city, air_force, COUNT(air_force) AS c
    FROM mission
    WHERE EXTRACT(YEAR FROM mission_date) = 1942
    GROUP BY target_city, air_force
) AS subquery
ORDER BY target_city, c DESC;

CREATE INDEX index_bomb_damage_assessment ON mission (bomb_damage_assessment)
DROP INDEX IF EXISTS index_bomb_damage_assessment;


explain analyze select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1

CREATE INDEX index_bomb_damage_assessment ON mission (bomb_damage_assessment)
DROP INDEX IF EXISTS index_bomb_damage_assessment;
