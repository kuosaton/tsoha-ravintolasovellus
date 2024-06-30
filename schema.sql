CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username VARCHAR(30) UNIQUE NOT NULL,
	password TEXT NOT NULL,
	seclevel INTEGER DEFAULT 1
);

CREATE TABLE restaurants (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	description TEXT,
	category VARCHAR(50) NOT NULL,
	address	TEXT,
	business_hours TEXT,
	entry_type INTEGER NOT NULL,
	visible	BOOLEAN DEFAULT TRUE
);

CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants(id) NOT NULL,
	creator_id INTEGER REFERENCES users(id) NOT NULL,
	creator_name VARCHAR(30) REFERENCES users(username),
	title VARCHAR(50) NOT NULL,
	description TEXT,
	rating INTEGER NOT NULL,
	recommendation INTEGER NOT NULL,
	visible	BOOLEAN DEFAULT TRUE
);

CREATE TABLE questions (
	id SERIAL PRIMARY KEY,
	restaurant_id INTEGER REFERENCES restaurants(id) NOT NULL,
	creator_id INTEGER REFERENCES users(id) NOT NULL,
	creator_name VARCHAR(30) REFERENCES users(username),
	content TEXT,
	answered BOOLEAN DEFAULT FALSE,
	visible BOOLEAN DEFAULT TRUE
);

CREATE TABLE answers (
	id SERIAL PRIMARY KEY,
	question_id INTEGER REFERENCES questions(id) NOT NULL,
	creator_id INTEGER REFERENCES users(id) NOT NULL,
	creator_name VARCHAR(30) REFERENCES users(username) NOT NULL,
	content TEXT,
	visible BOOLEAN DEFAULT TRUE
);
