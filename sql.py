# pylint: disable=line-too-long
"""SQL constants used by the database"""
#Startup Table Generation
USERS_STARTUP_TABLE = '''
                        CREATE TABLE IF NOT EXISTS users (
                            slack_id text PRIMARY KEY NOT NULL,
                            name text NOT NULL,
                            membership text NOT NULL
                        );
                      '''
CLEANUPSETTINGS_STARTUP_TABLE = '''
                                  CREATE TABLE IF NOT EXISTS cleanup_settings (
                                    cleanup_id text PRIMARY KEY NOT NULL,
                                    deck_requirement integer NOT NULL,
                                    townsman_captain boolean NOT NULL,
                                    minimum_inhouse integer NOT NULL,
                                    minimum_people integer NOT NULL
                                  );
                                '''
CLEANUPS_STARTUP_TABLE = 'CREATE TABLE IF NOT EXISTS cleanups AS SELECT * FROM users;'
CLEANUPS_STARTUP_ALTER = '''
                           BEGIN;
                           ALTER TABLE cleanups ADD COLUMN used boolean DEFAULT FALSE;
                           ALTER TABLE cleanups ADD COLUMN captain boolean DEFAULT TRUE;
                           ALTER TABLE cleanups ADD COLUMN captainCount integer DEFAULT 0;
                           UPDATE cleanups SET captain = FALSE WHERE membership = "New Member";
                           COMMIT;
                         '''
TAKEDOWNS_STARTUP_TABLE = 'CREATE TABLE IF NOT EXISTS takedowns AS SELECT * FROM users;'
TAKEDOWNS_STARTUP_ALTER = '''
                            BEGIN;
                            ALTER TABLE takedowns ADD COLUMN used boolean DEFAULT FALSE;
                            ALTER TABLE takedowns ADD COLUMN takedown_count integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN monday_lunch integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN monday_dinner integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN tuesday_lunch integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN tuesday_dinner integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN wednesday_lunch integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN wednesday_dinner integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN thursday_lunch integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN thursday_dinner integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN friday_lunch integer DEFAULT 0;
                            ALTER TABLE takedowns ADD COLUMN friday_dinner integer DEFAULT 0;
                            COMMIT;
                          '''
ADMIN_STARTUP_TABLE = '''
                        CREATE TABLE IF NOT EXISTS admin (
                            slack_id text PRIMARY KEY NOT NULL,
                            position text NOT NULL
                        );
                      '''
FINES_STARTUP_TABLE = '''
                        CREATE TABLE IF NOT EXISTS fines (
                            id integer PRIMARY KEY NOT NULL,
                            slack_id text NOT NULL,
                            reason text NOT NULL,
                            date text NOT NULL,
                            amount integer NOT NULL,
                            type text NOT NULL,
                            issuer text NOT NULL
                        );
                      '''
RECONCILLIATION_STARTUP_TABLE = '''
                                  CREATE TABLE IF NOT EXISTS reconcilliation (
                                      id integer PRIMARY KEY NOT NULL,
                                      slack_id text NOT NULL,
                                      notes text,
                                      type text NOT NULL,
                                      date text NOT NULL,
                                      amount integer NOT NULL,
                                      issuer text NOT NULL
                                  );
                                '''
NAUGHTY_STARTUP_TABLE = 'CREATE TABLE IF NOT EXISTS naughty AS SELECT slack_id, name FROM users;'
NAUGHTY_STARTUP_ALTER = '''
                            BEGIN;
                            ALTER TABLE naughty ADD COLUMN fines integer DEFAULT 0;
                            ALTER TABLE naughty ADD COLUMN reconcilliation integer DEFAULT 0;
                            ALTER TABLE naughty ADD COLUMN owed integer GENERATED ALWAYS AS (fines-reconcilliation);
                            COMMIT;
                          '''
#User
USERS_ADD_SELECT = 'SELECT slack_id FROM users WHERE slack_id = "{}";'
USERS_ADD_INSERT = 'INSERT INTO users(slack_id, name, membership) VALUES(?,?,?);'
USERS_ADD_UPDATE = 'UPDATE users SET name = "{}", membership = "{}" WHERE slack_id = "{}";'
USERS_DATABASE_SELECT = 'SELECT slack_id FROM cleanups WHERE slack_id = "{}";'
USERS_DATABASE_INSERT = 'INSERT INTO cleanups(slack_id, name, membership) VALUES (?,?,?);'
USERS_DATABASE_UPDATE = 'UPDATE cleanups SET name = "{}", membership = "{}" WHERE slack_id = "{}";'
USERS_DATABASE_UPDATECAPTAIN = '''
                                 BEGIN;
                                 UPDATE cleanups SET captain = FALSE WHERE membership = "New Member" AND slack_id = "{}";
                                 UPDATE cleanups SET captain = TRUE WHERE membership != "New Member" AND slack_id = "{}";
                                 COMMIT;
                               '''
