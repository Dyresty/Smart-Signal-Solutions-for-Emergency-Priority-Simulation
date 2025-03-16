# Smart Signal Solutions for Emergency Priority Simulation
Using Sumo Simulation <br>

### 1. Introduction<br>
Traffic signal control systems are crucial in managing urban traffic, ensuring orderly vehicle flow at intersections. Under normal conditions, these systems help prevent congestion and maintain safety. However, when emergency vehicles, such as ambulances, fire trucks, or police cars, encounter these signals, delays can significantly hinder their response times, potentially risking lives. Integrating advanced sensors into traffic signal control systems offer a promising solution to address this issue. By prioritizing emergency vehicles at intersections, traffic signals can dynamically adjust to provide a clear path, thus reducing response times and enhancing emergency response effectiveness[1].<br>

#### 1.1. Research Question
“How can traffic signal control systems be optimized to prioritize emergency vehicles, thereby minimizing their response time and improving overall emergency response effectiveness?” 
#### 1.2. Objectives of the Simulation
##### 1. Traffic Signal Adaptation: To develop algorithms for real-time adaptation of traffic signals to prioritize emergency vehicles.
##### 2. Response Time Reduction: To measure the reduction in response times for emergency vehicles using the optimized system.
### 2. Methodology
##### General Data Needed:<br>
1. Traffic Demand: Including the types of vehicles and their frequencies.<br>
2. Time Duration of Signals: Red and green signal durations.<br>
3. Peak Traffic Time: Time of the day at which traffic is at maximum levels.<br>
4. Waiting Time: The wait time of vehicles at a traffic signal.<br>
##### Key Performance Indicators (KPI)<br>
1. Waiting Time: The duration emergency vehicles spend waiting at the signal.<br>
2. Average Speed: The average speed of emergency vehicles within the project site.<br>
##### Data Collection and Data Collected:<br>
Field Data Collection (29th May, Wednesday, 8:00 am - 9:00 am):<br>
● Field: B303 road connecting Kronach, Neuses, and the highway.<br>
● Ratio: Approximately 5-7 cars and 2-3 trucks per red signal.<br>
● Frequency: From Kulmbach's side, approximately 7 vehicles (2 trucks, 5 cars) stop per signal, and from Kups’ end, approximately 9 vehicles (2 trucks, 7 cars) stop per signal.<br>
● Signal Durations: Red signal lasts approximately 1 minute and 15 seconds, with green signal durations of approximately 25 seconds.<br>
● Peak Traffic Time: Identified as office hours (8:00 am - 10:00 am and 3:00 pm - 5:00 pm).<br>
##### Preparation steps in SUMO<br>
1. Map Conversion: Utilized Open Street Maps for the designated location.<br>
2. Converted map data into SUMO-compatible format using osmNetconvert.typ file into ‘test.net.xml’ file.<br>
2. Trip Generation: Developed randomTripsGen.py to create random trips for simulation with ‘trips.rou.xml’ file. Adjusted trips based on field data for accuracy.<br>
3. Detector Setup: Configured detector units with ‘detectors.add’ file. Defined detector locations for monitoring vehicle movements.<br>
4. Configuration File: Created map.sumo.cfg to link network, route, and additional files for simulation.<br>
##### Description of Parameters:<br>
Network File (net-file): 'test.net.xml'<br>
Route Files (route-files): ‘trips.rou.xml’<br>
Additional Files (additional-files): ‘detectors.add.xml’<br>
Begin Time (begin): Set to 0 seconds.<br>
End Time (end): Set to 1200 seconds.<br>
Output file: fcd_output.xml<br>
Python Scripts:<br>
traffic_control.py: Manages detector units and signal phase changes.<br>
calculate_average_speed.py: Calculates average speed and wait time for emergency vehicles.<br>
randomTripsGen.py: Generates random trips with specified start and end points.<br>
### 3. Execution and Results
#### 3.1 Simulation Process
After defining key indicators and collecting data the simulation was performed with the help of network, route, traci, python scripts, and additional files. The trips and signal phases were adjusted according to the data collected from the field to simulate the situation accurately. The simulation is done in two ways, once without the detector units interacting with the traffic signal and once using the implementation of the detector units. In the simulation, the emergency vehicle is shown in red color and the other vehicles are shown in yellow color. The traffic density and the signal timings are adjusted according to the data collected on the field at peak traffic time.<br>
The situation of what an emergency vehicle would go through at peak traffic time is simulated, without considering the vehicles that would let way for emergency vehicles. It can be seen that the emergency vehicle is waiting behind the other vehicles, and driving as a normal vehicle.<br>
Traci Python script is used to simulate the detector units for changing the traffic signal when the detector unit recognizes an emergency vehicle. After detection, the specific signal connected to the sensor turns green.<br>
The randomly generated trips in the simulation help to simulate the randomness of the real world and understand its effectiveness. Ten observations have been noted.
#### 3.2 Observations
The observations of the simulation have been noted in Table 1. The average speed and the waiting time have been calculated with the help of a Python program that takes in the XML information from the output file. The actual waiting time at the red signal was 1 min 15 sec but for the simulation purpose we have reduced it accordingly.

