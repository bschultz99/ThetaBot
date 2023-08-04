-- SQLite
SELECT slack_id, name, used, captainCount, Kitchen FROM cleanups WHERE captain = 1 AND used = 0 ORDER BY Kitchen ASC, captainCount ASC;

DROP TABLE 'cleanups_2022-12-1*';

DROP TABLE 'takedowns';

ALTER TABLE 'admin' ADD 'position';

SELECT SUM(monday_lunch), SUM(monday_dinner), SUM(tuesday_lunch), SUM(tuesday_dinner), SUM(wednesday_lunch), SUM(wednesday_dinner), SUM(thursday_lunch), SUM(thursday_dinner), SUM(friday_lunch), SUM(friday_dinner) FROM "takedowns";

UPDATE 'takedowns' SET slack_id= 'UCQMZA62E' WHERE name = 'Bryant';

DELETE FROM takedowns WHERE slack_id = "UCQMZA62E";

SELECT * FROM cleanup_settings ORDER BY townsman_captain, deck_requirement;

SELECT cleanup_id FROM cleanup_settings;


PRAGMA table_info(cleanups)

SELECT * FROM cleanup_settings ORDER BY townsman_captain, deck_requirement;

SELECT name, membership, slack_id FROM cleanups 
    WHERE captain = 1 AND used = 0 AND membership = "In-House 3" OR membership = "In-House 2"
    ORDER BY Kitchen ASC, captainCount ASC;


SELECT * FROM cleanups WHERE used = 0;

SELECT * FROM cleanups
                        WHERE used = 0 AND (membership = "In-House 2" OR membership = "In-House 3")
                        ORDER BY "Kitchen" ASC;

SELECT slack_id FROM cleanups
                        WHERE used = 0 AND membership = "In-House 2" OR membership = "In-House 3"
                        ORDER BY "Kitchen" ASC
SELECT Count() FROM cleanups WHERE used = 0;

SELECT cleanup_id FROM cleanup_settings WHERE deck_requirement = 0 AND townsman_captain = 0;

SELECT * FROM cleanups ORDER BY membership;

SELECT cleanup_id, deck_requirement FROM cleanup_settings WHERE townsman_captain = 0

SELECT slack_id FROM cleanups 
                                WHERE used = 0 AND membership = "New Member"
                                ORDER BY "Study/Laundry" ASC
                                ;

SELECT cleanup_id, deck_requirement FROM cleanup_settings WHERE townsman_captain = 0 ORDER BY deck_requirement DESC;

SELECT name, captain, cleanup FROM "cleanups_2022-12-16" ORDER BY cleanup, captain DESC;

select name FROM users;

SELECT * FROM "takedowns_2023-01-12" ORDER BY assignment ASC;

UPDATE takedowns SET takedown_count = 0;
UPDATE takedowns SET used = 0;
UPDATE "takedowns_2023-01-15" SET assignment = "NULL";

SELECT * FROM "takedowns" WHERE used = 0;

SELECT * from admin WHERE slack_id = 'UCQMZA63E'

UPDATE cleanups SET captain = 0 WHERE name = 'Fran'

UPDATE admin SET slack_id = "UCQMZA62E" WHERE name = 'Bryant';

SELECT * FROM "takedowns_2023-01-14" WHERE assignment != "Break";
UPDATE "takedowns" SET takedown_count = takedown_count - 1 WHERE slack_id = "UCQMZA22E";

SELECT name, membership, takedown_count, monday_lunch, monday_dinner, tuesday_lunch, tuesday_dinner, wednesday_lunch, wednesday_dinner, thursday_lunch, thursday_dinner, friday_lunch, friday_dinner FROM takedowns;

UPDATE "admin" SET position = "Owner" WHERE name = "Bryant";

DELETE FROM admin WHERE slack_id = 'UWEMZA34E';

UPDATE cleanups SET captainCount = captainCount + 1 WHERE name = 'Sean';
UPDATE cleanups SET '1 Deck' = '1 Deck' + 1 WHERE name = 'Zach';

UPDATE takedowns SET wednesday_lunch = 0 WHERE name = 'Zach';

UPDATE cleanup_settings set minimum_people = 2 WHERE cleanup_id = "Deckbrush 1+3";

UPDATE cleanups SET captain = 0 WHERE name = "Remy";

UPDATE cleanups SET 'Kitchen' = 2 WHERE name = 'Khoi';
UPDATE cleanups SET captainCount = captainCount + 1 WHERE name = 'Bryant';

UPDATE takedowns SET takedown_count = takedown_count - 1 WHERE name = 'Zach';

SELECT * FROM cleanup_settings ORDER BY townsman_captain, deck_requirement;

SELECT cleanup_id, deck_requirement FROM cleanup_settings WHERE townsman_captain = 0 ORDER BY deck_requirement DESC;

SELECT name FROM sqlite_master WHERE type = 'table' AND name LIKE '%cleanups_2022%';

INSERT INTO fines(slack_id, reason, date, amount, type, issuer) VALUES('abc', 'bad', '7-16-23', 10, 'cleanups', 'Joe p');


SELECT Count() from fines WHERE slack_id = 'abc' and type = 'cleanups';
DROP TABLE fines;

SELECT name from users WHERE slack_id = '{}';

DROP TABLE reconcilliation;

SELECT u.name, r.notes, r.date, r.amount, r.type, x.name as issuer FROM reconcilliation r JOIN users u on u.slack_id = r.slack_id JOIN users x on x.slack_id = r.issuer ORDER BY u.name;

SELECT u.name, f.reason, f.date, f.amount, f.type, x.name as issuer FROM fines f JOIN users u on u.slack_id = f.slack_id JOIN users x on x.slack_id = f.issuer ORDER BY u.name;


SELECT x.name, SUM(r.amount) as reconcilliation FROM reconcilliation r JOIN users x on x.slack_id = r.slack_id GROUP BY x.name;

SELECT u.name, SUM(f.amount) as fines FROM fines f JOIN users u on u.slack_id = f.slack_id GROUP BY u.name ;

SELECT u.name, SUM(f.amount) as fines FROM fines f JOIN users u on u.slack_id = f.slack_id GROUP BY u.name ;

DROP TABLE reconcilliation;

UPDATE naughty SET reconcilliation = 10 WHERE slack_id = 'UAOPZA64E';

UPDATE users SET slack_id = 'UMQE271CZ' WHERE name = 'Skyler';

SELECT name, fines, reconcilliation, owed from naughty ORDER BY owed DESC;