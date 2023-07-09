import sqlite3
from sqlite3 import Error
from datetime import date
from sql import *
from display import *

#Creates the connection with the database file
def create_connection(db_file):
    con = None
    try:
        #Check_same_thread is set to false to allow multiple threads to connect to the db
        con = sqlite3.connect(db_file, check_same_thread=False)
        return con
    except Error as e:
        print(e)

#Creates a table in the db based on the provided query
def create_table(con, create_table_sql):
    try:
        cur = con.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)

#Creates the starter tables at app runtime
def startup(con):
    cur = con.cursor()
    create_table(con, users_startup_table)
    create_table(con, cleanupSettings_startup_table)
    create_table(con, cleanups_startup_table)
    create_table(con, takedowns_startup_table)
    create_table(con, admin_startup_table)
    try: 
        cur.executescript(cleanups_startup_alter)
    except Error as e:
        print(e)
    try:
        cur.executescript(takedowns_startup_alter)
    except Error as e:
        print(e)

#Adds user 
def add_user(con, user, takedowns):
    cur = con.cursor()
    if (cur.execute(users_add_select.format(user[0])).fetchall()): #If the user exists update user in db
        cur.execute(users_add_update.format(user[1],user[2], user[0])) #Update name and membership based on slack_id
    else:
        cur.execute(users_add_insert, user) # Add the user to the database if they do not exist
    #Update/ADD Cleanup Database
    if (cur.execute(users_database_select.format(user[0])).fetchall()): #If the user exists update user in the cleanup table
        cur.execute(users_database_update.format(user[1],user[2], user[0])) #Update name and membership based on slack_id
    else:
        cur.execute(users_database_insert, user)#Add the user to the cleanup table if they do not exist
    #Update/ADD takedown Database
    if (cur.execute(users_database_select_takedown.format(user[0])).fetchall()):
        cur.execute(users_database_update_takedown.format(takedowns[0], takedowns[1], takedowns[2], takedowns[3], takedowns[4], takedowns[5], takedowns[6], takedowns[7], takedowns[8], takedowns[9], user[2], user[0]))
    else:
        cur.execute(users_database_insert_takedown.format(takedowns[0], takedowns[1], takedowns[2], takedowns[3], takedowns[4], takedowns[5], takedowns[6], takedowns[7], takedowns[8], takedowns[9], user[2], user[0]))
    con.commit()
    cur.executescript(users_database_updateCaptain.format(user[0], user[0])) #Update captain status

def remove_user(con, slack_id): #Update SQL to include delete from takedowns
    cur = con.cursor()
    cur.executescript(users_remove_delete.format(slack_id, slack_id))

def add_cleanup(con, cleanup_setting):
    cur = con.cursor()
    if (cur.execute(cleanupSettings_add_select.format(cleanup_setting[0])).fetchall()):
        cur.execute(cleanupSettings_add_update.format(cleanup_setting[1], cleanup_setting[2], cleanup_setting[3], cleanup_setting[4], cleanup_setting[0]))
    else:
        cur.execute(cleanupSettings_add_insert, cleanup_setting)
    con.commit()

def remove_cleanup(con, cleanupName):
    cur = con.cursor()
    cur.execute(cleanupSettings_remove_delete.format(cleanupName))
    con.commit()

def generate_cleanups_database(con):
    cur = con.cursor()
    try:
        for cleanup in (cur.execute(cleanups_database_select)).fetchall():
            cur.execute(cleanups_database_alterCleanups.format(cleanup[0]))
            con.commit()
    except Error as e:
        print(e)

