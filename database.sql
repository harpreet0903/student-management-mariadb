CREATE DATABASE IF NOT EXISTS college_db;

USE college_db;

CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    course VARCHAR(30) NOT NULL,
    marks INT NOT NULL,
    city VARCHAR(50) NOT NULL
);

INSERT INTO students (name, course, marks, city)
VALUES
('Aman', 'BCA', 85, 'Yamunanagar'),
('Neha', 'BCA', 92, 'Ambala'),
('Rohan', 'BCA', 76, 'Kurukshetra'),
('Simran', 'BCA', 88, 'Yamunanagar'),
('Karan', 'BCA', 81, 'Chandigarh');
