import random

start_points = [ '-781372077','-564556363','-618077409','297659263','-205995791#3','294958226']
end_points = [ '-781372077','-618077409','297659263','294958226','-564556363']

#mid down starter - 294958226, 
#right right place - -781372077, -564556363
#right mid place - -618077409
#left end place - 297659263
#left top end place - -205995791#3

num_trips = 150  # Specify the number of trips
depart_time = 0  # Start time for trips
depart_interval = 0.5  # Time interval between each trip

with open('trips.rou.xml', 'w') as file:
    file.write('<routes>\n')
    timex = round(random.uniform(0, 25), 2)
    count=0
    for i in range(num_trips):
        start = random.choice(start_points)
        end = random.choice(end_points)
        if depart_time>=timex and count==0:
            count=1
            file.write(f'    <trip id="emergency" type="emergency" depart="{timex}" from="-781372077" to="297659263"/>\n')
        file.write(f'    <trip id="{i+1}" depart="{depart_time:.2f}" from="{start}" to="{end}"/>\n')
        depart_time += depart_interval
    file.write('</routes>\n')

