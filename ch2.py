
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

P = promptForNumber("Enter value for Power, P: ")	

m = promptForNumber("Enter value for mass, m: ")

deltat = promptForNumber("Enter value for timestep, deltat: ")

N = promptForNumber("Enter value for number of time steps, N: ")

v0 = promptForNumber("Enter value for the initial value for the velocity, v0: ")

C = promptForNumber("Enter value for the initial value for the velocity, v0: ")

rho = promptForNumber("Enter value for the initial value for the velocity, v0: ")

A  = promptForNumber("Enter value for the initial value for the velocity, v0: ")

##	Process Data		##
v = [v0]
t = [0]



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
	ion()
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

	C = promptForNumber("Enter value for the initial value for the velocity, v0: ")

	rho = promptForNumber("Enter value for the initial value for the velocity, v0: ")

	A  = promptForNumber("Enter value for the initial value for the velocity, v0: ")

	##	Initialize Arrays	
	v = [v0]
	t = [0]


	##	Extend Arrays 
	for i in range(int(N+1)):
		v.append(v[i] + ((P/(m*(v[i])))*deltat) - ((C*rho*A*(v[i]**2))/(2*m)))
		t.append(t[i] + deltat)

	##	Graph
	ion()		
	plot(t, v, 'g+')
	ylabel('Velocity')
	xlabel('Time')
	grid(True)
	title('Equation 2_10')
	draw()
	hold(False)





##	Run			##
calculate(t, v, P, m, deltat, N)

##	Graph			##
print t
print v


plot(t, v, 'g+')
ylabel('Velocity')
xlabel('Time')
grid(True)
title('Book Example 2.1 Bicycle')
draw()
hold(False)

raw_input("Enter return when finished")
