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
users_remove_delete = '''
                        BEGIN;
                        DELETE FROM users WHERE slack_id = "{}";
                        DELETE FROM cleanups WHERE slack_id = "{}";
                        COMMIT;
                      '''
#Generate Cleanups Database
cleanups_database_select = 'SELECT cleanup_id from cleanup_settings;'
cleanups_database_alterCleanups = 'ALTER TABLE cleanups ADD COLUMN "{}" integer DEFAULT 0;'
