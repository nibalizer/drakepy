



def problem2_18():
	from math import *
	##	Input
	print "A baseball hit from a bat  in air with varying air pressure and the magnus force"
	print "The s0/m coefficient is 4.1 x10^-4 taken from Adair(1990)"
	print "The equations of motion for this calculation are taken from figure 2.8"
	print "We look at x y only."
	print "The depenent variables are the initial velocity vector, decomposed into a speed scalar and an angle above the x axis, the initial height of the ball, and the timestep."
	print "For fun, you can choose a value for the angular velocity"
	v0 = promptForNumber("Please input the velocity scalar: ")
	angle = promptForNumber("Please input the angle in degrees between 0 and 90: ")
	deltat = promptForNumber("Enter value for timestep, deltat: ")
	yinit = promptForNumber("Enter initial height of the ball")
	w = promptForNumber("Enter the value of the angular velocity")

	
	##	Precalculations
	
	angle = radians(angle)
	vxinitial = cos(angle)*v0	
	vyinitial = sin(angle)*v0
	s0_m = 4.1e-4

	#	Initialize Arrays
	x = [0]
	y = [0]
	z = [0]
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
		vy.append(vy[i]-(9.8*deltat) + (s0_m * w * vx[i])*deltat)
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


