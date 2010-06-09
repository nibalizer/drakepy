#Spencer Krum
#Computational Physics
#Spring 2010
#PH 322

from matplotlib import *
from pylab import *

##	Normal Functions	##
def promptForNumber(prompt):
    while True:
	response = raw_input(prompt)
	try:
		if response == 'q':
			print "Thank you for using this python physics program"
			exit()
		else: 
			number = float(response)
			return number
	except ValueError:
	    print "You did not enter a number.\n"
def sign(number):
	while True:
		try:
			if  abs(number) == number:
				return 1
			else:
				return -1
		except ValueError:
			print "Not a number?"

def problem2_14_a():
	##	Input
	print "A baseball hit from a bat  in air with varying air pressure and a crosswind"
	print "The depenent variables are the initial velocity vector, decomposed into a speed scalar and a direction,"
	v0 = promptForNumber("Please input the velocity scalar: ")
	angle = promptForNumber("Please input the angle in degrees between 0 and 90: ")
	deltat = promptForNumber("Enter value for timestep, deltat: ")

	
	##	Precalculations
	
	angle = radians(angle)
	vxinitial = cos(angle)*v0	
	vyinitial = sin(angle)*v0


	#	Initialize Arrays
	x = [0]
	y = [0]
	vx = [vxinitial]
	vy = [vyinitial]
	i = 0
	##	Extend Arrays
	while y[i] >= 0: 
		x.append(x[i] + (vx[i]*deltat)) 	
		y.append(y[i] + (vy[i]*deltat))
		hypotenuseV =  sqrt((vx[i]**2) + (vy[i]**2))
		b2m = 0.0039 + 0.0058/(1 + exp((hypotenuseV - 35) / 5))	
		vx.append(vx[i] - ((b2m * hypotenuseV * vx[i])*deltat))
		vy.append(vy[i]-(9.8*deltat)- (b2m * hypotenuseV * vx[i])*deltat)
		i += 1

	##	Graph
	ion()
	plot(x,y, 'g+')
	ylabel('Height')
	xlabel('Distance')
	grid(True)
	distance = x.pop()
	title('Equation 2_26, total range = %f' % distance)
#	legend(distance)
	draw()
	hold(False)






def problem2_14():
	##	Input
	print "A baseball hit from a bat  in air with varying air pressure and a crosswind"
	print "The crosswind is a 10mph crosswind"
	print "10 mph is 4.4704m/s"
	print "The depenent variables are the initial velocity vector, decomposed into a speed scalar and a direction,"
	v0 = promptForNumber("Please input the velocity scalar: ")
	angle = promptForNumber("Please input the angle in degrees between 0 and 90: ")
	deltat = promptForNumber("Enter value for timestep, deltat: ")

	
	##	Precalculations
	
	angle = radians(angle)
	vxinitial = cos(angle)*v0	
	vyinitial = sin(angle)*v0
	vzinitial = 0

	#	Initialize Arrays
	x = [0]
	y = [0]
	z = [0]
	vx = [vxinitial]
	vy = [vyinitial]
	vz = [vzinitial]
	i = 0
	##	Extend Arrays
	while y[i] >= 0: 
		x.append(x[i] + (vx[i]*deltat)) 	
		y.append(y[i] + (vy[i]*deltat))
		z.append(z[i] + (vz[i]*deltat))
		hypotenuseV =  sqrt((vx[i]**2) + (vy[i]**2) + (vz[i]**2))
		b2m = 0.0039 + 0.0058/(1 + exp((hypotenuseV - 35) / 5))	
		vx.append(vx[i] - ((b2m * hypotenuseV * vx[i])*deltat))
		vy.append(vy[i]-(9.8*deltat)- (b2m * hypotenuseV * vx[i])*deltat)
		vz.append(vz[i] + (4.4704*deltat))
		i += 1

	##	Graph
	ion()
	plot(x,y, 'g+')
	ylabel('Height')
	xlabel('Distance')
	grid(True)
	distance = x.pop()
	distancez = z.pop()
	title('Equation 2_26, totalz range = %f' %  distancez)
#	legend(distance)
	draw()
	hold(False)

