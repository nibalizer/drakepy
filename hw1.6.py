

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

raw_input("Press return to move on to problem 1.6")
print "1.6 is a problem modeling growth of a population where some individuals live and some die, competing for resources."
print "N is the number of members of a population."
print "a is the 'birth' coefficient"
print "b is the 'death' coefficient"
print "The equation governing this relationship is:"
print "dN/dt = aN -bN^2"
print "Using the Euler approximation"
print "N(t + deltat) = N(t) + (aN - b(N^2)) * deltat"


a = promptForNumber("Enter your desired birth coefficient: ")
b = promptForNumber("Enter your desired death coefficient: ")
initial_popsize = promptForNumber("Enter your desired starting population size: ")
popsize = []
#print (popsize)
popsize.append(initial_popsize)
#print (popsize)
#lowerbound = promptForNumber("Enter your desired lower bounding t value")
upperbound = promptForNumber("Enter your desired upper bounding t value")
timestep = promptForNumber("Enter your desired length of delta t time steps")


def calculate1_6(birth, death, pop, t, timestep):
	 pop.append ( pop[t] + ( (birth * pop[t]) - (death * (pop[t]**2)) * timestep) )

for i in range(1 ,int(upperbound)):
	calculate1_6(a, b, popsize, i, timestep)
	print popsize[i]


labelone = "Population growth model"
plt.plot(popsize, marker='o', label ="substance A")
plt.xlabel('Time(arbitrary units)')
plt.ylabel('Population(arbitrary units)')
plt.title (labelone)

plt.show()


