-- SQL DATABASE SETUP FOR SavePals;

CREATE DATABASE IF NOT EXISTS SavePals;
CREATE USER IF NOT EXISTS 'savepals_dev'@'localhost' IDENTIFIED BY 'savepals_dev_pwd';
GRANT ALL PRIVILEGES ON `SavePals`.* TO 'savepals_dev'@'localhost';
GRANT ALL SELECT ON `performance_schema`.* To 'savepals_dev'@'localhost';
FLUSH PRIVILEGES;
