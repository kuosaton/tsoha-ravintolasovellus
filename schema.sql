CREATE TABLE visited_restaurants (
    id SERIAL PRIMARY KEY,
    name	TEXT,
    description TEXT,
    category    TEXT,
    rating       INT,
    review	TEXT,
    address	TEXT
);

CREATE TABLE bucketlist_restaurants (
    id SERIAL PRIMARY KEY,
    name	TEXT,
    description TEXT,
    category    TEXT,
    address	TEXT
);
