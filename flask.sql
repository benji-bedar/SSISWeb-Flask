CREATE TABLE colleges (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	code VARCHAR(255) NOT NULL
);

CREATE TABLE courses (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	code VARCHAR(255) NOT NULL,
	college_id INT NOT NULL,
	CONSTRAINT fk_college_id FOREIGN KEY(college_id) REFERENCES colleges(id)
);

CREATE TABLE students (
	id INT PRIMARY KEY AUTO_INCREMENT,
	avatar_url VARCHAR (255),
	id_number VARCHAR(255) NOT NULL,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	course_id INT NOT NULL,
	year VARCHAR(255) NOT NULL,
	gender VARCHAR (255) NOT NULL,
	CONSTRAINT fk_course_id FOREIGN KEY(course_id) REFERENCES courses(id)
);