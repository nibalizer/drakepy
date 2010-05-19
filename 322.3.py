# Spencer Krum
# May 2, 2010
# Assignment 3
# Computational Physics PH321 Spring '10
# Dr. Drake Mitchell

##	Problems 2.14, 2.18, 3_3, 3_4

##	Namespace	##
import matplotlib.pyplot as plt
import numpy as np
import array 
from hw3eq import *

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
		functions = (1,2,3,4)
		
		print "Welcome to Spencer Krum's 322 Assignment 3"
		print "Press q at any time to leave"
		print ""
		print "There are 4 problems. Press 1,2, 3, or 4 to run that problem."
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
					chap2p14()
				elif number == 2:
					chap2p18()
				elif number == 3:
					chap2_3_3()
				elif number == 4:
					chap2_3_4()
				elif number == 10:
					eq2_10()
				elif number == 2.2:
					problem2_2()
				elif number == 2.6:
					problem2_6()	
			else: 
				print "Sorry, There is no problem or equation number %d" % number

##	Problem Functions	##

def chap2p14():
	for i in range(40):
		print "\n"
	print "Welcome to problem 2.14"

	problem2_14()

		
	print "Problem done"
	raw_input("Press return to go back to the mainmenu")
	mainmenu()

def chap2p18():
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

def chap2_3_3():
	for i in range(20):
		print ""
	print "Welcome to Problem 2.2"
	print "A cannonball with the effects of air."
	print "Lets do problem2_9"
	problem2_9()
	print "Problem done"
	raw_input("Press return to go back to the mainmenu")
	mainmenu()

def chap2_3_4():
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








