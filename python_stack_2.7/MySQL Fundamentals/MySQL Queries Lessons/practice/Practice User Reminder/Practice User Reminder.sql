-- INSERT INTO users (user_id, first_name, last_name, email_address, created_at, updated_at)
-- 	VALUES (3, "Insiya", "Hakim", "ihakim@codingdojo.com", NOW(), NOW());
    
-- SELECT * FROM users;

-- INSERT INTO  reminders (reminder_id, content, remind_on_date, created_at, updated_at, user_id)
-- 	VALUES(4, "Party Again", NOW(), NOW(), NOW(), 1);
    
-- SELECT * FROM reminders;

-- INSERT INTO users_reminders (user_reminder_id, created_at, updated_at, reminder_id, user_id)
-- 	VALUES (4, NOW(), NOW(), 3, 2);

-- SELECT * FROM users_reminders;

-- INSERT INTO friends (friend_id, created_at, updated_at, user_id, user_friend_id)
-- 	VALUES(5, NOW(), NOW(), 3, 2);

-- SELECT * FROM friends;

SELECT reminders.content, reminders.remind_on_date, users.first_name, users.last_name FROM reminders
	JOIN users ON users.user_id = reminders.user_id
    WHERE users.user_id = 1;

SELECT users.email_address, reminders.content FROM users
	JOIN users_reminders ON users.user_id = users_reminders.user_id
    JOIN reminders ON reminders.reminder_id = users_reminders.reminder_id
    WHERE reminders.reminder_id = 3;
    
SELECT users.first_name AS user_first, users.last_name AS user_last, users2.first_name AS user2_first, users2.last_name AS user2_last FROM users
	JOIN friends ON users.user_id = friends.user_id
    JOIN users AS users2 ON users2.user_id = friends.user_friend_id
    WHERE users.user_id = 1;

SELECT users.first_name AS user_first, users.last_name AS user_last, users2.first_name AS user2_first, users2.last_name AS user2_last FROM users
	LEFT JOIN friends ON users.user_id = friends.user_id
    LEFT JOIN users AS users2 ON users2.user_id = friends.user_friend_id
    WHERE users.user_id = 1;
	
SELECT users.first_name, users.last_name, reminders.content FROM users
	JOIN reminders ON reminders.user_id = users.user_id;
    

