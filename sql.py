#Startup Table Generation
users_startup_table = '''
                        CREATE TABLE IF NOT EXISTS users (
                            slack_id text PRIMARY KEY NOT NULL,
                            name text NOT NULL,
                            membership text NOT NULL
                        );
                      '''
cleanupSettings_startup_table = '''
                                  CREATE TABLE IF NOT EXISTS cleanup_settings (
                                    cleanup_id text PRIMARY KEY NOT NULL,
                                    deck_requirement integer NOT NULL,
                                    townsman_captain boolean NOT NULL,
                                    minimum_inhouse integer NOT NULL,
                                    minimum_people integer NOT NULL
                                  );
                                '''
cleanups_startup_table = 'CREATE TABLE IF NOT EXISTS cleanups AS SELECT * FROM users;'
cleanups_startup_alter = '''
                           BEGIN;
                           ALTER TABLE cleanups ADD COLUMN used boolean DEFAULT FALSE;
                           ALTER TABLE cleanups ADD COLUMN captain boolean DEFAULT TRUE;
                           ALTER TABLE cleanups ADD COLUMN captainCount integer DEFAULT 0;
                           UPDATE cleanups SET captain = FALSE WHERE membership = "New Member";
                           COMMIT;
                         '''
takedowns_startup_table = 'CREATE TABLE IF NOT EXISTS takedowns AS SELECT * FROM users;'
takedowns_startup_alter = '''
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
admin_startup_table = '''
                        CREATE TABLE IF NOT EXISTS admin (
                            slack_id text PRIMARY KEY NOT NULL,
                            position text NOT NULL
                        );
                      '''
#User
users_add_select = 'SELECT slack_id FROM users WHERE slack_id = "{}";'
users_add_insert = 'INSERT INTO users(slack_id, name, membership) VALUES(?,?,?);'
users_add_update = 'UPDATE users SET name = "{}", membership = "{}" WHERE slack_id = "{}";'
users_database_select = 'SELECT slack_id FROM cleanups WHERE slack_id = "{}";'
users_database_insert = 'INSERT INTO cleanups(slack_id, name, membership) VALUES (?,?,?);'
users_database_update = 'UPDATE cleanups SET name = "{}", membership = "{}" WHERE slack_id = "{}";'
users_database_updateCaptain = '''
                                 BEGIN;
                                 UPDATE cleanups SET captain = FALSE WHERE membership = "New Member" AND slack_id = "{}";
                                 UPDATE cleanups SET captain = TRUE WHERE membership != "New Member" AND slack_id = "{}";
                                 COMMIT;
                               '''
users_database_select_takedown = 'SELECT slack_id FROM takedowns WHERE slack_id = "{}";'
users_database_update_takedown = 'UPDATE takedowns SET monday_lunch = "{}", monday_dinner = "{}", tuesday_lunch = "{}", tuesday_dinner = "{}", wednesday_lunch = "{}", wednesday_dinner = "{}", thursday_lunch = "{}", thursday_dinner = "{}", friday_lunch = "{}", friday_dinner = "{}", membership = "{}" WHERE slack_id = "{}";'
users_database_insert_takedown = 'INSERT INTO takedowns(monday_lunch, monday_dinner, tuesday_lunch, tuesday_dinner, wednesday_lunch, wednesday_dinner, thursday_lunch, thursday_dinner, friday_lunch, friday_dinner, membership, slack_id) VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'
users_remove_delete = '''
                        BEGIN;
                        DELETE FROM users WHERE slack_id = "{}";
                        DELETE FROM cleanups WHERE slack_id = "{}";
                        COMMIT;
                      '''
#Cleanup Settings
cleanupSettings_add_select = 'SELECT * FROM cleanup_settings WHERE cleanup_id = "{}";'
cleanupSettings_add_insert = 'INSERT INTO cleanup_settings(cleanup_id, deck_requirement, townsman_captain, minimum_inhouse, minimum_people) VALUES(?,?,?,?,?);'
cleanupSettings_add_update = 'UPDATE cleanup_settings SET deck_requirement = "{}", townsman_captain = "{}", minimum_inhouse = "{}", minimum_people = "{}" WHERE cleanup_id = "{}";'
cleanupSettings_remove_delete = 'DELETE FROM cleanup_settings WHERE cleanup_ID = "{}";'
#Generate Cleanups Database
cleanups_database_select = 'SELECT cleanup_id from cleanup_settings;'
cleanups_database_alterCleanups = 'ALTER TABLE cleanups ADD COLUMN "{}" integer DEFAULT 0;'
#Generate Cleanups
cleanups_generate_table = 'CREATE TABLE IF NOT EXISTS "cleanups_{}" AS SELECT slack_id, name FROM users;'
cleanups_generate_alter = '''
                            BEGIN;
                            ALTER TABLE "cleanups_{}" ADD COLUMN captain DEFAULT 0;
                            ALTER TABLE "cleanups_{}" ADD COLUMN cleanup DEFAULT NULL;
                            COMMIT;
                          '''
cleanups_generate_select = 'SELECT * FROM cleanup_settings ORDER BY townsman_captain, deck_requirement;'
cleanups_generate_captainUpdate = '''
                             BEGIN;
                             UPDATE cleanups SET captainCount = captainCount + 1 WHERE slack_id = "{}";
                             UPDATE cleanups SET "{}" = "{}" + 1 WHERE slack_id = "{}";
                             UPDATE cleanups SET used = 1 WHERE slack_ID = "{}";
                             UPDATE "cleanups_{}" SET captain = 1 WHERE slack_ID = "{}";
                             UPDATE "cleanups_{}" SET cleanup = "{}" WHERE slack_id = "{}";
                             COMMIT;
                           '''
cleanups_generate_selectCaptainInHouse = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND (membership = "In-House 3" OR membership = "In-House 2") ORDER BY "{}" ASC, captainCount ASC;'
cleanups_generate_selectCaptainInHouse2 = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND membership = "In-House 2" ORDER BY "{}" ASC, captainCount ASC;'
cleanups_generate_selectCaptainInHouse3 = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND membership = "In-House 3" ORDER BY "{}" ASC, captainCount ASC;'
cleanups_generate_selectCaptainAll = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 ORDER BY "{}" ASC, captainCount ASC;'
cleanups_generate_selectCaptainInHouse2Townsman = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND (membership = "In-House 2" OR membership = "Townsman") ORDER BY "{}" ASC, captainCount ASC;'
cleanups_generate_selectCaptainInHouse3Townsman = 'SELECT slack_id FROM cleanups WHERE captain = 1 AND used = 0 AND (membership = "In-House 3" OR membership = "Townsman") ORDER BY "{}" ASC, captainCount ASC;'
cleanups_generate_selectMinInHouse = 'SELECT slack_id FROM cleanups WHERE used = 0 AND (membership = "In-House 2" OR membership = "In-House 3") ORDER BY "{}" ASC;'
cleanups_generate_selectMinInHouse2 = 'SELECT slack_id FROM cleanups WHERE used = 0 AND membership = "In-House 2" ORDER BY "{}" ASC;'
cleanups_generate_selectMinInHouse3 = 'SELECT slack_id FROM cleanups WHERE used = 0 AND membership = "In-House 3" ORDER BY "{}" ASC;'
cleanups_generate_update = '''
                                BEGIN;
                                UPDATE cleanups SET "{}" = "{}" + 1 WHERE slack_id = "{}";
                                UPDATE cleanups SET used = 1 WHERE slack_id = "{}";
                                UPDATE "cleanups_{}" SET cleanup = "{}" WHERE slack_id = "{}";
                                COMMIT;
                              '''
cleanups_generate_selectAll = 'SELECT slack_id FROM cleanups WHERE used = 0 ORDER BY "{}" ASC;'
cleanups_generate_selectPeople2 = 'SELECT slack_id FROM cleanups WHERE used = 0 AND (membership = "In-House 2" OR membership = "Townsman" OR membership = "New Member") ORDER BY "{}" ASC;'
cleanups_generate_selectPeople3 = 'SELECT slack_id FROM cleanups WHERE used = 0 AND (membership = "In-House 3" OR membership = "Townsman" OR membership = "New Member") ORDER BY "{}" ASC;'
cleanups_generate_selectCount = 'SELECT count() FROM cleanups WHERE used = 0;'
cleanups_generate_selectCleanup = 'SELECT cleanup_id, deck_requirement FROM cleanup_settings WHERE townsman_captain = 0 ORDER BY deck_requirement DESC;'
cleanups_generate_updateUsed = 'UPDATE cleanups SET used = 0'
cleanups_generate_selectOutput = 'SELECT name, captain, cleanup FROM "cleanups_{}" ORDER BY cleanup, captain DESC;'
#Generate Takedowns
takedowns_generate_table = 'CREATE TABLE IF NOT EXISTS "takedowns_{}" AS SELECT slack_id, name FROM users;'
takedowns_generate_alter = '''
                            BEGIN;
                            ALTER TABLE "takedowns_{}" ADD COLUMN assignment DEFAULT NULL;
                            COMMIT;
                          '''
takedowns_generate_sum = 'SELECT SUM(monday_lunch), SUM(monday_dinner), SUM(tuesday_lunch), SUM(tuesday_dinner), SUM(wednesday_lunch), SUM(wednesday_dinner), SUM(thursday_lunch), SUM(thursday_dinner), SUM(friday_lunch), SUM(friday_dinner) FROM "takedowns";'
takedowns_generate_minimum = 'SELECT * FROM "takedowns" WHERE {} = 1 AND ("membership" = "In-House 2" OR "membership" = "In-House 3" OR "membership" = "Townsman") AND used = 0 ORDER BY "takedown_count";'
takedowns_generate_update= '''
                                    BEGIN;
                                    UPDATE takedowns SET takedown_count = takedown_count + 1 WHERE slack_id = "{}";
                                    UPDATE takedowns SET used = 1 WHERE slack_id = "{}";
                                    UPDATE "takedowns_{}" SET assignment = "{}" WHERE slack_id = "{}";
                                    COMMIT;
                                  '''
takedowns_generate_fill = 'SELECT * FROM "takedowns" WHERE {} = 1 AND used = 0 ORDER BY "takedown_count";'
takedowns_generate_remaining = 'SELECT slack_id FROM "takedowns" WHERE used = 0;'
takedowns_generate_break = 'UPDATE "takedowns_{}" SET assignment = "Break" WHERE slack_id = "{}";'
takedowns_generate_updateUsed = 'UPDATE takedowns SET used = 0;'
takedowns_generate_error = '''
                             BEGIN;
                             UPDATE takedowns SET takedown_count = takedown_count - 1 WHERE used = 1;
                             UPDATE takedowns SET used = 0;
                             UPDATE "takedowns_{}" SET assignment = NULL;
                             COMMIT;
                          '''
takedowns_generate_selectOutput = 'SELECT name, assignment FROM "takedowns_{}" ORDER BY assignment ASC;'
takedowns_revert_select = 'SELECT slack_id FROM "takedowns_{}" WHERE assignment != "Break";'
takedowns_revert_update = 'UPDATE "takedowns" SET takedown_count = takedown_count - 1 WHERE slack_id = "{}";'
takedowns_revert_week = 'UPDATE "takedowns_{}" SET assignment = "NULL";'
# Admin
admin_select = 'SELECT * FROM admin where slack_id = "{}";'
admin_add_select = 'SELECT slack_id FROM admin WHERE slack_id = "{}";'
admin_add_insert = 'INSERT INTO admin(slack_id, position) VALUES(?,?);'
admin_add_update = 'UPDATE admin SET position = "{}" WHERE slack_id = "{}";'
# Takedowns Display
takedowns_display_select = 'SELECT name, membership, takedown_count, monday_lunch, monday_dinner, tuesday_lunch, tuesday_dinner, wednesday_lunch, wednesday_dinner, thursday_lunch, thursday_dinner, friday_lunch, friday_dinner FROM takedowns;'
# Cleanups Display
cleanups_display_select = 'SELECT * FROM cleanups;'