#a little file for testing the database
#TODO: do real testing
from database_api import *

num_passed = 0
total = 0

#add some locations
print("\n\nTest: Add 2 locations. . .", end='')
total += 1
loc_result = addLocation(0, "hospital", 1.1011)
loc_result2 = addLocation(1, "doctors office", 1.2)
if loc_result != 0 or loc_result2 != 0:
    print("\nFAILED. adding 2 locations should have returned (0, 0) but instead returned (" + str(loc_result), " ," + str(loc_result2))
else:
    num_passed += 1
    print("OK")

#add a drone
print("Test: Adding a drone. . .", end='')
total += 1
result = addDrone(0, 0, 1000)
if result != 0:
    print("\nFAILED. adding drone should have been successful (return 0), but instead returned " + str(result))
else:
    num_passed += 1
    print("OK")
    

#add a user
print("Test: Adding a user. . .", end='')
total += 1
usr_result = addUser(0, "johndoe@wisc.edu", "ultrasecurepassword")
if usr_result != 0:
    print("\nFAILED. adding user should have been successful (return 0), but instead returned " + str(usr_result))
else:
    num_passed += 1
    print("OK")

#authenticate the user
print("Test: Authenticate the user. . .", end = '')
total += 1
auth_result = authenticateUser("johndoe@wisc.edu", "ultrasecurepassword")
if auth_result != 0:
    print("\nFAILED. authenticating user should have been successful (return 0), but instead returned " + str(auth_result))
else:
    num_passed += 1
    print("OK")

#authenticate the user w/ incorrect password
print("Test: Authenticate the user with bad pass. . .", end = '')
total += 1
auth_result = authenticateUser("johndoe@wisc.edu", "aleciomadrid")
if auth_result != -1:
    print("\nFAILED. authenticating user should have failed (return -1), but instead returned " + str(auth_result))
else:
    num_passed += 1
    print("OK")

#authenticate w/ bad user
print("Test: Authenticate with bad email. . .", end = '')
total += 1
auth_result = authenticateUser("iteration1@wisc.edu", "aleciomadrid")
if auth_result != -2:
    print("\nFAILED. authenticating user should have failed (return -2), but instead returned " + str(auth_result))
else:
    num_passed += 1
    print("OK")


#print final stats
print("\nPassed [%d/%d]" % (num_passed, total))
