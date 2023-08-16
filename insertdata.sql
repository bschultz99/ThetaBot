-- SQLite

INSERT INTO users VALUES
("U02DM23N38U", "Anthony A", "In-House 3"),
("UMKC86MJP", "Derek", "In-House 3"),
("U01LF8CQN9Z", "Kevin", "In-House 3"),
("U01LBV6LHHB", "Huy C", "In-House 2"),
("U02D83EUPEJ", "Pedro", "In-House 2"),
("U032HNL55PE", "John", "In-House 2"),
("U02DERE7CQJ", "Charles", "In-House 2"),
("U0427474LE4", "Dylan", "In-House 3"),
("U02DER8TQ67", "Ronald", "In-House 3"),
("U041KSDJA2G", "Marshall", "In-House 3"),
("U01M4T3JS9E", "Anthony N", "In-House 2"),
("UCVEQVA86", "Zawad", "In-House 3"),
("U02E4EBLW64", "Joel", "In-House 2"),
("U02DTE5UUM7", "Ronan", "In-House 2"),
("U0412RQCJVD", "Thupten", "In-House 2"),
("U041KSDDSJ0", "Patrick", "In-House 3"),
("U04KXQJTH6Z", "Kaleb", "In-House 3"),
("U04KXQJSMNZ", "Khoi", "In-House 2"),
("U04LDC58M5X", "Phu", "In-House 2"),
("U0412RQEV2T", "Anudeep", "Townsman"),
("U041W23PR8R", "Eddy", "Townsman"),
("U0427470248", "Jeremiah", "Townsman"),
("U041HD7845Q", "Ricky", "Townsman"),
("UMQE271CZ", "Skyler", "Townsman"),
("U032CG9DM9T", "Heze", "Townsman"),
("U04KL72F9U7", "Khang", "Townsman"),
("U02D045RXSB", "Jovany", "Townsman"),
("UT33FQB6H", "Zach", "Townsman");

UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'Anthony A';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Derek';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Kevin';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Huy C';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Pedro';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'John';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Charles';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Dylan';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Ronald';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Marshall';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Anthony N';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Zawad';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Joel';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 1 WHERE name = 'Ronan';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Thupten';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Patrick';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Kaleb';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Khoi';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'Phu';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Anudeep';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Eddy';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 1 WHERE name = 'Jeremiah';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Ricky';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Skyler';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Heze';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Khang';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Jovany';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'Zach';
