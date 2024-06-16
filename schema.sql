CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT,
	password TEXT,
	seclevel INTEGER
);

CREATE TABLE restaurants (
	id SERIAL PRIMARY KEY,
	name TEXT,
	description TEXT,
	category TEXT,
	address	TEXT,
	business_hours TEXT,
	entry_type INTEGER,
	visible	BOOLEAN DEFAULT TRUE
);

CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants,
	user_id INTEGER REFERENCES users,
	user_name TEXT,
	title TEXT,
	description TEXT,
	rating INTEGER,
	recommendation INTEGER,
	visible	BOOLEAN DEFAULT TRUE
);

CREATE TABLE questions (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	user_name TEXT,
	restaurant_id INTEGER REFERENCES restaurants,
	content TEXT,
	visible BOOLEAN DEFAULT TRUE
);

CREATE TABLE answers (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES users,
	user_name TEXT,
	question_id INTEGER REFERENCES questions,
	content TEXT,
	visible BOOLEAN DEFAULT TRUE
);
