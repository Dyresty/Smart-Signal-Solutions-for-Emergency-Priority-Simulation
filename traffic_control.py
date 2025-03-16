import traci
import sumolib

def control_traffic_lights():
    # Set the traffic light to the green phase
    traci.trafficlight.setPhase("21637580", 0)  # This one is particularly for setting the signal for sensors 1 and 2 to green.

def run_simulation():
    sumoBinary = sumolib.checkBinary('sumo-gui')
    traci.start([sumoBinary, "-c", "map.sumocfg"])

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        # Check if an emergency vehicle is detected by any sensor
        for sensor_id in SENSOR_IDS:
                if sensor_id=='sensor1' or sensor_id=='sensor2':    
                    if traci.inductionloop.getLastStepVehicleIDs(sensor_id):
                        for veh_id in traci.inductionloop.getLastStepVehicleIDs(sensor_id):
                            if traci.vehicle.getTypeID(veh_id) == "emergency":
                                control_traffic_lights()
                                print("EMERGENCY VEHICLE PASSED THE SENSOR")

    traci.close()

if __name__ == "__main__":
    SENSOR_IDS = ["sensor1", "sensor2", "sensor3", "sensor4","sensor5"] 
    run_simulation()
