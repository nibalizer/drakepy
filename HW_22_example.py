# Example problem 2.2
#
from numpy import *
from pylab import *

#Personal functions
def promptForNumber(prompt):
    while True:
        response = raw_input(prompt)
        try:
            number = float(response)
            return number
        except ValueError:
            print "You did not enter a number.\n"

def promptForBoolean(prompt):
    while True:
       response = raw_input(prompt)
       if response in ('y', 'yes'):
            return True
       if response in ('n', 'no'):
            return False

#print headers and get user input
print "[2.2] Using the Euler Method to model bicycle velocity with air resistance."


power = promptForNumber('Bicyclist\'s power output in watts (near 400 watts suggested): ')
mass = promptForNumber('Bicyclist\'s mass in kg (60 kg suggested):  ')
drag_coefficient = promptForNumber('Drag coefficient (1 suggested):  ')
area = promptForNumber('Cross-sectional area of bicyclist in meters (0.33 suggested): ')
air_density = 1.2
print "Air density: %.2f\nInitial Velocity: 1\nInitial time: 0" %air_density
max_time = promptForNumber('Upper time boundary in seconds(>1): ')
if max_time < 1:
        print "Upper time boundary must be greater than 1, using default value of 50."
        max_time = 50
suggested_step_size = (max_time / 100);
step_size_string = "Step size (%.2f suggested)" %suggested_step_size
step_size = promptForNumber(step_size_string)

second_biker = promptForBoolean('Add a second bicyclist for comparison (y/n)?: ')
if second_biker == True:
        second_power = promptForNumber('Second bicyclist\'s power: ')
        second_area = promptForNumber('Second bicyclist\'s cross-sectional area: ')
        second_mass = promptForNumber('Second bicyclist\'s mass: ')    

num_indices = ceil(max_time / step_size)

data_points = np.zeros((num_indices, 2), dtype=np.float)

time_array = np.zeros(num_indices, dtype = np.float)
velocity_array = np.zeros(num_indices, dtype= np.float)


i =0
previous_velocity = 0
time = 0
velocity = 0


##Initial Conditions
velocity_array[0] = 1

##Second biker

if second_biker == True:
    second_velocity_array = np.zeros(num_indices, dtype = np.float)
    second_velocity = 0
    previous_second_velocity = 0
    second_velocity_array[0] = 1

for i in range(1, int(num_indices-1)):
    previous_velocity = velocity_array[i-1]
    velocity = previous_velocity + (step_size * ( power / (mass * previous_velocity) ) ) - ( step_size * ( (drag_coefficient * air_density * area * pow(previous_velocity, 2) ) / (2 * mass)))
    time = time + step_size
    time_array[i] = time
    velocity_array[i] = velocity

    if second_biker == True:
        previous_second_velocity = second_velocity_array[i-1]
        second_velocity = previous_second_velocity + (step_size * ( second_power / (second_mass * previous_second_velocity) ) ) - ( step_size * ( (drag_coefficient * air_density * second_area * pow(previous_second_velocity, 2) ) / (2 * second_mass)))
        second_velocity_array[i] = second_velocity
    
ion()
biker_one_string = "Biker One: P = %.0fW, A = %.2fm^2" %(power, area)
if second_biker == True:
    biker_two_string = "Biker Two: P = %.0fW, A = %.2fm^2" %(second_power, second_area)

scatter(time_array, velocity_array, s=8, marker='o', c='r', label = biker_one_string)

if second_biker == True:
    scatter(time_array, second_velocity_array, s=8, marker='o', c='b', label = biker_two_string)
xlabel('Time (s)')
ylabel('Velocity (m/s)')
title('2.2: Bicycle with air resistance (v vs. t)')
grid(True)

if second_biker == True:
    legend((biker_one_string, biker_two_string), loc = 'lower right')


