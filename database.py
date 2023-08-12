# pylint: disable=line-too-long, wildcard-import
"""Database"""
import sqlite3
from sqlite3 import Error
from datetime import date
from sql import *
from display import cleanup_weekly, takedown_weekly, takedowns_display, cleanups_display, fines_display, reconcilliations_display, naughtylist_display
from templates import FINE_MESSAGE, RECONCILLIATION_MESSAGE

#Creates the connection with the database file
def create_connection(db_file):
    """Create Connection"""
    con = None
    try:
        #Check_same_thread is set to false to allow multiple threads to connect to the db
        con = sqlite3.connect(db_file, check_same_thread=False)
        return con
    except Error as error:
        print(error)

#Creates a table in the db based on the provided query
def create_table(con, create_table_sql):
    """Create Table"""
    try:
        cur = con.cursor()
        cur.execute(create_table_sql)
    except Error as error:
        print(error)

#Creates the starter tables at app runtime
def startup(con):
    """Startup"""
    cur = con.cursor()
    create_table(con, USERS_STARTUP_TABLE)
    create_table(con, CLEANUPSETTINGS_STARTUP_TABLE)
    create_table(con, CLEANUPS_STARTUP_TABLE)
    create_table(con, TAKEDOWNS_STARTUP_TABLE)
    create_table(con, ADMIN_STARTUP_TABLE)
    create_table(con, FINES_STARTUP_TABLE)
    create_table(con, RECONCILLIATION_STARTUP_TABLE)
    create_table(con, NAUGHTY_STARTUP_TABLE)
    try:
        cur.executescript(CLEANUPS_STARTUP_ALTER)
    except Error as error:
        print(error)
    try:
        cur.executescript(TAKEDOWNS_STARTUP_ALTER)
    except Error as error:
        print(error)
    try:
        cur.executescript(NAUGHTY_STARTUP_ALTER)
    except Error as error:
        print(error)

def add_user(con, user, takedowns):
    """Add user"""
    cur = con.cursor()
    if cur.execute(USERS_ADD_SELECT.format(user[0])).fetchall(): #If the user exists update user in db
        cur.execute(USERS_ADD_UPDATE.format(user[1],user[2], user[0])) #Update name and membership based on slack_id
    else:
        cur.execute(USERS_ADD_INSERT, user) # Add the user to the database if they do not exist
    #Update/ADD Cleanup Database
    if cur.execute(USERS_DATABASE_SELECT.format(user[0])).fetchall(): #If the user exists update user in the cleanup table
        cur.execute(USERS_DATABASE_UPDATE.format(user[1],user[2], user[0])) #Update name and membership based on slack_id
    else:
        cur.execute(USERS_DATABASE_INSERT, user)#Add the user to the cleanup table if they do not exist
    #Update/ADD takedown Database
    if cur.execute(USERS_DATABASE_SELECT_TAKEDOWN.format(user[0])).fetchall():
        cur.execute(USERS_DATABASE_UPDATE_TAKEDOWN.format(takedowns[0], takedowns[1], takedowns[2], takedowns[3], takedowns[4], takedowns[5], takedowns[6], takedowns[7], takedowns[8], takedowns[9], user[2], user[0]))
    else:
        cur.execute(USERS_DATABASE_INSERT_TAKEDOWN.format(takedowns[0], takedowns[1], takedowns[2], takedowns[3], takedowns[4], takedowns[5], takedowns[6], takedowns[7], takedowns[8], takedowns[9], user[2], user[0]))
    #Update/ADD naughty Database
    if cur.execute(USERS_DATABASE_SELECT_NAUGHTY.format(user[0])).fetchall(): #If the user exists update user in the naughty table
        cur.execute(USERS_DATABASE_UPDATE_NAUGHTY.format(user[1], user[0])) #Update name based on slack_id
    else:
        cur.execute(USERS_DATABASE_INSERT_NAUGHTY.format(user[0], user[1]))
    con.commit()
    cur.executescript(USERS_DATABASE_UPDATECAPTAIN.format(user[0], user[0])) #Update captain status

def remove_user(con, slack_id): #Update SQL to include delete from takedowns
    """Remove User"""
    cur = con.cursor()
    cur.executescript(USERS_REMOVE_DELETE.format(slack_id, slack_id))

