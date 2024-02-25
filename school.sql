-- Schema
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   varchar(20) NOT NULL,
  last_name    varchar(20) NOT NULL,
  age          integer NOT NULL,
  subject      integer NOT NULL
);

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id serial PRIMARY KEY,
  subject varchar(30) NOT NULL
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id           serial PRIMARY KEY,
  first_name   varchar(20) NOT NULL,
  last_name    varchar(20) NOT NULL,
  age          integer NOT NULL,
  subject      integer NOT NULL
);