CREATE DATABASE IF NOT EXISTS user_registration;

USE user_registration;

CREATE TABLE IF NOT EXISTS users (
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT,
    gender ENUM('Male', 'Female', 'Other'),
    ethnicity VARCHAR(50),
    UNIQUE KEY unique_user (first_name, last_name)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;