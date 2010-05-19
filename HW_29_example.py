# Problem 2.9 Example
from numpy import *
from pylab import *
from matplotlib.font_manager import fontManager, FontProperties

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
print "[2.9] Modeling a projectile with the Euler Method."


initial_velocity = promptForNumber('Initial velocity in m/s (700): ')
firing_angle = promptForNumber('Firing angle in degrees (1-90):  ')


##convert to degrees
firing_angle = firing_angle * (pi / 180)

print "Initial velocity = %.2f\nFiring Angle = %.2f rad\n" %(initial_velocity, firing_angle)

time_array = np.zeros(1, dtype=np.float)

velocity_x_array = np.zeros(1, dtype=np.float)
velocity_y_array = np.zeros(1, dtype=np.float)

velocity_x_with_drag_array = np.zeros(1, dtype=np.float)
velocity_y_with_drag_array = np.zeros(1, dtype=np.float)

position_x_array = np.zeros(1, dtype=np.float)
position_y_array = np.zeros(1, dtype=np.float)

position_x_with_drag_array = np.zeros(1, dtype=np.float)
position_y_with_drag_array = np.zeros(1, dtype=np.float)

##Compute initial velocity components
velocity_x_array[0] = initial_velocity * cos(firing_angle)
velocity_y_array[0] = initial_velocity * sin(firing_angle)
velocity_x_with_drag_array[0] = initial_velocity * cos(firing_angle)
velocity_y_with_drag_array[0] = initial_velocity * sin(firing_angle)
initial_density = 1.2
drag_force_coefficient = 0.00004

step_size = 1

at_ground = False

#Loop specific variables
previous_velocity_x = 0
previous_velocity_y = 0
density = 1.2
previous_velocity_x_with_drag = 0
previous_velocity_y_with_drag = 0
velocity_magnitude = 0
velocity_x = 0
velocity_y = 0
drag_force_x = 0
drag_force_y = 0
time = 0

next_velocity_x = 0
next_velocity_y = 0
next_position_x = 0
next_position_y = 0

i = 0

##Do without density correction first
while at_ground != True:
    next_position_x = position_x_array[i] + step_size*velocity_x_array[i]
    next_position_y = position_y_array[i] + step_size*velocity_y_array[i]

   
    velocity_magnitude = sqrt( pow(velocity_x_array[i], 2) + pow(velocity_y_array[i], 2) )
    
    next_velocity_x = velocity_x_array[i] + step_size*(-drag_force_coefficient * velocity_magnitude * velocity_x_array[i])
    next_velocity_y = velocity_y_array[i] + step_size*(-9.8 - drag_force_coefficient * velocity_magnitude * velocity_y_array[i])

    velocity_x_array = np.append(velocity_x_array, next_velocity_x)
    velocity_y_array = np.append(velocity_y_array, next_velocity_y)


    position_x_array = np.append(position_x_array, next_position_x)
    position_y_array = np.append(position_y_array, next_position_y)

    if next_position_y < 0:
        at_ground = True
    
    i = i + 1


##Interpolate the last point

##Do with density correction
no_density_string = "No density correction (d=%.1fkm)" %(position_x_array[i-1]/1000)

i = 0
at_ground = False

while at_ground != True:
    next_position_x = position_x_with_drag_array[i] + step_size *velocity_x_with_drag_array[i]
    next_position_y = position_y_with_drag_array[i] + step_size *velocity_y_with_drag_array[i]

   
    density = 1.2 * exp( - position_y_with_drag_array[i] / 10000 ) / 1.2
    velocity_magnitude = sqrt( pow(velocity_x_with_drag_array[i], 2) + pow(velocity_y_with_drag_array[i], 2) )
    
    next_velocity_x = velocity_x_with_drag_array[i] + step_size*(-drag_force_coefficient * velocity_magnitude * velocity_x_with_drag_array[i] * density)
    next_velocity_y = velocity_y_with_drag_array[i] + step_size*(-9.8 - drag_force_coefficient * velocity_magnitude * velocity_y_with_drag_array[i] * density)

    velocity_x_with_drag_array = np.append(velocity_x_with_drag_array, next_velocity_x)
    velocity_y_with_drag_array = np.append(velocity_y_with_drag_array, next_velocity_y)
   
    position_x_with_drag_array = np.append(position_x_with_drag_array, next_position_x)
    position_y_with_drag_array = np.append(position_y_with_drag_array, next_position_y)

    i = i + 1

    if next_position_y < 0:
       i = i - 1
       at_ground = True


