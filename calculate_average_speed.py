import xml.etree.ElementTree as ET

def calculate_average_speed_and_wait_time(fcd_output_file, vehicle_id):
    tree = ET.parse(fcd_output_file)
    root = tree.getroot()

    speed_sum = 0
    speed_count = 0
    accumulated_wait_time = 0

    for timestep in root.findall('timestep'):
        time = float(timestep.get('time'))
        for vehicle in timestep.findall('vehicle'):
            if vehicle.get('id') == vehicle_id:
                speed = float(vehicle.get('speed'))
                speed_sum += speed
                speed_count += 1
                if speed == 0:
                    accumulated_wait_time += 1  # Increment by the timestep duration (assuming 1 second)

    if speed_count > 0:
        average_speed = speed_sum / speed_count
        return average_speed, accumulated_wait_time
    else:
        print(f"Vehicle {vehicle_id} not found in the simulation.")
        return 0, 0

if __name__ == "__main__":
    fcd_output_file = "fcd_output.xml"
    vehicle_id = "emergency"

    avg_speed, total_wait_time = calculate_average_speed_and_wait_time(fcd_output_file, vehicle_id)
    print(f"Average speed of vehicle {vehicle_id}: {avg_speed:.2f} m/s")
    print(f"Accumulated wait time of vehicle {vehicle_id}: {total_wait_time} s")
