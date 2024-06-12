CREATE TABLE visited_restaurants (
    id SERIAL PRIMARY KEY,
    name	TEXT,
    description TEXT,
    category    TEXT,
    rating      INT,
    review	TEXT,
    address	TEXT,
    visible	BOOLEAN DEFAULT TRUE
);

CREATE TABLE bucketlist_restaurants (
    id SERIAL PRIMARY KEY,
    name	TEXT,
    description TEXT,
    category	TEXT,
    address	TEXT,
    visible	BOOLEAN DEFAULT TRUE
);

CREATE TABLE favourites (
    id SERIAL PRIMARY KEY,
    visited_id    INTEGER REFERENCES visited_restaurants,
    bucketlist_id INTEGER REFERENCES bucketlist_restaurants,
    visible	  BOOLEAN DEFAULT TRUE
);