USERS_DATABASE_SELECT_TAKEDOWN = 'SELECT slack_id FROM takedowns WHERE slack_id = "{}";'
USERS_DATABASE_UPDATE_TAKEDOWN = '''UPDATE takedowns SET
                                    monday_lunch = "{}", monday_dinner = "{}",
                                    tuesday_lunch = "{}", tuesday_dinner = "{}",
                                    wednesday_lunch = "{}", wednesday_dinner = "{}",
                                    thursday_lunch = "{}", thursday_dinner = "{}",
                                    friday_lunch = "{}", friday_dinner = "{}",
                                    membership = "{}" WHERE slack_id = "{}";'''
USERS_DATABASE_INSERT_TAKEDOWN = '''INSERT INTO takedowns(monday_lunch, monday_dinner, tuesday_lunch, tuesday_dinner, wednesday_lunch, wednesday_dinner, thursday_lunch, thursday_dinner, friday_lunch, friday_dinner, membership, slack_id) VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'''
USERS_REMOVE_DELETE = '''
                        BEGIN;
                        DELETE FROM users WHERE slack_id = "{}";
                        DELETE FROM cleanups WHERE slack_id = "{}";
                        COMMIT;
                      '''
USERS_DATABASE_SELECT_NAUGHTY = 'SELECT slack_id FROM naughty WHERE slack_id = "{}";'
USERS_DATABASE_UPDATE_NAUGHTY = 'UPDATE naughty SET name = "{}" WHERE slack_id = "{}";'
USERS_DATABASE_INSERT_NAUGHTY = ' INSERT INTO naughty(slack_id, name, fines, reconcilliation, owed) VALUES ("{}","{}",0,0,0);'
#Cleanup Settings
CLEANUPSETTINGS_ADD_SELECT = 'SELECT * FROM cleanup_settings WHERE cleanup_id = "{}";'
CLEANUPSETTINGS_ADD_INSERT = 'INSERT INTO cleanup_settings(cleanup_id, deck_requirement, townsman_captain, minimum_inhouse, minimum_people) VALUES(?,?,?,?,?);'
CLEANUPSETTINGS_ADD_UPDATE = 'UPDATE cleanup_settings SET deck_requirement = "{}", townsman_captain = "{}", minimum_inhouse = "{}", minimum_people = "{}" WHERE cleanup_id = "{}";'
CLEANUPSETTINGS_REMOVE_DELETE = 'DELETE FROM cleanup_settings WHERE cleanup_ID = "{}";'
#Generate Cleanups Database
CLEANUPS_DATABASE_SELECT = 'SELECT cleanup_id from cleanup_settings;'
CLEANUPS_DATABASE_ALTERCLEANUPS = 'ALTER TABLE cleanups ADD COLUMN "{}" integer DEFAULT 0;'
#Generate Cleanups
CLEANUPS_GENERATE_TABLE = 'CREATE TABLE IF NOT EXISTS "cleanups_{}" AS SELECT slack_id, name FROM users;'
CLEANUPS_GENERATE_ALTER = '''
                            BEGIN;
                            ALTER TABLE "cleanups_{}" ADD COLUMN captain DEFAULT 0;
                            ALTER TABLE "cleanups_{}" ADD COLUMN cleanup DEFAULT NULL;
                            COMMIT;
                          '''
CLEANUPS_GENERATE_SELECT = 'SELECT * FROM cleanup_settings ORDER BY townsman_captain, deck_requirement;'
CLEANUPS_GENERATE_CAPTAINUPDATE = '''
                             BEGIN;
                             UPDATE cleanups SET captainCount = captainCount + 1 WHERE slack_id = "{}";
                             UPDATE cleanups SET "{}" = "{}" + 1 WHERE slack_id = "{}";
                             UPDATE cleanups SET used = 1 WHERE slack_ID = "{}";
                             UPDATE "cleanups_{}" SET captain = 1 WHERE slack_ID = "{}";
                             UPDATE "cleanups_{}" SET cleanup = "{}" WHERE slack_id = "{}";
                             COMMIT;
                           '''
