# usecase_whatis_type


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
