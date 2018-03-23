import dronekit as dk
import dronekit_sitl as dk_sitl
import time

print "Start  simulator (SITL)"

sitl = dk_sitl.start_default()
connect_string = sitl.connection_string()



# Exception to throw in the event of a failed connection
class NoConnectionError(Exception):
    def __init__(self):
        Exception.__init__(self)




# Drone Autopilot Class
class DronePilot:


    # Constructor Method
    def _init__(self):
        self.connect_string     = None
        self.drone              = None

    # Method to initiate drone connection
    def connect(self,connect_string):

        # Store connect_string in event of disconnect
        self.connect_string = connect_string

        # Display connect message
        print("Autopilot connecting to vehicle on: %s" % (connect_string,))

        # Try to initialize drone connection
        try:
            self.drone = dk.connect(connect_string,wait_ready=True)
        except:

            # Try to reconnect 3 more times before giving up
            attempts = 3
            while attempts > 0:

                # Display message telling how many more attempts
                print "Connection error, ", attempts, " more attempts"
                try:
                    self.drone = dk.connect(connect_string, wait_ready=True)

                    # Break out of loop if connection is successful
                    break
                except:
                    attempts -= 1
            raise NoConnectionError()
        return

    # Run preflight check and arm vehicle
    def preFlight(self):

        # Wait for autopilot to get ready
        while not self.drone.is_armable:
            print "Waiting for autopilot"
            time.sleep(2)

        # Arm autopilot
        print "Arming motors"
        self.drone.mode = dk.VehicleMode("GUIDED")
        self.drone.armed = True

        # Wait for autopilot to arm
        while not self.drone.armed:
            print "Waiting for autopilot to arm"
            time.sleep(2)

        # Print armed confirmation
        print "Vehicle Successfully Armed"

        # Print message
        print "Running Preflight Check"

        # Check vehicle status
        print "Current Status: ", self.drone.system_status

        # Check battery level
        print "Battery Level: ", self.drone.battery

        # Check airspeed
        print "Current Airspeed: ", self.drone.airspeed










    # Method to disconnect from drone
    def disconnect(self):

        # Print closing message
        print "Autopilot disonnecting from vehicle"
        # Close drone connection before exiting script
        self.drone.close()




# Main function to run program
def main():

    # Print simulator message
    print "Starting simulator (SITL)"

    # Start drone simulator
    sitl = dk_sitl.start_default()

    # Get simulated drone connection string
    connect_string = sitl.connection_string()

    # Create new drone autopilot instance
    drone = DronePilot()

    # Initiate Drone Connection
    drone.connect(connect_string)

    # Run preflight check
    drone.preFlight()

    # Close vehicle object before exiting script
    print "Simulation successful"
    drone.disconnect()

    # Shut down simulator if its still running
    try:
        sitl.stop()
    except:
        pass

    # Print completed if all process finished correctly

    print("Completed")

# Run main
main()




