CLEANUPS_GENERATE_SELECTCAPTAININHOUSE = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND (membership = "In-House 3" OR membership = "In-House 2") ORDER BY "{}" ASC, captainCount ASC;'
CLEANUPS_GENERATE_SELECTCAPTAININHOUSE2 = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND membership = "In-House 2" ORDER BY "{}" ASC, captainCount ASC;'
CLEANUPS_GENERATE_SELECTCAPTAININHOUSE3 = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND membership = "In-House 3" ORDER BY "{}" ASC, captainCount ASC;'
CLEANUPS_GENERATE_SELECTCAPTAINALL = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 ORDER BY "{}" ASC, captainCount ASC;'
CLEANUPS_GENERATE_SELECTCAPTAININHOUSE2TOWNSMAN = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND (membership = "In-House 2" OR membership = "Townsman") ORDER BY "{}" ASC, captainCount ASC;'
CLEANUPS_GENERATE_SELECTCAPTAININHOUSE3TOWNSMAN = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND (membership = "In-House 3" OR membership = "Townsman") ORDER BY "{}" ASC, captainCount ASC;'
CLEANUPS_GENERATE_SELECTMININHOUSE = 'SELECT slack_id FROM cleanups WHERE used = 0 AND (membership = "In-House 2" OR membership = "In-House 3") ORDER BY "{}" ASC;'
CLEANUPS_GENERATE_SELECTMININHOUSE2 = 'SELECT slack_id FROM cleanups WHERE used = 0 AND membership = "In-House 2" ORDER BY "{}" ASC;'
CLEANUPS_GENERATE_SELECTMININHOUSE3 = 'SELECT slack_id FROM cleanups WHERE used = 0 AND membership = "In-House 3" ORDER BY "{}" ASC;'
CLEANUPS_GENERATE_UPDATE = '''
                                BEGIN;
                                UPDATE cleanups SET "{}" = "{}" + 1 WHERE slack_id = "{}";
                                UPDATE cleanups SET used = 1 WHERE slack_id = "{}";
                                UPDATE "cleanups_{}" SET cleanup = "{}" WHERE slack_id = "{}";
                                COMMIT;
                              '''
CLEANUPS_GENERATE_SELECTALL = 'SELECT slack_id FROM cleanups WHERE used = 0 ORDER BY "{}" ASC;'
CLEANUPS_GENERATE_SELECTPEOPLE2 = 'SELECT slack_id FROM cleanups WHERE used = 0 AND (membership = "In-House 2" OR membership = "Townsman" OR membership = "New Member") ORDER BY "{}" ASC;'
CLEANUPS_GENERATE_SELECTPEOPLE3 = 'SELECT slack_id FROM cleanups WHERE used = 0 AND (membership = "In-House 3" OR membership = "Townsman" OR membership = "New Member") ORDER BY "{}" ASC;'
CLEANUPS_GENERATE_SELECTCOUNT = 'SELECT count() FROM cleanups WHERE used = 0;'
CLEANUPS_GENERATE_SELECTCLEANUP = 'SELECT cleanup_id, deck_requirement FROM cleanup_settings WHERE townsman_captain = 0 ORDER BY deck_requirement DESC;'
CLEANUPS_GENERATE_UPDATEUSED = 'UPDATE cleanups SET used = 0'
CLEANUPS_GENERATE_SELECTOUTPUT = 'SELECT name, captain, cleanup FROM "cleanups_{}" ORDER BY cleanup, captain DESC;'
#Generate Takedowns
TAKEDOWNS_GENERATE_TABLE = 'CREATE TABLE IF NOT EXISTS "takedowns_{}" AS SELECT slack_id, name FROM users;'
TAKEDOWNS_GENERATE_ALTER = '''
                            BEGIN;
                            ALTER TABLE "takedowns_{}" ADD COLUMN assignment DEFAULT NULL;
                            COMMIT;
                          '''
TAKEDOWNS_GENERATE_SUM = 'SELECT SUM(monday_lunch), SUM(monday_dinner), SUM(tuesday_lunch), SUM(tuesday_dinner), SUM(wednesday_lunch), SUM(wednesday_dinner), SUM(thursday_lunch), SUM(thursday_dinner), SUM(friday_lunch), SUM(friday_dinner) FROM "takedowns";'
TAKEDOWNS_GENERATE_MINIMUM = 'SELECT * FROM "takedowns" WHERE {} = 1 AND ("membership" = "In-House 2" OR "membership" = "In-House 3" OR "membership" = "Townsman") AND used = 0 ORDER BY "takedown_count";'
TAKEDOWNS_GENERATE_UPDATE = '''
                                    BEGIN;
                                    UPDATE takedowns SET takedown_count = takedown_count + 1 WHERE slack_id = "{}";
                                    UPDATE takedowns SET used = 1 WHERE slack_id = "{}";
                                    UPDATE "takedowns_{}" SET assignment = "{}" WHERE slack_id = "{}";
                                    COMMIT;
                                  '''
