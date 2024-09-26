CREATE TABLE IF NOT EXISTS countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INT NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(id),
    CONSTRAINT unique_city_country UNIQUE (name, country_id)
);

CREATE TABLE IF NOT EXISTS locations (
    id SERIAL PRIMARY KEY,
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    CONSTRAINT unique_loc UNIQUE (latitude, longitude)
);

CREATE TABLE IF NOT EXISTS target_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS industries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS targets (
    id SERIAL PRIMARY KEY,
    city_id int NOT NULL,
    target_type_id int,
    target_industry_id int,
    location_id int,
	priority int,
    FOREIGN KEY (city_id) REFERENCES cities(id),
    FOREIGN KEY (target_industry_id) REFERENCES industries(id),
    FOREIGN KEY (target_type_id) REFERENCES target_types(id),
    FOREIGN KEY (location_id) REFERENCES locations(id)
);