def generate_cleanups(con, channel_id, client):
    today = date.today()
    cur = con.cursor()
    create_table(con, cleanups_generate_table.format(today))
    try:
        cur.executescript(cleanups_generate_alter.format(today, today))
    except Error as e:
        print(e)
    for cleanup in (cur.execute(cleanups_generate_select)).fetchall(): #Captain Selection
        if cleanup[1] == 0 and cleanup[2] == 0: #No deck requirement and In-House brother
            captain = (cur.execute(cleanups_generate_selectCaptainInHouse.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 2 and cleanup[2] == 0: #2nd Deck Captain 
            captain = (cur.execute(cleanups_generate_selectCaptainInHouse2.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 3 and cleanup[2] == 0: #3rd Deck Captain
            captain = (cur.execute(cleanups_generate_selectCaptainInHouse3.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 0 and cleanup[2] == 1: #Any Captain
            captain = (cur.execute(cleanups_generate_selectCaptainAll.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 2 and cleanup[2] == 1: #Townsman or 2nd Deck Captain
            captain = (cur.execute(cleanups_generate_selectCaptainInHouse2Townsman.format(cleanup[0]))).fetchone()[0]
        else: #Townsman or 3rd Deck Captain
            captain = (cur.execute(cleanups_generate_selectCaptainInHouse3Townsman.format(cleanup[0]))).fetchone()[0]
        try:
            cur.executescript(cleanups_generate_captainUpdate.format(captain, cleanup[0], cleanup[0], captain, captain, today, captain, today, cleanup[0], captain))
        except Error as e:
            print(e)
    for cleanup in (cur.execute(cleanups_generate_select)).fetchall(): #Minimum In-House brothers
        if cleanup[1] == 0: #Any In-House
            select = cleanups_generate_selectMinInHouse
        elif cleanup[1] == 2: #2nd Deck In-House
            select = cleanups_generate_selectMinInHouse2
        elif cleanup[1] == 3: #3rd Deck In-House
            select = cleanups_generate_selectMinInHouse3
        for _ in range(cleanup[3] - 1): 
            person = (cur.execute(select.format(cleanup[0]))).fetchone()[0]
            try:
                cur.executescript(cleanups_generate_update.format(cleanup[0], cleanup[0], person, person, today, cleanup[0], person))
            except Error as e:
                print(e)
    for cleanup in (cur.execute(cleanups_generate_select)).fetchall(): #Minimum Brothers
        if cleanup[1] == 0: 
            select = cleanups_generate_selectAll #Any Brother
        elif cleanup[1] == 2: 
            select = cleanups_generate_selectPeople2 #Any 2nd Deck, Townsman, New Member
        elif cleanup[1] == 3: 
            select = cleanups_generate_selectPeople3 #Any 3rd Deck, Townsman, New Member
        for _ in range(cleanup[4]-(cleanup[3]+1)):
            person = (cur.execute(select.format(cleanup[0]))).fetchone()[0]
            try:
                cur.executescript(cleanups_generate_update.format(cleanup[0], cleanup[0], person, person, today, cleanup[0], person))
            except Error as e:
                print(e)
    cleanups = (cur.execute(cleanups_generate_selectCleanup)).fetchall() #Fill in cleanups that aren't townsman focused
    cleanupCounter = 0
    for _ in range((cur.execute(cleanups_generate_selectCount)).fetchone()[0]): #Loop through remaining brothers
        cleanup = cleanups[cleanupCounter] #Choose which cleanup
        if cleanup[1] == 0:
            person = (cur.execute(cleanups_generate_selectAll.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 2:
            person = (cur.execute(cleanups_generate_selectPeople2.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 3: 
            person = (cur.execute(cleanups_generate_selectPeople3.format(cleanup[0]))).fetchone()[0]
        try:
            cur.executescript(cleanups_generate_update.format(cleanup[0], cleanup[0], person, person, today, cleanup[0], person))
            if cleanupCounter+1 == len(cleanups): #If counter of cleanups reaches end reset
                cleanupCounter = 0
            else:
                cleanupCounter += 1 #Move on to next cleanup
        except Error as e:
                print(e)
    cur.execute(cleanups_generate_updateUsed) #Reset used column to 0
    con.commit()
    cleanup_weekly(cleanups_generate_selectOutput.format(today), con, channel_id, client)


def generate_takedown(con, channel_id, client):
    today = date.today()
    cur = con.cursor()
    create_table(con, takedowns_generate_table.format(today))
    try:
        cur.executescript(takedowns_generate_alter.format(today))
    except Error as e:
        print(e)
    sum = list((cur.execute(takedowns_generate_sum).fetchall())[0])
    slots = ('monday_lunch', 'monday_dinner', 'tuesday_lunch', 'tuesday_dinner', 'wednesday_lunch', 'wednesday_dinner', 'thursday_lunch', 'thursday_dinner', 'friday_lunch', 'friday_dinner')
    positions = [0,0,0,0,0,0,0,0,0,0]
    for _ in range(10): #Put 1 Active on each takedown
        position = smallest(sum, positions)
        people = cur.execute(takedowns_generate_minimum.format(slots[position])).fetchall()
        try:
            sum = tuple(x-y for x, y in zip(sum, people[0][5:]))
        except IndexError:
            cur.executescript(takedowns_generate_error.format(today))
            return sum
        positions[position] = 1
        cur.executescript(takedowns_generate_update.format(people[0][0], people[0][0], today, slots[position], people[0][0]))
    positions = [0,0,0,0,0,0,0,0,0,0]
    for _ in range(10): #Fill each takedown so that there are three people on each
        position = smallest(sum, positions)
        people = cur.execute(takedowns_generate_fill.format(slots[position])).fetchall()
        try:
            sum = tuple(x-y for x, y in zip(sum, people[0][5:]))
        except IndexError:
            cur.executescript(takedowns_generate_error.format(today))
            return sum
        cur.executescript(takedowns_generate_update.format(people[0][0], people[0][0], today, slots[position], people[0][0]))
        try:
            sum = tuple(x-y for x, y in zip(sum, people[1][5:]))
        except IndexError:
            cur.executescript(takedowns_generate_error.format(today))
            return sum
        cur.executescript(takedowns_generate_update.format(people[1][0], people[1][0], today, slots[position], people[1][0]))
        positions[position] = 1
    takedown_break = cur.execute(takedowns_generate_remaining).fetchall() #Set everyone else on break
    for i in range(len(takedown_break)):
        cur.execute(takedowns_generate_break.format(today, takedown_break[i][0]))
        con.commit()
    cur.execute(takedowns_generate_updateUsed) #Reset used column to 0
    con.commit()
    takedown_weekly(takedowns_generate_selectOutput.format(today), con, channel_id, client)
        
def revert_takedowns(con):
    today = date.today()
    cur = con.cursor()
    people = list(cur.execute(takedowns_revert_select.format(today)).fetchall()) #List brothers who aren't on break
    for i in range(len(people)):
        cur.execute(takedowns_revert_update.format(people[i][0])) #Revert takedowns database
        con.commit()
    cur.execute(takedowns_revert_week.format(today)) #Revert weekly takedowns generation
    con.commit()

def display_takedowns(con, user_id, client):
    takedowns_display(takedowns_display_select, con, user_id, client)

def display_cleanups(con, user_id, client):
    cleanups_display(cleanups_display_select, con, user_id, client)

def smallest(sum, positions):
    smallest = 1000000
    position = 0
    for i in range(len(sum)):
        if(smallest > sum[i] and positions[i] == 0):
            smallest = sum[i]
            position = i
    return position

def admin_check(con, user_id):
    cur = con.cursor()
    person = cur.execute(admin_select.format(user_id)).fetchall()
    if person:
        return True
    return False

def admin_add(con, position, user_id):
    cur = con.cursor()
    if (cur.execute(admin_add_select.format(user_id)).fetchall()):
        cur.execute(admin_add_update.format(position, user_id))
    else:
        cur.execute(admin_add_insert, (user_id, position))
    con.commit()
