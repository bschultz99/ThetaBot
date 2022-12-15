-- SQLite
SELECT slack_id, name, used, captainCount, Kitchen FROM cleanups WHERE captain = 1 AND used = 0 ORDER BY Kitchen ASC, captainCount ASC;

UPDATE cleanups SET used = 0;

DROP TABLE 'cleanups_2022-12-14';

DROP TABLE 'cleanups';

SELECT cleanup_id FROM cleanup_settings;

UPDATE cleanups SET "1 Deck" = "1 Deck" + 1 WHERE slack_id = "UCQMZA22E"

UPDATE cleanups SET used = used + 1 WHERE slack_id = 'UCQMZA22E'

PRAGMA table_info(cleanups)

SELECT * FROM cleanup_settings ORDER BY townsman_captain, deck_requirement;

SELECT name, membership, slack_id FROM cleanups 
    WHERE captain = 1 AND used = 0 AND membership = "In-House 3" OR membership = "In-House 2"
    ORDER BY Kitchen ASC, captainCount ASC;

UPDATE cleanups SET captain = 0 WHERE name = "Jason"

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