density_string = "Density correction (d=%.1fkm)" %(position_x_with_drag_array[i-1]/1000)

##Find best angle
best_angle = 0
best_distance = 0
test_angle = 1
current_angle = 1

test_velocity_x_array = np.zeros(250, dtype=float)
test_velocity_y_array = np.zeros(250, dtype=float)
test_position_x_array = np.zeros(250, dtype=float)
test_position_y_array = np.zeros(250, dtype=float)

i = 0
at_ground = False

##Test each angle
for test_angle in range(90):

    current_angle = test_angle * ( pi / 180)
    i = 0
    at_ground = False

    test_velocity_x_array[0] = initial_velocity*cos(current_angle)
    test_velocity_y_array[0] = initial_velocity*sin(current_angle)
    
    
    while at_ground != True:
        next_position_x = test_position_x_array[i] + step_size *test_velocity_x_array[i]
        next_position_y = test_position_y_array[i] + step_size *test_velocity_y_array[i]

        if next_position_y < 0:
           i = i - 1
           at_ground = True
        else:
            density = 1.2 * exp( - test_position_y_array[i] / 10000 ) / 1.2
            velocity_magnitude = sqrt( pow(test_velocity_x_array[i], 2) + pow(test_velocity_y_array[i], 2) )
            
            next_velocity_x = test_velocity_x_array[i] + step_size*(-drag_force_coefficient * velocity_magnitude * test_velocity_x_array[i] * density)
            next_velocity_y = test_velocity_y_array[i] + step_size*(-9.8 - drag_force_coefficient * velocity_magnitude * test_velocity_y_array[i] * density)

            test_velocity_x_array[i+1] = next_velocity_x
            test_velocity_y_array[i+1] = next_velocity_y
           
            test_position_x_array[i+1] = next_position_x
            test_position_y_array[i+1] = next_position_y

            i = i + 1

    if test_position_x_array[i] > best_distance:
        best_distance = test_position_x_array[i]
        best_angle = test_angle


##Draw best angle
current_angle = best_angle * ( pi / 180)
i = 0
at_ground = False

test_velocity_x_array = np.zeros(250, dtype=float)
test_velocity_y_array = np.zeros(250, dtype=float)
test_position_x_array = np.zeros(250, dtype=float)
test_position_y_array = np.zeros(250, dtype=float)

test_velocity_x_array[0] = initial_velocity*cos(current_angle)
test_velocity_y_array[0] = initial_velocity*sin(current_angle)


while at_ground != True:
    next_position_x = test_position_x_array[i] + step_size * test_velocity_x_array[i]
    next_position_y = test_position_y_array[i] + step_size * test_velocity_y_array[i]

    
    density = 1.2 * exp( - test_position_y_array[i] / 10000 ) / 1.2
    velocity_magnitude = sqrt( pow(test_velocity_x_array[i], 2) + pow(test_velocity_y_array[i], 2) )
    
    next_velocity_x = test_velocity_x_array[i] + step_size*(-drag_force_coefficient * velocity_magnitude * test_velocity_x_array[i] * density)
    next_velocity_y = test_velocity_y_array[i] + step_size*(-9.8 - drag_force_coefficient * velocity_magnitude * test_velocity_y_array[i] * density)

    test_velocity_x_array[i+1] = next_velocity_x
    test_velocity_y_array[i+1] = next_velocity_y
   
    test_position_x_array[i+1] = next_position_x
    test_position_y_array[i+1] = next_position_y

    i = i + 1

    if next_position_y < 0:
       i = i - 1
       at_ground = True


##Trim the zeros, set 0,0 at a non-zero value so it doesn't get trimmed
test_position_x_array[0] = 0.00001
test_position_y_array[0] = 0.00001
test_position_x_array = np.trim_zeros(test_position_x_array)
test_position_y_array = np.trim_zeros(test_position_y_array)

best_string = "Maximum (d=%.1fkm, angle=%.0f)" %((test_position_x_array[i-1]/1000), best_angle)

ion()
##Plot
plot(position_x_array, position_y_array,  c='b', label=no_density_string)
plot(position_x_with_drag_array, position_y_with_drag_array,  c='r', alpha=0.75, label=density_string)
plot(test_position_x_array, test_position_y_array,  c='k', label=best_string)

xlabel('X (m)')
ylabel('Y (m)')
title('2.9 Projectile with air density correction')

##Legend
font = FontProperties(size='small')
legend((no_density_string, density_string, best_string), loc='lower left', prop=font)

axhline(y=0, color='k', alpha=0.5)

