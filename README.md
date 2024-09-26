# World War II Database Project

This project is a Flask web application that interacts with a database containing data about the Second World War. It utilizes SQLAlchemy ORM to perform CRUD operations and execute queries that explore historical data such as air force activities in different cities during the war.

## Features

- **Flask application**
- **SQLAlchemy ORM** for database interactions
- **CRUD operations** 
- Complex queries
  
## Installation

```bash
git clone https://github.com/jshlomov/postgres_submit_project.git
source venv/bin/activate
pip install -r requirements.txt
```


## API Endpoints

- **Get all targets**
  - `GET /targets`
  
- **Get target by ID**
  - `GET /targets/<target_id>`

- **Create a new target**
  - `POST /targets`
  
- **Update an existing target**
  - `PUT /targets/<target_id>`
  
- **Delete a target**
  - `DELETE /targets/<target_id>`

## SQL main queries

```sql
EXPLAIN ANALYZE SELECT DISTINCT ON (target_city) target_city, air_force, c
FROM (
    SELECT target_city, air_force, COUNT(air_force) AS c
    FROM mission
    WHERE EXTRACT(YEAR FROM mission_date) = 1942
    GROUP BY target_city, air_force
) AS subquery
ORDER BY target_city, c DESC;

CREATE INDEX index_mission_date ON mission (EXTRACT(YEAR FROM mission_date));
DROP INDEX IF EXISTS index_mission_date;

EXPLAIN ANALYZE SELECT bomb_damage_assessment, COUNT(target_country) FROM mission
WHERE bomb_damage_assessment IS NOT NULL
AND airborne_aircraft > 5
GROUP BY target_country, bomb_damage_assessment
ORDER BY COUNT(bomb_damage_assessment) DESC LIMIT 1;

CREATE INDEX index_bomb_damage_assessment ON mission (bomb_damage_assessment);
DROP INDEX IF EXISTS index_bomb_damage_assessment;
```

## Analyze data

**In the "Details" file in SQL directory**



