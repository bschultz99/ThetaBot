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
#Generate Cleanups Database
cleanups_database_table = 'CREATE TABLE IF NOT EXISTS cleanups AS SELECT * FROM users;'
cleanups_database_alter = '''
                            BEGIN;
                            ALTER TABLE cleanups ADD COLUMN used boolean DEFAULT FALSE;
                            ALTER TABLE cleanups ADD COLUMN captain boolean DEFAULT TRUE;
                            ALTER TABLE cleanups ADD COLUMN captainCount integer DEFAULT 0;
                            UPDATE cleanups SET captain = FALSE WHERE membership = "New Member";
                            COMMIT;
                          '''
cleanups_database_select = 'SELECT cleanup_id from cleanup_settings;'
cleanups_database_alterCleanups = 'ALTER TABLE cleanups ADD COLUMN "{}" integer DEFAULT 0;'