def problem2_18():
	##input
	print "A baseball hit from a bat  in air with varying air pressure and the magnus force"
	print "The s0/m coefficient is 4.1 x10^-4 taken from Adair(1990)"
	print "The equations of motion for this calculation are taken from figure 2.8"
	print "We look at x y only."
	print "The depenent variables are the initial velocity vector, decomposed into a speed scalar and an angle above the x axis, the initial height of the ball, and the timestep."
	print "For fun, you can choose a value for the angular velocity"
	v0 = promptForNumber("Please input the velocity scalar(in meters per second, 90mph is 40m/s): ")
	angle = promptForNumber("Please input the angle in degrees between 0 and 90: ")
	deltat = promptForNumber("Enter value for timestep, deltat: ")
	yinit = promptForNumber("Enter initial height of the ball(in meters, 2 meters is appropriate): ")
	w = promptForNumber("Enter the value of the rotations per minute on the ball(in rpm, the vanilla problem calls for 1000rpm, you can put a zero in to see a pitch without spin): ")

	
	##	Precalculations
	
	angle = radians(angle)
	vxinitial = cos(angle)*v0	
	vyinitial = sin(angle)*v0
	s0_m = 4.1e-4
	w = 2.54*9*w/60

	#	Initialize Arrays
	x = [0]
	y = [yinit]
	vx = [vxinitial]
	vy = [vyinitial]
	i = 0
	##	Extend Arrays
	while y[i] >= 0: 
		x.append(x[i] + (vx[i]*deltat)) 	
		y.append(y[i] + (vy[i]*deltat))
		hypotenuseV =  sqrt((vx[i]**2) + (vy[i]**2))
		b2m = 0.0039 + 0.0058/(1 + exp((hypotenuseV - 35) / 5))	
		vx.append(vx[i] - ((b2m * hypotenuseV * vx[i])*deltat))
		vy.append(vy[i]-(9.8*deltat) - ((b2m * hypotenuseV * vy[i])*deltat) + ((s0_m * w * vx[i])*deltat))
		i += 1

	##	Graph
	ion()
	plot(x,y, 'g+')
	ylabel('Height')
	xlabel('Distance')
	grid(True)
	distance = x.pop()
	title('Equation 2_30, total range = %f' % distance)
#	legend(distance)
	draw()
	hold(False)


def problem3_3():
	##	Setup
	print "Problem 3.2"
	print "Use the Euler method to simulate the motion of a pendulum as in Figure 3.2. Study the behavior as a function of the step size, deltat, and show that the total energy always increases with time."

	##	Input
	print "The dependent variables are the length of the string, the length of the simulation, and the number of timesteps."
	l = promptForNumber("Please input the length of the string in meters: ")	
	N = promptForNumber("Please input the length of the simulation in seconds: ")
	deltat = promptForNumber("Please input the length of a single timestep deltat in seconds: ")
	theta_init = promptForNumber("Please input the inital angular position in radians: ")
	omega_init = promptForNumber("Please input the inital angular velocity, omega in radians/s: ")
	##	Precalculations
	g = 9.8
	##	Initialize Arrays
	theta = [theta_init]
	omega = [omega_init]
	t = [0]

	##	Extend Arrays
	for i in range(int((N/deltat))):
		omega.append(omega[i] -(((g/l)*theta[i])*deltat))
		theta.append(theta[i] + omega[i]*deltat)
		t.append(t[i] + deltat)


	##	Debug
	print theta, omega, t

	##	Graph
	ion()
	plot(t, theta, 'g-')
	ylabel('Theta')
	xlabel('Time')
	grid(True)
	draw()
	hold(False)
	## hold up
	raw_input("Press return to see omega vs time")
	plot(t, omega, 'g+')
	ylabel('Omega')
	xlabel('Time')
	grid(True)
	draw()
	hold(False)

def syllabus3_3():
	##	Setup
	print "Find the root of f(x) = cos(x)-x = 0 by the method of bisection. How many iterations are necessary to determine the root to eight significant figures?"
	##	Input
	left = promptForNumber("Enter the choice of the left side bound(suggest 0): ")
	right = promptForNumber("Enter the choice of the right side bound(suggest 1): ")
	##	Precalculations
	g = lambda x: cos(x) - x
	iterations = 1
	##	Main Loop
	while True:
		middle = (left + right)/2
		if sign(g(left)) != sign(g(middle)):
			print "The zero is between %.08f and %.08f, maximum uncertainty %.08f, iterations: %d" % (left, middle, abs(middle-right), iterations)
			right = middle
		else:
			print "The zero is between %.08f and %.08f, maximum uncertainty %.08f, iterations: %d" % (middle, right, abs(middle-right), iterations)
			left = middle
		iterations += 1
		response = raw_input("Go for another iteration? (y/n)")
		if response == "n":
			return
					
		
