-- SQLite
INSERT into takedowns VALUES
("GHQMZA22E", "Phu", "New Member",0,0,0,0,0,0,0,0,0,0,0,0),
("ILQMZA22E", "Khang", "New Member",0,0,0,0,0,0,0,0,0,0,0,0),
("DCQMZA22E", "Kaleb", "New Member",0,0,0,0,0,0,0,0,0,0,0,0),
("UJQMZA22E", "Khoi", "New Member",0,0,0,0,0,0,0,0,0,0,0,0);

INSERT INTO users VALUES
("UCQMZA22E", "Anthony A", "In-House 3"),
("UCQMZG64E", "Derek", "In-House 3"),
("UCQMAA62E", "Kevin", "In-House 3"),
("UCGMZB61E", "Huy C", "In-House 2"),
("UWEMZA24E", "Pedro", "In-House 2"),
("UWEMZA34E", "John", "In-House 2"),
("GFQMZA62E", "Charles", "In-House 2"),
("UCQBJH63E", "Dylan", "In-House 3"),
("UAOPZA64E", "Ronald", "In-House 3"),
("UWEMZA64E", "Marshall", "In-House 3"),
("UCHMZA63E", "Anthony N", "In-House 2"),
("UCQMZ253E", "Zawad", "In-House 3"),
("UCQMZA2FE", "Joel", "In-House 2"),
("UCQMZ8G4E", "Ronan", "In-House 2"),
("UCE23A64E", "Thupten", "In-House 2"),
("UCSDZQ64E", "Patrick", "In-House 3"),
("UCSDZQ64E", "Kaleb", "In-House 3"),
("UCSDZQ64E", "Khoi, "In-House 2"),
("UCSDZQ64E", "Phu", "In-House 2"),
("UCSDZD34E", "Anudeep", "Townsman"),
("UCSDZD34E", "Eddy", "Townsman"),
("UCSDZD34E", "Jeremiah", "Townsman"),
("UCDDZA64E", "Ricky", "Townsman"),
("UASDZA64E", "Skyler", "Townsman"),
("UCGDZA64E", "Heze", "Townsman"),
("UCSDZL64E", "Jason", "Townsman"),
("UCSDDA64E", "Khang", "Townsman"),
("UCSEZA64E", "Jovany", "Townsman"),
("UCSDAA64E", "Zach", "Townsman");

UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'Anthony A';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Fran';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Derek';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Kevin';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Huy C';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Pedro';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'John';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Charles';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Dylan';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Cameron';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Ronald';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Jovany';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Aleks';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 1 WHERE name = 'Marshall';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Anthony N';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Zawad';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Joel';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Ronan';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'Remy';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Arsh';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Thupten';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 1 WHERE name = 'Anudeep';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Eddy';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Sean';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'David';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Patrick';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Jeremiah';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 1 WHERE name = 'Ricky';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Skyler';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Huy N';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Heze';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Jason';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Bryant';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 1 WHERE name = 'Zach';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'Phu';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Khang';
UPDATE 'takedowns' SET 'takedown_count' = 12, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Kaleb';
UPDATE 'takedowns' SET 'takedown_count' = 11, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Khoi';