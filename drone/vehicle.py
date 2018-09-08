import dronekit_sitl
from dronekit import connect, VehicleMode
import time

class Vehicle():

    def connect(self, port):
        self.sitl = dronekit_sitl.start_default()
        connection_string = "tcp:127.0.0.1:" + str(port)
        # Connect to the Vehicle.
        print("Connecting to vehicle on: %s" % (connection_string,))
        vehicle = connect(connection_string, wait_ready=True)

        # Get some vehicle attributes (state)
        print("Get some vehicle attribute values:")
        print(" GPS: %s" % vehicle.gps_0)
        print(" Battery: %s" % vehicle.battery)
        print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
        print(" Is Armable?: %s" % vehicle.is_armable)
        print(" System status: %s" % vehicle.system_status.state)
        print(" Mode: %s" % vehicle.mode.name)    # settable
        print("Completed")