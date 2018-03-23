from dronekit import connect, VehicleMode
import dronekit_sitl as dk_sitl


print "Start  simulator (SITL)"

sitl = dk_sitl.start_default()
connect_string = sitl.connection_string()

# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connect_string,))
vehicle = connect(connect_string, wait_ready=True)

# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.gps_0
print " Battery: %s" % vehicle.battery
print " Last Heartbeat: %s" % vehicle.last_heartbeat
print " Is Armable?: %s" % vehicle.is_armable
print " System status: %s" % vehicle.system_status.state
print " Mode: %s" % vehicle.mode.name    # settable

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")















