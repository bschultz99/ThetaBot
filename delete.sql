-- SQLite
SELECT slack_id, name, used, captainCount, Kitchen FROM cleanups WHERE captain = 1 AND used = 0 ORDER BY Kitchen ASC, captainCount ASC;

DROP TABLE 'cleanups_2023-01-07';

DROP TABLE 'takedowns';

ALTER TABLE 'takedowns' DROP 'break_count';

SELECT SUM(monday_lunch), SUM(monday_dinner), SUM(tuesday_lunch), SUM(tuesday_dinner), SUM(wednesday_lunch), SUM(wednesday_dinner), SUM(thursday_lunch), SUM(thursday_dinner), SUM(friday_lunch), SUM(friday_dinner) FROM "takedowns";

UPDATE 'cleanup_settings' SET minimum_inhouse = 1 WHERE cleanup_id = '1 Deck';

DELETE FROM cleanups WHERE name = "Andrew";

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