##### Effect of Signal Optimization on KPI’s

| No. | Waiting Time (sec) With Sensor | Waiting Time (sec) Without Sensor | Average Speed (m/s) With Sensor | Average Speed (m/s) Without Sensor |
|----|------------------|------------------|---------------------------|----------------------------|
| 1  | 1                | 37               | 16.52                      | 12.92                       |
| 2  | 1                | 1                | 14.77                      | 14.74                       |
| 3  | 1                | 1                | 16.76                      | 16.66                       |
| 4  | 1                | 33               | 14.86                      | 12.42                       |
| 5  | 1                | 35               | 14.82                      | 11.79                       |
| 6  | 1                | 19               | 15.44                      | 13.21                       |
| 7  | 1                | 1                | 17.19                      | 17.09                       |
| 8  | 1                | 38               | 16.55                      | 13.25                       |
| 9  | 1                | 37               | 15.42                      | 13.53                       |
| 10 | 1                | 31               | 15.14                      | 12.10                       |
| **Average** | **1** | **23.3** | **15.75** | **13.77** |

The optimization of signals led to a significant effect on the KPIs defined earlier. The waiting time for emergency vehicles has reduced to 1 second which was 23.3 seconds before the implementation of sensors. The average speed of the emergency vehicle also increased to 15.75 m/s which was 13.77 m/s before optimization[2].<br>

#### 3.3 Key Findings Focused on Objectives
##### 1. Traffic Signal Adaptation
The developed algorithm enables real-time traffic signal adjustment to prioritize emergency vehicles. Placing the detector unit at an approximate distance of 100m from the signal serves two crucial purposes. We ensure the accurate detection of emergency vehicles and facilitate their smooth passage. This setup remains effective even during heavy traffic congestion near the signal, preventing situations where the emergency vehicle might get blocked far from the sensor unit, leading to undetected status. Secondly, this distance allows vehicles stopped at the signal sufficient time to resume movement before the emergency vehicle approaches the intersection.

##### 2. Response Time Reduction
The response time according to our observation has reduced as a reduction in wait time also indicates a reduction in response time. Hence, we can say that the usage of detection units drastically reduces the waiting time at signals, thereby increasing the average speed of the emergency vehicle and also reducing the response time. 

### 4. Discussion and Conclusion
##### Summary of main findings
The developed algorithm facilitates real-time adjustments of traffic signals to prioritize emergency vehicles through strategically positioned detector units. Placing these units at least 100 meters from traffic signals ensures early detection of emergency vehicles and grants sufficient time for vehicles stopped at signals to resume movement before the emergency vehicle arrives at intersections. Consequently, the waiting time for emergency vehicles at signals dramatically reduced from 23.3 seconds to a mere 1 second, leading to increased average speeds from 13.77m/s to 15.75m/s and decreased overall response times.<br>
##### Evaluation of the results in terms of their relevance and applicability
Our study aimed to optimize traffic signal control systems to prioritize emergency vehicles, reducing response times and improving overall emergency response effectiveness. Our algorithm enables real-time adjustment of traffic signals to prioritize emergency vehicles, providing a crucial solution for urban traffic management. By strategically placing detector units 100 meters from signals, we ensure reliable detection and smooth passage, even in heavy traffic. Our system's ability to drastically reduce response times for emergency vehicles signifies a significant improvement in urban emergency response capabilities. This reduction ensures swift navigation through intersections, ultimately leading to quicker assistance during critical situations.<br>
Moreover, the increase in average speed shows the practical applicability of our approach in enhancing overall traffic flow and minimizing delays.
##### Practical Application:
Simulation in the B303 project validates our approach's practicality in real-world scenarios, showcasing its potential to aid emergency responders. By prioritizing emergencies and optimizing traffic signals, our method improves emergency response effectiveness and traffic management efficiency under emergencies. This highlights the relevance of our findings in addressing pressing urban challenges and improving transportation of emergency vehicles efficiency on urban road networks.

### References
[1] LOO, YIM LING ; AHMAD, AZHANA ; MUSTAPHA, AIDA ; MOSTAFA, SALAMA A.: A Self-Adaptive Agent-Based Dynamic Processes Simulation Modelling Framework. In: 2021 4th International Symposium on Agents, Multi-Agent Systems and Robotics (ISAMSR). Batu Pahat, Malaysia : IEEE, 2021 — ISBN 978-1-66543-632-8, S. 124–129<br>
[2] XIE, XIAO-FENG ; SMITH, STEPHEN F. ; CHEN, TING-WEI ; BARLOW, GREGORY J.: Real-time traffic control for sustainable urban living. In: 17th International IEEE Conference on Intelligent Transportation Systems (ITSC). Qingdao, China : IEEE, 2014 — ISBN 978-1-4799-6078-1, S.1863–1868<br>

### Simulation Video
The video of the simulation and the explanation of the code have been added in the link below.<br>
https://drive.google.com/file/d/11aMXgOoRsZjghq_T7efsic98OFPkSbDG/view?usp=sharing

