
##	Namespace	##

from pylab import *
ion()
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

##	User Imput		##

#P = promptForNumber("Enter value for Power, P: ")	

#m = promptForNumber("Enter value for mass, m: ")

#deltat = promptForNumber("Enter value for timestep, deltat: ")

#N = promptForNumber("Enter value for number of time steps, N: ")

#v0 = promptForNumber("Enter value for the initial value for the velocity, v0: ")

#C = promptForNumber("Enter value for the initial value for the velocity, v0: ")

#rho = promptForNumber("Enter value for the initial value for the velocity, v0: ")

#A  = promptForNumber("Enter value for the initial value for the velocity, v0: ")

##	Process Data		##
#v = [v0]
#t = [0]



##	Calculate Subroutine	##
def calculate(t, v, P, m, deltat, N):
	for i in range(int(N+1)):
		v.append(v[i] + ((P/(m*(v[i])))*deltat))
		t.append(t[i] + deltat)

##	eq2_7			##

def eq2_7():
	##	Input
	P = promptForNumber("Enter value for Power, P: ")	

	m = promptForNumber("Enter value for mass, m: ")

	deltat = promptForNumber("Enter value for timestep, deltat: ")

	N = promptForNumber("Enter value for number of time steps, N: ")

	v0 = promptForNumber("Enter value for the initial value for the velocity, v0: ")

	##	Initialize Arrays	
	v = [v0]
	t = [0]


	##	Extend Arrays 
	for i in range(int(N+1)):
		v.append(v[i] + ((P/(m*(v[i])))*deltat))
		t.append(t[i] + deltat)

	##	Graph		

	plot(t, v, 'g+')
	ylabel('Velocity')
	xlabel('Time')
	grid(True)
	title('Equation 2_7')
	draw()
	hold(False)


def eq2_10():
	##	Input
	P = promptForNumber("Enter value for Power, P: ")	

	m = promptForNumber("Enter value for mass, m: ")

	deltat = promptForNumber("Enter value for timestep, deltat: ")

	N = promptForNumber("Enter value for number of time steps, N: ")

	v0 = promptForNumber("Enter value for the initial value for the velocity, v0: ")

	C = promptForNumber("Enter value for the drag coefficient, C: ")

	rho = promptForNumber("Enter value for the air density, rho: ")

	A  = promptForNumber("Enter value for cross sectional area, A: ")

	##	Initialize Arrays	
	v = [v0]
	t = [0]


	##	Extend Arrays 
	for i in range(int(N+1)):
		v.append(v[i] + ((P/(m*(v[i])))*deltat) - ((C*rho*A*(v[i]**2))/(2*m))*deltat)
		t.append(t[i] + deltat)

	##	Graph		
	plot(t, v, 'g+')
	ylabel('Velocity')
	xlabel('Time')
	grid(True)
	title('Equation 2_10')
	draw()
	hold(False)

def problem2_2():
	
	##	Input
#	P = promptForNumber("Enter value for Power, P: ")	

#	m = promptForNumber("Enter value for mass, m: ")

	delta  = promptForNumber("Enter value for step size, delta: ")

#	N = promptForNumber("Enter value for maximum cross sec of steps, N: ")

	vt = promptForNumber("Enter value for the terminal velocity, vt: ")

	C = promptForNumber("Enter value for the drag coefficient, C: ")

	rho = promptForNumber("Enter value for the air density, rho: ")

	Area  = promptForNumber("Enter value for the maximum cross sectional area, A: ")


	##	Initialize Arrays	
	P = [0]
	A = [0]


	##	Extend Arrays 
	for i in range(int((Area/delta))):
		P.append(C*rho*(vt**3)*(i*delta)/2)
		A.append(A[i] + delta)

	##	Graph		
	plot(A, P, 'g-')
	ylabel('Power')
	xlabel('Cross Sectional Area')
	grid(True)
	title('For a given terminal velocity v=%d, the power required for cross sectional area' % vt)
	draw()
	hold(False)


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




##



##



##	Run			##
#calculate(t, v, P, m, deltat, N)

##	Graph			##
#print t
#print v


#plot(t, v, 'g+')
#ylabel('Velocity')
#xlabel('Time')
#grid(True)
#title('Book Example 2.1 Bicycle')
#draw()
#hold(False)

#raw_input("Enter return when finished")
