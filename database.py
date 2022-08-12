import sqlite3
from sqlite3 import Error
from datetime import date
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
                                        user_id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        membership text NOT NULL,
                                        slack_id integer NOT NULL
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
    create_table(conn, user_table_sql)
    create_table(conn, takedowns_table_sql)

def add_user(conn, user):
    select_sql = "SELECT * FROM users WHERE slack_id=?"
    insert_sql = "INSERT INTO users(name,membership,slack_id) VALUES(?,?,?)"
    update_sql = "UPDATE users SET name = ?, membership = ? WHERE slack_id = ?"
    cur = conn.cursor()
    cur.execute(select_sql, (user[2],))
    rows = cur.fetchall()
    if not rows:
        cur.execute(insert_sql, user)
        conn.commit()
    else:
        cur.execute(update_sql, user)
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

