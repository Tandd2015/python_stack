-- My SQL Functions

-- Text
-- CONCAT()
SELECT CONCAT('Mr.', ' ', first_name, ' ', last_name) FROM clients;
SELECT CONCAT('Mr.', ' ', first_name, ' ', last_name) AS full_name FROM clients;
-- CONCAT_WS()
SELECT CONCAT_WS(' ', first_name, last_name, 'cool something new') AS full_name FROM clients;
-- LENGTH()
SELECT LENGTH(last_name) AS last_len FROM clients;
-- LOWER()
SELECT LOWER(first_name) AS first_lowercase FROM clients;
SELECT first_name FROM clients;

-- DATE
-- HOUR()
SELECT HOUR(joined_datetime) AS date_hour, joined_datetime FROM clients;
-- DAYNAME()
SELECT DAYNAME(joined_datetime) AS day_name, joined_datetime FROM clients;
-- MONTH()
SELECT MONTH(joined_datetime) AS month_number, joined_datetime FROM clients;
-- NOW()
SELECT NOW() AS right_now;
-- DATE_FORMAT()
SELECT DATE_FORMAT(joined_datetime, '%W %M %e, %Y')FROM clients;

-- Text Functions
-- CONCAT()
-- CONCAT_WS()
-- LENGTH()
-- TRIM()
-- UPPER()
-- LOWER()
-- REPLACE()
-- SUBSTRING()

-- Date Functions
-- DATE()
-- HOUR()
-- MINUTE()
-- SECOND()
-- DAYNAME()
-- DAYOFMONTH()
-- MONTHNAME()
-- MONTH()
-- YEAR()
-- CURDATE()
-- CURTIME()
-- NOW()
-- TIME_FORMAT()
-- DATE_FORMAT()
 