# Spencer Krum
# April 2, 2010
# Assignment 1 - Due 8 April 2010
# Computational Physics PH321 Spring '10
# Dr. Drake Mitchell

import matplotlib.pyplot as plt
import numpy as np
import array 

def promptForNumber(prompt):
    while True:
        response = raw_input(prompt)
        try:
            number = float(response)
            return number
        except ValueError:
            print "You did not enter a number.\n"


print "Spencer Krum"
print "Assignment 1"

print "Problem 1.1"
print "Calculate solutions to the differential equation dv/dt = -g for times t=0 to t=10"
print "Using Euler's Formula:"
print "dv/dt = -g"
print ""
print ""
print "Taylor Expansion for velocity:"
print "V(t) = Vo + dV/dt delta t + 1/2 d2V/dt2 delta t^2 ..."
print "V(t) = Vo + dV/dt delta t"
print "dV/dt = (V(t + delta t) - V(t)) / delta t"
print "V(t + delta t) = V(t) + dV/dt (delta t)"
print "V(t = delta t) = V(t) - g*(delta t)"
print "Taking falling down to be the negative direction"


times = [1,2,3,4,5,6,7,8,9,10]
velocities = [0,0,0,0,0,0,0,0,0,0]
def calculate(V, t):
         V[t] = V[t-1] + -9.8

for i in range(1,10):
        calculate(velocities, i)
	print velocities[i]


#plt.plot([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8], 'ro')
#plt.ylabel('Some Numbers')
#plt.show


labelone = "A falling object in the absence of air"
plt.plot(times, velocities, marker='o', label = labelone)
plt.xlabel('Time(s)')
plt.ylabel('Velocity (m/s)')
plt.title (labelone)


raw_input("Press enter to see a pretty graph of this data, which fits perfectly the analytical solution")
plt.show()




raw_input("Press enter to begin 1.4")
print "Problem 1.4"
print "Calculate solutions to coupled equations as functions of time using Euler's formula"
print "From book, eq 1.7: Nu (t + delta t) = Nu (t) - (Nu(t)/tau) * delta t"
print "From problem 1.4:"
print "dNa/dt = - Na/taua"
print "dNb/dt = Na/taua - Nb/taub"
print "Substituting:"
print "Na (t + delta t) = Na (t) - (Na(t)/taua) * delta t"
#print "Nb (t + delta t) = Na (t)/taua - (Nb(t)/taub) * delta t"
print "Nb (t + delta t) = Nb (t) + (d/dt Nb (t) * delta t)"
print "Nb (t + delta t) = Nb (t) + (Na(t + delta t)/taua - Nb (t)/taub * delta t)"




times1_4 = [1,2,3,4,5,6,7,8,9,10]
Na = [0,0,0,0,0,0,0,0,0,0]
Nb = [0,0,0,0,0,0,0,0,0,0]
taua = promptForNumber("Enter the time constant for substance A in arbitrary units") 
taub = promptForNumber("Enter the time cosntant for substance B in arbitrary units")
#deltat = promptForNumber("Enter the time step in seconds, 1 suggested")
Na[0] = promptForNumber("Enter the initial ammount of A")
Nb[0] = promptForNumber("Enter the initial ammount of B")


def calculate1_4(A, B, t, timeconstA, timeconstB):
	A[t] = A[t-1] - (A[t-1]/timeconstA )
	B[t] = B[t-1] + ((A[t-1]/timeconstA -  B[t-1]/timeconstB))

for i in range(1,10):
	calculate1_4(Na, Nb, i, taua, taub)
	print Na[i] ,  Nb[i]



labelone = "coupled differential eq. for half lives of particles"
plt.plot(times1_4, Na, marker='o', label ="substance A")
plt.plot(times1_4, Nb, marker='+', label ="substance B")
plt.xlabel('Time(arbitrary units)')
plt.ylabel('Number of particles(arbitrary units)')
plt.title (labelone)

plt.show()


raw_input("Press return to try new values for taua and taub")


times1_4 = [1,2,3,4,5,6,7,8,9,10]
Na = [0,0,0,0,0,0,0,0,0,0]
Nb = [0,0,0,0,0,0,0,0,0,0]
taua = promptForNumber("Enter the time constant for substance A in arbitrary units") 
taub = promptForNumber("Enter the time cosntant for substance B in arbitrary units")
#deltat = promptForNumber("Enter the time step in seconds, 1 suggested")
Na[0] = promptForNumber("Enter the initial ammount of A")
Nb[0] = promptForNumber("Enter the initial ammount of B")





def calculate1_4(A, B, t, timeconstA, timeconstB):
	A[t] = A[t-1] - (A[t-1]/timeconstA )
	B[t] = B[t-1] + ((A[t-1]/timeconstA -  B[t-1]/timeconstB))

for i in range(1,10):
	calculate1_4(Na, Nb, i, taua, taub)
	print Na[i] ,  Nb[i]



labelone = "Coupled differential EQ's "
plt.plot(times1_4, Na, marker='o', label ="substance A")
plt.plot(times1_4, Nb, marker='+', label ="substance B")
plt.xlabel('Time(arbitrary units)')
plt.ylabel('Number of particles(arbitrary units)')
plt.title (labelone)

plt.show()


#
# Problem 1.6
#
from pylab import *

#Problem 1.6

ion()
tstep = float(raw_input("Enter your time step(try 0.0001): "))
initial_pop = float(raw_input("Enter the initial population value(try 100): "))


t3 = arange(0.0, 5.01, tstep)
theory_n1 = arange(0.0, 5.01, tstep)
theory_n2 = arange(0.0, 5.01, tstep)
n1 = arange(0.0, 5.01, tstep)
n2 = arange(0.0, 5.01, tstep)
theory_n1[0] = initial_pop
n1[0] = initial_pop
tau1 = float(raw_input("Enter tau1(try 10): "))
tau2 = float(raw_input("Enter tau2(try 100): "))
theory_n2[0] = 100.0
n2[0] = 100.0
#tstep = t3[1] - t3[0]
for k in range(1, int(5/tstep)):
	theory_n1[k] = n1[0]*exp(1*t3[k]/tau1)
	n1[k] = n1[k-1] + 1*tstep*n1[k-1]/tau1
	n2[k] = n2[k-1] + 1*tstep*n2[k-1]/tau1 - 1*tstep*n2[k-1]*n2[k-1]/tau2
plot(t3, theory_n1, 'g+', t3, n1, 'r-', t3, n2, 'b+')
ylabel('Population N')
xlabel('time (arbitrary units)')
grid(True)
title('a=0.1, b=0: red=theory, green=Euler; a/b=10 blue=Euler ')
draw()
hold(False)
print("Numerical result agrees with analytic result for b=0")

raw_input("Enter return when finished")

