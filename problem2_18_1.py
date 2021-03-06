

def problem2_18():
	from math import *
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

