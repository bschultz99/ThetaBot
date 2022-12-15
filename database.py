import sqlite3
from sqlite3 import Error
from datetime import date
from sql import *
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def startup(conn):
    user_table_sql = """ CREATE TABLE IF NOT EXISTS users (
                                        slack_id text PRIMARY KEY,
                                        name text NOT NULL,
                                        membership text NOT NULL
                                    ); """
    takedowns_table_sql = """ CREATE TABLE IF NOT EXISTS takedowns (
                                        takedown_id integer PRIMARY KEY,
                                        monday_lunch text,
                                        monday_dinner text,
                                        tuesday_lunch text,
                                        tuesday_dinner text,
                                        wednesday_lunch text,
                                        wednesday_dinner text,
                                        thursday_lunch text,
                                        thursday_dinner text,
                                        friday_lunch text,
                                        friday_dinner text,
                                        takedown_count integer,
                                        break_count integer,
                                        membership text NOT NULL,
                                        slack_id integer NOT NULL
                                    ); """
    cleanup_settings_sql = """ CREATE TABLE IF NOT EXISTS cleanup_settings (
                                        cleanup_id text PRIMARY KEY,
                                        deck_requirement integer NOT NULL,
                                        townsman_captain boolean NOT NULL,
                                        minimum_inhouse integer NOT NULL,
                                        minimum_people integer NOT NULL
                                    ); """
    create_table(conn, user_table_sql)
    create_table(conn, cleanup_settings_sql)
    create_table(conn, takedowns_table_sql)

def add_user(conn, user):
    select_sql = "SELECT * FROM users WHERE slack_id=?"
    insert_sql = "INSERT INTO users(slack_id, name, membership) VALUES(?,?,?)"
    update_sql = "UPDATE users SET name = '{}', membership = '{}' WHERE slack_id = '{}'"
    cur = conn.cursor()
    cur.execute(select_sql, (user[0],))
    rows = cur.fetchall()
    if not rows:
        cur.execute(insert_sql, user)
        conn.commit()
    else:
        cur.execute(update_sql.format(user[1],user[2], user[0]))
        conn.commit()
    #Update/ADD Cleanup Database
    select_database_sql = "SELECT * FROM cleanups WHERE slack_id =?"
    insert_database_sql = "INSERT INTO cleanups(slack_id, name, membership) VALUES(?,?,?)"
    update_database_sql = "UPDATE cleanups SET name = '{}', membership = '{}' WHERE slack_id = '{}'"
    cur = conn.cursor()
    cur.execute(select_database_sql, (user[0],))
    rows = cur.fetchall()
    if not rows:
        cur.execute(insert_database_sql, user)
        conn.commit()
    else:
        cur.execute(update_database_sql.format(user[1],user[2], user[0]))
        conn.commit()
    update_captain_sql = " UPDATE cleanups SET captain = FALSE WHERE membership = 'New Member' AND slack_id = ?;"
    update_captain_sql2 = "UPDATE cleanups SET captain = TRUE WHERE membership != 'New Member' AND slack_id = ?;"
    cur.execute(update_captain_sql, (user[0],))
    conn.commit()
    cur.execute(update_captain_sql2, (user[0],))
    conn.commit()

def remove_user(conn, slack_id):
    remove_sql = "DELETE FROM users WHERE slack_id = ?"
    cur = conn.cursor()
    cur.execute(remove_sql, (slack_id,))
    conn.commit()
    remove_database_sql = "DELETE FROM cleanups WHERE slack_id = ?"
    cur = conn.cursor()
    cur.execute(remove_database_sql, (slack_id,))
    conn.commit()

def add_takedown(conn, takedowns):
    select_sql = "SELECT * FROM takedowns WHERE slack_id=?"
    insert_sql = "INSERT INTO takedowns(monday_lunch, monday_dinner, tuesday_lunch, tuesday_dinner, wednesday_lunch, wednesday_dinner, thursday_lunch, thursday_dinner, friday_lunch, friday_dinner, membership, slack_id) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
    update_sql = "UPDATE takedowns SET monday_lunch = ?, monday_dinner = ?, tuesday_lunch = ?, tuesday_dinner = ?, wednesday_lunch = ?, wednesday_dinner = ?, thursday_lunch = ?, thursday_dinner = ?, friday_lunch = ?, friday_dinner = ?, membership = ? WHERE slack_id = ?"
    cur = conn.cursor()
    cur.execute(select_sql, (takedowns[11],))
    rows = cur.fetchall()
    print(rows)
    if not rows:
        cur.execute(insert_sql, takedowns)
        conn.commit()
    else:
        cur.execute(update_sql, takedowns)
        conn.commit()

