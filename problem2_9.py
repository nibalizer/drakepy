#Spencer Krum
#Computational Physics 322
#Problem 2_9



def problem2_9():
	
	from math import *
	##	Input
	print "A cannon fires in air with varying air pressure."
	print "The depenent variables are the initial velocity vector, decomposed into a speed scalar and a direction,"
	print "We begin with equation 2_10"
	v0 = promptForNumber("Please input the velocity scalar: ")
	angle = promptForNumber("Please input the angle in degrees between 0 and 90: ")
	deltat = promptForNumber("Enter value for timestep, deltat: ")

	C = promptForNumber("Enter value for the drag coefficient, C: ")

	rho = promptForNumber("Enter value for the air density, rho: ")

	A = promptForNumber("Enter value for cross sectional area, A: ")
	
	m = promptForNumber("Enter value for the mass, m: ")


	##	Precalculations
	
	angle = radians(angle)
	vxinitial = cos(angle)*v0	
	vyinitial = sin(angle)*v0

	b2 = (.5)*(C)*(rho)*(A)

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
		hypotenuseV =  sqrt((vx[i]**2) + (vy[i]**2))
		vx.append(vx[i] - ((b2 * hypotenuseV * vx[i])/m)*deltat)
		vy.append(vy[i]-(9.8*deltat)- ((b2 * hypotenuseV * vx[i])/m)*deltat)
		i += 1
	plot(x,y, 'g+')
	ylabel('Height')
	xlabel('Distance')
	grid(True)
	title('Equation 2_20')
	draw()
	hold(False)


