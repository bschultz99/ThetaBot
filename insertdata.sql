-- SQLite
INSERT into takedowns VALUES
("GHQMZA22E", "Phu", "New Member",0,0,0,0,0,0,0,0,0,0,0,0),
("ILQMZA22E", "Khang", "New Member",0,0,0,0,0,0,0,0,0,0,0,0),
("DCQMZA22E", "Kaleb", "New Member",0,0,0,0,0,0,0,0,0,0,0,0),
("UJQMZA22E", "Khoi", "New Member",0,0,0,0,0,0,0,0,0,0,0,0);

INSERT INTO users VALUES
("UCQMZA22E", "Anthony A", "In-House 3"),
("UCQMZA63E", "Fran", "In-House 2"),
("UCQMZG64E", "Derek", "In-House 3"),
("UCQMAA62E", "Kevin", "In-House 3"),
("UCGMZB61E", "Huy C", "In-House 2"),
("UWEMZA24E", "Pedro", "In-House 2"),
("UWEMZA34E", "John", "In-House 2"),
("GFQMZA62E", "Charles", "In-House 2"),
("UCQBJH63E", "Dylan", "In-House 3"),
("UHMMZA63E", "Cameron", "In-House 3"),
("UAOPZA64E", "Ronald", "In-House 3"),
("UCEDZA62E", "Jovany", "In-House 3"),
("USSMZA63E", "Aleks", "In-House 2"),
("UWEMZA64E", "Marshall", "In-House 3"),
("UCHMZA63E", "Anthony N", "In-House 2"),
("UCQMZ253E", "Zawad", "In-House 3"),
("UCQMZA2FE", "Joel", "In-House 2"),
("UCQMZ8G4E", "Ronan", "In-House 2"),
("EWEMAA64E", "Remy", "In-House 2"),
("UCHDZA64E", "Arsh", "In-House 3"),
("UCE23A64E", "Thupten", "In-House 2"),
("UCQGZASDE", "Anudeep", "Townsman"),
("UCQQ4A64E", "Eddy", "Townsman"),
("UCQMOA6HB", "Sean", "Townsman"),
("UCQMZL34E", "David", "Townsman"),
("UCSDZQ64E", "Patrick", "Townsman"),
("UCSDZD34E", "Jeremiah", "Townsman"),
("UCDDZA64E", "Ricky", "Townsman"),
("UASDZA64E", "Skyler", "Townsman"),
("UFSDZA64E", "Huy N", "Townsman"),
("UCGDZA64E", "Heze", "Townsman"),
("UCSDZL64E", "Jason", "Townsman"),
("UCSDDA64E", "Bryant", "Townsman"),
("UCSEZA64E", "Roberto", "Townsman"),
("UCSDAA64E", "Zach", "Townsman");

INSERT INTO admin VALUES
("UCQMZA62E", "Bryant"),
("UCGDZA64E", "Heze"),
("UWEMZA34E", "John");

UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Anthony A';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Fran';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'Derek';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Kevin';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Huy C';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Pedro';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'John';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Charles';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'Dylan';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Cameron';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Ronald';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Jovany';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 1 WHERE name = 'Aleks';
UPDATE 'takedowns' SET 'takedown_count' = 5, 'monday_lunch' = 1, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Marshall';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Anthony N';
UPDATE 'takedowns' SET 'takedown_count' = 6, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 1 WHERE name = 'Zawad';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Joel';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Ronan';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Remy';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Arsh';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 1, 'friday_dinner' = 1 WHERE name = 'Thupten';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 1, 'friday_dinner' = 0 WHERE name = 'Anudeep';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Eddy';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Sean';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 1, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'David';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Patrick';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Jeremiah';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 1 WHERE name = 'Ricky';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 1, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Skyler';
UPDATE 'takedowns' SET 'takedown_count' = 4, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Huy N';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Heze';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Jason';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Bryant';
UPDATE 'takedowns' SET 'takedown_count' = 0, 'monday_lunch' = 0, 'monday_dinner' = 1, 'tuesday_lunch' = 0, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 1, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Roberto';
UPDATE 'takedowns' SET 'takedown_count' = 2, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 1, 'tuesday_dinner' = 0, 'wednesday_lunch' = 0, 'wednesday_dinner' = 0, 'thursday_lunch' = 1, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Zach';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Phu';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Khang';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Kaleb';
UPDATE 'takedowns' SET 'takedown_count' = 1, 'monday_lunch' = 0, 'monday_dinner' = 0, 'tuesday_lunch' = 0, 'tuesday_dinner' = 1, 'wednesday_lunch' = 1, 'wednesday_dinner' = 0, 'thursday_lunch' = 0, 'thursday_dinner' = 0, 'friday_lunch' = 0, 'friday_dinner' = 0 WHERE name = 'Khoi';