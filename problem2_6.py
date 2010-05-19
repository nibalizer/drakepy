#Spencer w
#PH322
#Problem 2_6

from ch2eq import *

def problem2_6():
	
	from math import *
	##	Input
	print "A cannon fires."
	print "The depenent variables are the initial velocity vector, decomposed into a speed scalar and a direction."
	v0 = promptForNumber("Please input the velocity scalar: ")
	angle = promptForNumber("Please input the angle in degrees between 0 and 90: ")
	deltat = promptForNumber("Enter value for timestep, deltat: ")



	##	Precalculations
	
	angle = radians(angle)
	vxinitial = cos(angle)*v0	
	vyinitial = sin(angle)*v0
	##	Initialize Arrays
	x =[0]
	y= [0]
	vx = [vxinitial]
	vy = [vyinitial]
	i = 0
	##	Extend Arrays
	while y[i] >= 0: 
		x.append(x[i] + (vx[i]*deltat)) 	
		y.append(y[i] + (vy[i]*deltat))
		vx.append(vx[i])
		vy.append(vy[i]-(9.8*deltat))
		i += 1
	plot(x,y, 'g+')
	ylabel('Height')
	xlabel('Distance')
	grid(True)
	title('Equation 2_15')
	draw()
	hold(False)