TAKEDOWNS_GENERATE_FILL = 'SELECT * FROM "takedowns" WHERE {} = 1 AND used = 0 ORDER BY "takedown_count";'
TAKEDOWNS_GENERATE_REMAINING = 'SELECT slack_id FROM "takedowns" WHERE used = 0;'
TAKEDOWNS_GENERATE_BREAK = 'UPDATE "takedowns_{}" SET assignment = "Break" WHERE slack_id = "{}";'
TAKEDOWNS_GENERATE_UPDATEUSED = 'UPDATE takedowns SET used = 0;'
TAKEDOWNS_GENERATE_ERROR = '''
                             BEGIN;
                             UPDATE takedowns SET takedown_count = takedown_count - 1 WHERE used = 1;
                             UPDATE takedowns SET used = 0;
                             UPDATE "takedowns_{}" SET assignment = NULL;
                             COMMIT;
                          '''
TAKEDOWNS_GENERATE_SELECTOUTPUT = 'SELECT name, assignment FROM "takedowns_{}" ORDER BY assignment ASC;'
TAKEDOWNS_REVERT_SELECT = 'SELECT slack_id FROM "takedowns_{}" WHERE assignment != "Break";'
TAKEDOWNS_REVERT_UPDATE = 'UPDATE "takedowns" SET takedown_count = takedown_count - 1 WHERE slack_id = "{}";'
TAKEDOWNS_REVERT_WEEK = 'UPDATE "takedowns_{}" SET assignment = "NULL";'
# Admin
ADMIN_SELECT = 'SELECT * FROM admin where slack_id = "{}";'
ADMIN_ADD_SELECT = 'SELECT slack_id FROM admin WHERE slack_id = "{}";'
ADMIN_ADD_INSERT = 'INSERT INTO admin(slack_id, position) VALUES(?,?);'
ADMIN_ADD_UPDATE = 'UPDATE admin SET position = "{}" WHERE slack_id = "{}";'
# Takedowns Display
TAKEDOWNS_DISPLAY_SELECT = 'SELECT name, membership, takedown_count, monday_lunch, monday_dinner, tuesday_lunch, tuesday_dinner, wednesday_lunch, wednesday_dinner, thursday_lunch, thursday_dinner, friday_lunch, friday_dinner FROM takedowns;'
# Cleanups Display
CLEANUPS_DISPLAY_SELECT = 'SELECT * FROM cleanups;'
# Fine and Reconcilliation
FINES_DATABASE_INSERT = 'INSERT INTO fines(slack_id, reason, date, amount, type, issuer) VALUES (?,?,?, ?, ?, ?);'
FINES_CLEANUPS_SUM = 'SELECT Count() from fines WHERE slack_id = "{}" and type = "Cleanups";'
ISSUER_SELECT = 'SELECT name from users WHERE slack_id = "{}";'
RECONCILLIATION_DATABASE_INSERT = 'INSERT INTO reconcilliation(slack_id, notes, type, date, amount, issuer) VALUES (?,?,?,?,?,?);'
FINES_NAUGHTY_UPDATE = 'UPDATE naughty SET fines = fines + "{}" WHERE slack_id = "{}";'
RECONCILLIATION_NAUGHTY_UPDATE = 'UPDATE naughty SET reconcilliation = reconcilliation + "{}" WHERE slack_id = "{}";'
# Fines and Reconcilliation Display
FINES_DISPLAY_SELECT = 'SELECT u.name, f.reason, f.date, f.amount, f.type, x.name as issuer FROM fines f JOIN users u on u.slack_id = f.slack_id JOIN users x on x.slack_id = f.issuer ORDER BY u.name;'
RECONCILLIATIONS_DISPLAY_SELECT = 'SELECT u.name, r.notes, r.date, r.amount, r.type, x.name as issuer FROM reconcilliation r JOIN users u on u.slack_id = r.slack_id JOIN users x on x.slack_id = r.issuer ORDER BY u.name;'
# Naughty Boy
NAUGHTY_DISPLAY_SELECT = 'SELECT name, fines, reconcilliation, owed from naughty ORDER BY owed DESC;'
