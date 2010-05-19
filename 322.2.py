# Spencer Krum
# May 2, 2010
# Assignment 2
# Computational Physics PH321 Spring '10
# Dr. Drake Mitchell

##	Problems 2.2, 2.6, 2.9


##	Namespace	##
import matplotlib.pyplot as plt
import numpy as np
import array 
from ch2eq import *

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

def mainmenu():
	while True:
		functions = (1,2,3,7,10,2.2,2.6)
		
		print "Welcome to Spencer Krum's 322 Assignment 2"
		print "Press q at any time to leave"
		print ""
		print "There are 3 problems. Press 1,2,or 3 to run that problem."
		print "A number of functions are loaded from chapter 2 as well."
		print "The following imputs should do things:"
		print functions
		print "For numbers not 1,2,3; the number corresponds to the equation from the book being modeled."
		print "For instance the imput of 7 starts a function for eq 2.7"
		while True:	
			number = promptForNumber("Run problem: ")
			if number in functions:
				print "Going to number %d" % number
				if number == 1:
					chap2p2()
				elif number == 2:
					chap2p6()
				elif number == 3:
					chap2p9()
				elif number == 7:
					eq2_7()
				elif number == 10:
					eq2_10()
				elif number == 2.2:
					problem2_2()
				elif number == 2.6:
					problem2_6()	
			else: 
				print "Sorry, There is no problem or equation number %d" % number

##	Problem Functions	##

def chap2p2():
	for i in range(40):
		print "\n"
	print "Welcome to Problem 2.2"
	print "What is the effect of cross sectional area?"
	print "For two riders, one in the front of the pack, another drafting from the middle, the difference in cross sectional area is about 30%"
	print "Equation 2.10 (call it with '7' on the main menu) shows velocity vs time for constant power."
	print "This equation asymptotically approaches the terminal velocity for a given set of conditions."
	print "Assuming that terminal velocity is when v(t+1) = v(t) we can rearange eq 2.10 as:"
	print "P=C*rho*A*(v^3)/2"
	print "This allows us to graph power vs cross sectional area for any terminal velocity."
	print "We now call function problem2_2(), call it from mainmenu with '2.2'"

	problem2_2()

		
	print "Problem done"
	raw_input("Press return to go back to the mainmenu")
	mainmenu()

def chap2p6():
	for i in range(20):
		print ""
	print "Welcome to Problem 2.6"
	print "A cannonball launched in a vacuum."
	print "Following book example pseudocode 2.2"
	print "We now call function problem 2_6(), call it from mainmenu with '2.6'"
	
	problem2_6()

	print "Problem done"
	raw_input("Press return to go back to the mainmenu")
	mainmenu()

def chap2p9():
	for i in range(20):
		print ""
	print "Welcome to Problem 2.2"
	print "A cannonball with the effects of air."
	print "Lets do problem2_9"
	problem2_9()
	print "Problem done"
	raw_input("Press return to go back to the mainmenu")
	mainmenu()


##	Main			##
mainmenu()











		