def add_cleanup(conn, cleanup_setting):
    select_sql = "SELECT * FROM cleanup_settings WHERE cleanup_id=?"
    insert_sql = "INSERT INTO cleanup_settings(cleanup_id,deck_requirement,townsman_captain, minimum_inhouse, minimum_people) VALUES(?,?,?,?,?)"
    update_sql = "UPDATE cleanup_settings SET deck_requirement = ?, townsman_captain = ?, minimum_inhouse = ?, minimum_people = ? WHERE cleanup_id = ?"
    cur = conn.cursor()
    cur.execute(select_sql, (cleanup_setting[0],))
    rows = cur.fetchall()
    if not rows:
        cur.execute(insert_sql, cleanup_setting)
        conn.commit()
    else:
        cur.execute(update_sql, cleanup_setting[1:] + (cleanup_setting[0],))
        conn.commit()
def remove_cleanup(conn, cleanupName):
    remove_sql = "DELETE FROM cleanup_settings WHERE cleanup_id = ?"
    cur = conn.cursor()
    cur.execute(remove_sql, (cleanupName,))
    conn.commit()

def generate_cleanups_database(con):
    cur = con.cursor()
    create_table(con, cleanups_database_table)
    try:
        cur.executescript(cleanups_database_alter)
        for cleanUp in (cur.execute(cleanups_database_select)).fetchall():
            cur.execute(cleanups_database_alterCleanups.format(cleanUp[0]))
            con.commit()
    except Error as e:
        print(e)