def add_cleanup(con, cleanup_setting):
    """Add Cleanup"""
    cur = con.cursor()
    if cur.execute(CLEANUPSETTINGS_ADD_SELECT.format(cleanup_setting[0])).fetchall():
        cur.execute(CLEANUPSETTINGS_ADD_UPDATE.format(cleanup_setting[1], cleanup_setting[2], cleanup_setting[3], cleanup_setting[4], cleanup_setting[0]))
    else:
        cur.execute(CLEANUPSETTINGS_ADD_INSERT, cleanup_setting)
    con.commit()

def remove_cleanup(con, cleanup_name):
    """Remove Cleanup"""
    cur = con.cursor()
    cur.execute(CLEANUPSETTINGS_REMOVE_DELETE.format(cleanup_name))
    con.commit()

def generate_cleanups_database(con):
    """Generate Cleanups Database"""
    cur = con.cursor()
    try:
        for cleanup in (cur.execute(CLEANUPS_DATABASE_SELECT)).fetchall():
            cur.execute(CLEANUPS_DATABASE_ALTERCLEANUPS.format(cleanup[0]))
            con.commit()
    except Error as error:
        print(error)

def generate_cleanups(con, channel_id, client):
    """Generate Cleanups"""
    today = date.today()
    cur = con.cursor()
    create_table(con, CLEANUPS_GENERATE_TABLE.format(today))
    try:
        cur.executescript(CLEANUPS_GENERATE_ALTER.format(today, today))
    except Error as error:
        print(error)
    for cleanup in (cur.execute(CLEANUPS_GENERATE_SELECT)).fetchall(): #Captain Selection
        if cleanup[1] == 0 and cleanup[2] == 0: #No deck requirement and In-House brother
            captain = (cur.execute(CLEANUPS_GENERATE_SELECTCAPTAININHOUSE.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 2 and cleanup[2] == 0: #2nd Deck Captain
            captain = (cur.execute(CLEANUPS_GENERATE_SELECTCAPTAININHOUSE2.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 3 and cleanup[2] == 0: #3rd Deck Captain
            captain = (cur.execute(CLEANUPS_GENERATE_SELECTCAPTAININHOUSE3.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 0 and cleanup[2] == 1: #Any Captain
            captain = (cur.execute(CLEANUPS_GENERATE_SELECTCAPTAINALL.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 2 and cleanup[2] == 1: #Townsman or 2nd Deck Captain
            captain = (cur.execute(CLEANUPS_GENERATE_SELECTCAPTAININHOUSE2TOWNSMAN.format(cleanup[0]))).fetchone()[0]
        else: #Townsman or 3rd Deck Captain
            captain = (cur.execute(CLEANUPS_GENERATE_SELECTCAPTAININHOUSE3TOWNSMAN.format(cleanup[0]))).fetchone()[0]
        try:
            cur.executescript(CLEANUPS_GENERATE_CAPTAINUPDATE.format(captain, cleanup[0], cleanup[0], captain, captain, today, captain, today, cleanup[0], captain))
        except Error as error:
            print(error)
    for cleanup in (cur.execute(CLEANUPS_GENERATE_SELECT)).fetchall(): #Minimum In-House brothers
        if cleanup[1] == 0: #Any In-House
            select = CLEANUPS_GENERATE_SELECTMININHOUSE
        elif cleanup[1] == 2: #2nd Deck In-House
            select = CLEANUPS_GENERATE_SELECTMININHOUSE2
        elif cleanup[1] == 3: #3rd Deck In-House
            select = CLEANUPS_GENERATE_SELECTMININHOUSE3
        for _ in range(cleanup[3] - 1):
            person = (cur.execute(select.format(cleanup[0]))).fetchone()[0]
            try:
                cur.executescript(CLEANUPS_GENERATE_UPDATE.format(cleanup[0], cleanup[0], person, person, today, cleanup[0], person))
            except Error as error:
                print(error)
    for cleanup in (cur.execute(CLEANUPS_GENERATE_SELECT)).fetchall(): #Minimum Brothers
        if cleanup[1] == 0:
            select = CLEANUPS_GENERATE_SELECTALL #Any Brother
        elif cleanup[1] == 2:
            select = CLEANUPS_GENERATE_SELECTPEOPLE2 #Any 2nd Deck, Townsman, New Member
        elif cleanup[1] == 3:
            select = CLEANUPS_GENERATE_SELECTPEOPLE3 #Any 3rd Deck, Townsman, New Member
        for _ in range(cleanup[4]-(cleanup[3]+1)):
            person = (cur.execute(select.format(cleanup[0]))).fetchone()[0]
            try:
                cur.executescript(CLEANUPS_GENERATE_UPDATE.format(cleanup[0], cleanup[0], person, person, today, cleanup[0], person))
            except Error as error:
                print(error)
    cleanups = (cur.execute(CLEANUPS_GENERATE_SELECTCLEANUP)).fetchall() #Fill in cleanups that aren't townsman focused
    cleanup_counter = 0
    for _ in range((cur.execute(CLEANUPS_GENERATE_SELECTCOUNT)).fetchone()[0]): #Loop through remaining brothers
        cleanup = cleanups[cleanup_counter] #Choose which cleanup
        if cleanup[1] == 0:
            person = (cur.execute(CLEANUPS_GENERATE_SELECTALL.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 2:
            person = (cur.execute(CLEANUPS_GENERATE_SELECTPEOPLE2.format(cleanup[0]))).fetchone()[0]
        elif cleanup[1] == 3:
            person = (cur.execute(CLEANUPS_GENERATE_SELECTPEOPLE3.format(cleanup[0]))).fetchone()[0]
        try:
            cur.executescript(CLEANUPS_GENERATE_UPDATE.format(cleanup[0], cleanup[0], person, person, today, cleanup[0], person))
            if cleanup_counter+1 == len(cleanups): #If counter of cleanups reaches end reset
                cleanup_counter = 0
            else:
                cleanup_counter += 1 #Move on to next cleanup
        except Error as error:
            print(error)
    cur.execute(CLEANUPS_GENERATE_UPDATEUSED) #Reset used column to 0
    con.commit()
    cleanup_weekly(CLEANUPS_GENERATE_SELECTOUTPUT.format(today), con, channel_id, client)

def generate_takedown(con, channel_id, client):
    """Generate Takedowns"""
    today = date.today()
    cur = con.cursor()
    create_table(con, TAKEDOWNS_GENERATE_TABLE.format(today))
    try:
        cur.executescript(TAKEDOWNS_GENERATE_ALTER.format(today))
    except Error as error:
        print(error)
    summation = list((cur.execute(TAKEDOWNS_GENERATE_SUM).fetchall())[0])
    slots = ('monday_lunch', 'monday_dinner', 'tuesday_lunch', 'tuesday_dinner', 'wednesday_lunch', 'wednesday_dinner', 'thursday_lunch', 'thursday_dinner', 'friday_lunch', 'friday_dinner')
    positions = [0,0,0,0,0,0,0,0,0,0]
    for _ in range(10): #Put 1 Active on each takedown
        position = smallest(summation, positions)
        people = cur.execute(TAKEDOWNS_GENERATE_MINIMUM.format(slots[position])).fetchall()
        try:
            summation = tuple(x-y for x, y in zip(summation, people[0][5:]))
        except IndexError:
            cur.executescript(TAKEDOWNS_GENERATE_ERROR.format(today))
            return summation
        positions[position] = 1
        cur.executescript(TAKEDOWNS_GENERATE_UPDATE.format(people[0][0], people[0][0], today, slots[position], people[0][0]))
    positions = [0,0,0,0,0,0,0,0,0,0]
    for _ in range(10): #Fill each takedown so that there are three people on each
        position = smallest(summation, positions)
        people = cur.execute(TAKEDOWNS_GENERATE_FILL.format(slots[position])).fetchall()
        try:
            summation = tuple(x-y for x, y in zip(summation, people[0][5:]))
            cur.executescript(TAKEDOWNS_GENERATE_UPDATE.format(people[0][0], people[0][0], today, slots[position], people[0][0]))
        except IndexError:
            unlucky = cur.executescript(TAKEDOWNS_GENERATE_NOMEMBERS.format(slots[position])).fetchall()
            cur.executescript(TAKEDOWNS_GENERATE_UNLUCKY.format(unlucky[0][0], unlucky[0][0], today, slots[position], unlucky[0][0]))
        try:
            summation = tuple(x-y for x, y in zip(summation, people[1][5:]))
            cur.executescript(TAKEDOWNS_GENERATE_UPDATE.format(people[1][0], people[1][0], today, slots[position], people[1][0]))
        except IndexError:
            unlucky = cur.executescript(TAKEDOWNS_GENERATE_NOMEMBERS.format(slots[position])).fetchall()
            cur.executescript(TAKEDOWNS_GENERATE_UNLUCKY.format(unlucky[0][0], unlucky[0][0], today, slots[position], unlucky[0][0]))
        positions[position] = 1
    takedown_break = cur.execute(TAKEDOWNS_GENERATE_REMAINING).fetchall() #Set everyone else on break
    for value in enumerate(takedown_break):
        cur.execute(TAKEDOWNS_GENERATE_BREAK.format(today, value[0]))
        con.commit()
    cur.execute(TAKEDOWNS_GENERATE_UPDATEUSED) #Reset used column to 0
    con.commit()
    takedown_weekly(TAKEDOWNS_GENERATE_SELECTOUTPUT.format(today), con, channel_id, client)

def revert_takedowns(con):
    """Revert Takedowns"""
    today = date.today()
    cur = con.cursor()
    people = list(cur.execute(TAKEDOWNS_REVERT_SELECT.format(today)).fetchall()) #List brothers who aren't on break
    for person in enumerate(people):
        cur.execute(TAKEDOWNS_REVERT_UPDATE.format(person[0])) #Revert takedowns database
        con.commit()
    cur.execute(TAKEDOWNS_REVERT_WEEK.format(today)) #Revert weekly takedowns generation
    con.commit()

def display_takedowns(con, user_id, client):
    """Display Takedowns"""
    takedowns_display(TAKEDOWNS_DISPLAY_SELECT, con, user_id, client)

def display_cleanups(con, user_id, client):
    """Display Cleanups"""
    cleanups_display(CLEANUPS_DISPLAY_SELECT, con, user_id, client)

def smallest(summation, positions):
    """Smallest"""
    small_value = 1000000
    position = 0
    for i, value in enumerate(summation):
        if(small_value > value and positions[i] == 0):
            small_value = value
            position = i
    return position

def admin_check(con, user_id):
    """Admin Check"""
    cur = con.cursor()
    person = cur.execute(ADMIN_SELECT.format(user_id)).fetchall()
    if person:
        return True
    return False

def admin_add(con, position, user_id):
    """Admin Add"""
    cur = con.cursor()
    if cur.execute(ADMIN_ADD_SELECT.format(user_id)).fetchall():
        cur.execute(ADMIN_ADD_UPDATE.format(position, user_id))
    else:
        cur.execute(ADMIN_ADD_INSERT, (user_id, position))
    con.commit()

def end_semester(con):
    """End Semester"""
    cur = con.cursor()
    tables = cur.execute(DELETE_TABLES_SELECT).fetchall()
    for table in enumerate(tables):
        cur.execute(DELETE_TABLES_DROP.format(table))

def fines(con, person, fine_date, fine_type, reason, amount, issuer, client):
    """Fines"""
    cur = con.cursor()
    if fine_type == 'Cleanup':
        missed_cleanups = cur.execute(FINES_CLEANUPS_SUM.format(person)).fetchone()[0]
        amount = 5 * (missed_cleanups + 1)
    elif fine_type == 'Takedown':
        amount = 5
    elif fine_type == 'Theta Raid':
        amount = 1 * int(amount)
    elif fine_type == 'Roll Call':
        amount = 5 * int(amount)
    elif fine_type == 'Warning':
        amount = 0
    elif fine_type == 'Other':
        amount = int(amount)
    fine = (person, reason, fine_date, amount, fine_type, issuer)
    cur.execute(FINES_DATABASE_INSERT, fine)
    cur.execute(FINES_NAUGHTY_UPDATE.format(amount, person))
    con.commit()
    issuer = cur.execute(ISSUER_SELECT.format(issuer)).fetchone()[0]
    client.chat_postMessage(channel=person, text=FINE_MESSAGE.format(fine_type, reason, fine_date, amount, issuer))

def reconcilliations(con, person, recon_date, recon_type, notes, amount, issuer, client):
    """Reconcilliations"""
    cur = con.cursor()
    reconcilliation = (person, notes, recon_type, recon_date, amount, issuer)
    cur.execute(RECONCILLIATION_DATABASE_INSERT, reconcilliation)
    cur.execute(RECONCILLIATION_NAUGHTY_UPDATE.format(amount, person))
    con.commit()
    issuer = cur.execute(ISSUER_SELECT.format(issuer)).fetchone()[0]
    client.chat_postMessage(channel=person, text=RECONCILLIATION_MESSAGE.format(recon_type, notes, recon_date, amount, issuer))

def display_fines(con, user_id, client):
    """Display Fines List"""
    fines_display(FINES_DISPLAY_SELECT, con, user_id, client)

def display_reconcilliations(con, user_id, client):
    """Display Reconcilliations List"""
    reconcilliations_display(RECONCILLIATIONS_DISPLAY_SELECT, con, user_id, client)

def display_naughtylist(con, user_id, client):
    """Display Naughty List"""
    naughtylist_display(NAUGHTY_DISPLAY_SELECT, con, user_id, client)
