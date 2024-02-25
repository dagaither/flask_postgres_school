COPY students FROM '/Users/davidgaither/Projects/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;
COPY subjects FROM '/Users/davidgaither/Projects/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;
COPY teachers FROM '/Users/davidgaither/Projects/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;

-- Because we've inserted rows with hardcoded values for the primary key, id
-- the sequence used to generate id values for new rows is stuck at "1". So
-- we manually reset the sequences to the max value of id for each table.

SELECT setval('students_id_seq', (SELECT MAX(id) FROM students));
SELECT setval('subjects_id_seq', (SELECT MAX(id) FROM subjects));
SELECT setval('teachers_id_seq', (SELECT MAX(id) FROM teachers));