def generate_cleanups(conn):
    today = date.today()
    cleanups_table_sql = f""" CREATE TABLE IF NOT EXISTS 'cleanups_{today}' AS
                                    SELECT slack_id, name
                                    FROM users
                                ;""" 
    alter_cleanups_sql = f"ALTER TABLE 'cleanups_{today}' ADD COLUMN captain DEFAULT 0"
    alter_cleanups_2_sql = f"ALTER TABLE 'cleanups_{today}' ADD COLUMN cleanup DEFAULT NULL"
    create_table(conn, cleanups_table_sql)
    try:
        cur = conn.cursor()
        cur.execute(alter_cleanups_sql)
        cur.execute(alter_cleanups_2_sql)
        conn.commit()
    except:
        print("Fuckity remove this later as the table shouldn't double generate I hope")
    #Retrieve List of cleanups
    select_cleanups_sql = "SELECT * FROM cleanup_settings ORDER BY townsman_captain, deck_requirement"
    cur = conn.cursor()
    cur.execute(select_cleanups_sql)
    cleanups = cur.fetchall()
    #Captain Selection
    #GO BACK AND UPDATE ' INTO "
    update_captain_sql = "UPDATE cleanups SET captainCount = captainCount + 1 WHERE slack_id = '{}'"
    update_captain2_sql = 'UPDATE cleanups SET "{}" = "{}" + 1 WHERE slack_id = "{}"'
    update_used_sql = 'UPDATE cleanups SET used = 1 WHERE slack_id = "{}"'
    update_weekly_captain_sql = 'UPDATE "cleanups_{}" SET captain = 1 WHERE slack_id = "{}"'
    update_weekly_cleanup_sql = 'UPDATE "cleanups_{}" SET cleanup = "{}" WHERE slack_id = "{}"'
    cur = conn.cursor()
    #FOR LOOP THIS SHIT WITH ALL CLEANUPS
    for cleanup in cleanups:
        if cleanup[1] == 0 and cleanup[2] == 0: #In-House
            select_captain_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE captain = 1 AND used = 0 AND (membership = "In-House 3" OR membership = "In-House 2")
                                ORDER BY "{}" ASC, captainCount ASC
                                ;'''
        elif cleanup[1] == 2 and cleanup[2] == 0: #In-House 2
            select_captain_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE captain = 1 AND used = 0 AND membership = "In-House 2"
                                ORDER BY "{}" ASC, captainCount ASC
                                ;'''
        elif cleanup[1] == 3 and cleanup[2] == 0: #In-House 3
            select_captain_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE captain = 1 AND used = 0 AND membership = "In-House 3"
                                ORDER BY "{}" ASC, captainCount ASC
                                ;'''
        elif cleanup[1] == 0 and cleanup[2] == 1: #In-House and Townsman
            select_captain_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE captain = 1 AND used = 0
                                ORDER BY "{}" ASC, captainCount ASC
                                ;'''
        elif cleanup[1] == 2 and cleanup[2] == 1: #In-House 2 and Townsman
            select_captain_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE captain = 1 AND used = 0 AND (membership = "In-House 2" OR membership = "Townsman")
                                ORDER BY "{}" ASC, captainCount ASC
                                ;'''
        else: # In-House 3 and townsman
            select_captain_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE captain = 1 AND used = 0 AND (membership = "In-House 3" or membership = "Townsman")
                                ORDER BY "{}" ASC, captainCount ASC
                                ;'''
        cur.execute(select_captain_sql.format(cleanup[0]))
        captain = cur.fetchone()[0]
        try:
            cur.execute(update_captain_sql.format(captain))
            cur.execute(update_captain2_sql.format(cleanup[0], cleanup[0], captain))
            cur.execute(update_used_sql.format(captain))
            cur.execute(update_weekly_captain_sql.format(today, captain))
            cur.execute(update_weekly_cleanup_sql.format(today, cleanup[0], captain))
            conn.commit()
        except:
            print("BIG ERROR")
    #Generate Minimum-InHouse
    for cleanup in cleanups:
        if cleanup[1] == 0: #In-House 2 and In-House 3
            select_cleanup_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE used = 0 AND (membership = "In-House 2" OR membership = "In-House 3")
                                ORDER BY "{}" ASC
                                ;'''
        elif cleanup[1] == 2 and cleanup[2] == 0: #In-House2
            select_cleanup_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE used = 0 AND membership = "In-House 2"
                                ORDER BY "{}" ASC
                                ;'''
        elif cleanup[1] == 3 and cleanup[2] == 0: #In-House 3
            select_cleanup_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE used = 0 AND membership = "In-House 3"
                                ORDER BY "{}" ASC
                                ;'''
        update_inhouse_sql = 'UPDATE cleanups SET "{}" = "{}" + 1 WHERE slack_id = "{}"'
        update_used_sql = 'UPDATE cleanups SET used = 1 WHERE slack_id = "{}"'
        update_weekly_cleanup_sql = 'UPDATE "cleanups_{}" SET cleanup = "{}" WHERE slack_id = "{}"'
        for x in range(cleanup[3]):
            cur.execute(select_cleanup_sql.format(cleanup[0]))
            person = cur.fetchone()[0]
            try:
                cur.execute(update_inhouse_sql.format(cleanup[0], cleanup[0], person))
                cur.execute(update_used_sql.format(person))
                cur.execute(update_weekly_cleanup_sql.format(today, cleanup[0], person))
                conn.commit()
            except Error as e:
                print(e)
    #Generate Minimum-People
    for cleanup in cleanups:
        if cleanup[1] == 0: #Anyone
            select_cleanup_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE used = 0
                                ORDER BY "{}" ASC
                                ;'''
        elif cleanup[1] == 2: #In-House 2 and townsman/new members
            select_cleanup_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE used = 0 AND (membership = "In-House 2" OR membership = "Townsman" OR membership = "New Member")
                                ORDER BY "{}" ASC
                                ;'''
        elif cleanup[1] == 3: #In-House 3 and townsman/new members
            select_cleanup_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE used = 0 AND (membership = "In-House 3" OR membership = "Townsman" OR membership = "New Member")
                                ORDER BY "{}" ASC
                                ;'''
        update_inhouse_sql = 'UPDATE cleanups SET "{}" = "{}" + 1 WHERE slack_id = "{}"'
        update_used_sql = 'UPDATE cleanups SET used = 1 WHERE slack_id = "{}"'
        update_weekly_cleanup_sql = 'UPDATE "cleanups_{}" SET cleanup = "{}" WHERE slack_id = "{}"'
        for x in range(cleanup[4]-(cleanup[3]+1)):
            cur.execute(select_cleanup_sql.format(cleanup[0]))
            person = cur.fetchone()[0]
            try:
                cur.execute(update_inhouse_sql.format(cleanup[0], cleanup[0], person))
                cur.execute(update_used_sql.format(person))
                cur.execute(update_weekly_cleanup_sql.format(today, cleanup[0], person))
                conn.commit()
            except Error as e:
                print(e)
    #Fill in the Rest
    rest_cleanup_sql = 'SELECT Count() FROM cleanups WHERE used = 0'
    cleanups_sql = 'SELECT cleanup_id, deck_requirement FROM cleanup_settings WHERE townsman_captain = 0 ORDER BY deck_requirement DESC'
    select_cleanup_sql = ''' SELECT slack_id FROM cleanups
                            WHERE used = 0 
                            ORDER BY "{}" ASC
                            ;'''
    cur.execute(rest_cleanup_sql)
    rest = cur.fetchone()[0]
    cur.execute(cleanups_sql)
    cleanups = cur.fetchall()
    cleanupCounter = 0
    for x in range(rest):
        cleanup = cleanups[cleanupCounter]
        if cleanup[1] == 0: #Anyone
            select_cleanup_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE used = 0
                                ORDER BY "{}" ASC
                                ;'''
        elif cleanup[1] == 2: #In-House 2 and townsman/new members
            select_cleanup_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE used = 0 AND (membership = "In-House 2" OR membership = "Townsman" OR membership = "New Member")
                                ORDER BY "{}" ASC
                                ;'''
        elif cleanup[1] == 3: #In-House 3 and townsman/new members
            select_cleanup_sql = ''' SELECT slack_id FROM cleanups 
                                WHERE used = 0 AND (membership = "In-House 3" OR membership = "Townsman" OR membership = "New Member")
                                ORDER BY "{}" ASC
                                ;'''
        cur.execute(select_cleanup_sql.format(cleanup[0]))
        person = cur.fetchone()[0]
        try:
            cur.execute(update_inhouse_sql.format(cleanup[0], cleanup[0], person))
            cur.execute(update_used_sql.format(person))
            cur.execute(update_weekly_cleanup_sql.format(today, cleanup[0], person))
            conn.commit()
            if cleanupCounter+1 == len(cleanups):
                cleanupCounter = 0
            else:
                cleanupCounter += 1
        except Error as e:
                print(e)
    #Reset used column
    update_used_sql = 'UPDATE cleanups SET used = 0'
    cur.execute(update_used_sql)
    conn.commit()


