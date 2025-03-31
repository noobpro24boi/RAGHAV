
CREATE DATABASE railway_ticket_system;

USE railway_ticket_system;

CREATE TABLE tickets (
    pnr INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_no BIGINT(11) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    nationality VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    catering_service VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    train_no INT NOT NULL,
    arrival VARCHAR(255) NOT NULL,
    departure VARCHAR(255) NOT NULL,
    class VARCHAR(255) NOT NULL,
);

