import sqlite3
import os
#This file contains all methods for creating and modifying the SQLite db
# @authors Tyler Georgia, Jack Truskowski

DATABASE_NAME = "naxodrone.db"

def initTable(table_name, cols):
    
    c = conn.cursor()
    db_cols = "("
    for col in cols:
        db_cols += col[0] + " " + col[1] + ","
    db_cols = db_cols[:-1]
    db_cols += ")"
    
    # Create table
    try:
        c.execute('''CREATE TABLE ''' + table_name + " " + db_cols)
    except:
        print("Failed to create table: " + table_name + "\n\tMake sure query is well-formed")
    
    print("Successfully created table: " + table_name)

    # Save (commit) the changes
    conn.commit()
    
def createConnection(db_file):
    """ create a database connection to the SQLite database 
	    specified by the db_file
	:param db_file: database file
	:return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    
    except Error as e:
        print(e)	
	
    return none


def addDrone(drone_id, loc_id, serial_num=None):
    conn = createConnection(DATABASE_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM locations WHERE id = ?;", (loc_id,))
    a = cur.fetchone()
    
    if a != None:
        try:
            cur.execute('''INSERT INTO drones (droneid, locationid, payloadStatus, isAvailable, serialNum) VALUES(?, ?, ?, ?, ?); ''', (drone_id, loc_id, 0, 1, serial_num))
            conn.close()
            return 0
        except:
            conn.close()
            return -1
    else:
        conn.close()
        return -2

def authenticateUser(email, password):
    conn = createConnection(DATABASE_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", (email,))
    a = cur.fetchone()

    if a != None:
        if a[2] == password:
            return 0
        else:
            return -1
    else:
        return -2
        
'''    
def request_drone(locationID):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM location \
                          WHERE ID = ?;", locationID)
    a = fetchone()
    if a == 1:
        cur.execute("SELECT droneControlNumber FROM drone \
                              WHERE ID = ? \
                              AND payloadStatus = 1 \
                              And isAvailable = 1;", locationID)
        fetch = fetchone()
        return fetch
    else: 
        return -1

def drone_Payload_Status(boolIN, droneID):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM drones \
                          WHERE droneID = ?;", droneID)
    a = fetchone()
    
    if a == 1:
        if boolIN == None:
            cur.execute("SELECT payloadStatus FROM drone\
                                WHERE droneID = ?;", droneID)
            return fetchone()
        elif boolIN == True:
            cur.execute("UPDATE drone SET payloadStatus = 1\
                                WHERE droneID = ?;", droneID)
            return 0
        elif boolIN == False:
            cur.execute("UPDATE drone SET payloadStatus = 0\
                                WHERE droneID = ?;", droneID)
            return 0
        else: 
            return -1

def set_Drone_Availability(boolIN, droneID):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM drones \
                          WHERE droneID = ?;", droneID)
    a = fetchone()
    
    if a == 1:
        if boolIN == True:
            cur.execute("UPDATE drone SET isAvailable = 1 \
                                WHERE droneID = ?;", droneID)
            return 0
        elif boolIN == False:
            cur.execute("UPDATE drone SET isAvailable = 0 \
                                WHERE droneID = ?;", droneID)
            return 0        
        else:
            return -1
'''

'''
Adds a user to the users table
Returns:
0 = success
-1 = failure adding to db
-2 = email address already exists
'''
def addUser(my_id, email, password):

    conn = createConnection(DATABASE_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    a = cur.fetchone()

    if a == None:
        try:
            cur.execute("INSERT INTO users (id, email, password) VALUES(?,?,?);", (my_id, email, password) )       #can add password restrictions ( must be good enough )e
            conn.commit()
            conn.close()
            return 0
        except sqlite3.Error as e:
            print(e)
            conn.close()
            return -1
    else:
        conn.close()
        return -2
    
'''
def update_User_Email(userEmail, userID):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM user \
                          WHERE  userID = ?;", userID)
    a = fetchone()
    if a == 1:
        cur.execute("UPDATE user SET email = ?\
                            WHERE userID = ?;", userEmail, userID)
        return 0
    else:
        return -1
'''

def addLocation(loc_id, name, gps_loc):
    #don't know what checks I should make. Should we allow multiple locations 
    #similar spots with similar names?

    conn = createConnection(DATABASE_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM locations WHERE gps=?", (gps_loc,))
    a = cur.fetchone()
    if a == None:
        try:
            cur.execute("INSERT INTO locations (id, name, gps, naxoloneCount) VALUES (?, ?, ?, ?);", (loc_id, name, gps_loc, 0))
            conn.commit()
            return 0
        except sqlite3.Error as e:
            print(e)
            conn.close()
            return -1
    return -2
            

def add_Naxolone(numNaxolone, locationID):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM location \
                          WHERE  ID = ?;", locationID)
    a = fetchone()

    if a == 1:
        cur.execute("UPDATE location SET Naxolone = Naxolone + ?;", numNaxolone)
        return 0
    else:
        return -1

def decrement_Naxolone(locationID):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM location \
                          WHERE  ID = ?;", locationID)
    a = fetchone()

    if a == 1:
        cur.execute("UPDATE location SET naxolone = naxolone - 1;")
        return 0
    else: 
        return -1

def naxolone_Count(locationID):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM location \
                          WHERE  ID = ?;", locationID)
    a = fetchone()

    if a == 1:
        cur.execute("SELECT naxolone FROM location\
                            WHERE ID = ?;", locationID)
        numNaxolone = fetchone()
        return numNaxolone
    else:
        return -1

def check_Admin_UserName(username):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM location \
                          WHERE  userName = ?;", username)
    a = fetchone()

    if a == 1:
        cur.execute("SELECT userID FROM administrator\
                            WHERE userName = ?;", username)
        return fetchone()
    else:
        return -1   #Admin username not found

def check_User_Email(email):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM user \
                          WHERE  email = ?;", email)
    a = fetchone()

    if a == 1:
        cur.execute("SELECT userID FROM user\
                            WHERE email = ?;", email)
        return fetchone()
    else:
        return -1   #User email not found

def checkUserPswd(userID, pswd):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM user \
                          WHERE  userID = ?\
                          AND password = ?;", userID, pswd)
    a = fetchone()

    if a == 1:
        return 0
    else:
        return -1

def check_Admin_Password(adminID, pswd):
    cur = conn.cursur()
    cur.execute("SELECT COUNT(*) FROM administrator \
                          WHERE  ID = ?\
                          AND password = ?;", adminID, pswd)
    a = fetchone()

    if a == 1:
        return 0
    else:
        return -1

    
#### Main entry point
if __name__ == "__main__":
    print("Running this file creates a new database and will overwrite the existing database. \n\tAre you sure? (Enter 'n' to cancel)")
    user_input = input()
    if user_input.lower() == 'n':
        exit(0)
        
    try:
        os.remove("naxodrone.db")
    except:
        print("No existing database found... continuing")

    #Create the tables
    conn = sqlite3.connect('naxodrone.db')
    initTable("drones", [("droneid", "INTEGER"), ("locationid", "INTEGER"), ("payloadStatus", "BOOLEAN"), ("isAvailable", "BOOLEAN"), ("serialNum", "INTEGER")])
    
    initTable("locations", [("id", "INTEGER"), ("name", "TEXT"), ("gps", "INTEGER"), ("naxoloneCount", "INTEGER")])

    initTable("users", [("id", "INTEGER"), ("email", "TEXT"), ("password", "TEXT")])

    initTable("addresses", [("id", "INTEGER"), ("street", "TEXT"), ("state", "TEXT"), ("zip", "INTEGER"), ("userid", "INTEGER")])

    initTable("administrators", [("id", "INTEGER"), ("firstName", "TEXT"), ("lastName", "TEXT"), ("username", "TEXT"), ("password", "TEXT")])

    #close the connection
    conn.close()