def generate_takedown(conn):
    today = date.today()
    takedowns_table_sql = f""" CREATE TABLE IF NOT EXISTS [{today}] (
                                        slots integer,
                                        monday_lunch text,
                                        monday_dinner text,
                                        tuesday_lunch text,
                                        tuesday_dinner text,
                                        wednesday_lunch text,
                                        wednesday_dinner text,
                                        thursday_lunch text,
                                        thursday_dinner text,
                                        friday_lunch text,
                                        friday_dinner text
                                    ); """
    create_table(conn, takedowns_table_sql)
    select_sql = "SELECT SUM(monday_lunch), SUM(monday_dinner), SUM(tuesday_lunch), SUM(tuesday_dinner), SUM(wednesday_lunch), SUM(wednesday_dinner), SUM(thursday_lunch), SUM(thursday_dinner), SUM(friday_lunch), SUM(friday_dinner) from takedowns"
    select_sql_new = "SELECT SUM(monday_lunch), SUM(monday_dinner), SUM(tuesday_lunch), SUM(tuesday_dinner), SUM(wednesday_lunch), SUM(wednesday_dinner), SUM(thursday_lunch), SUM(thursday_dinner), SUM(friday_lunch), SUM(friday_dinner) from takedowns where membership = 'New Member'"
    cur = conn.cursor()
    cur.execute(select_sql)
    sum = cur.fetchall()
    cur = conn.cursor()
    cur.execute(select_sql_new)
    new = cur.fetchall()

    for x in range(10):
        if (sum[0][x]-new[0][x] < 5):
            return False

