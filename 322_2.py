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
		print "Welcome to Spencer Krum's 322 Assignment 2"
		print "Press q at any time to leave"
		print ""
		print "There are 3 problems. Press 1,2,or 3 to run that problem."
		while True:	
			number = promptForNumber("Run problem: ")
			if number in (1,2,3):
				print "Going to number %d" % number
				if number == 1:
					chap2p2()
				elif number == 2:
					chap2p6()
				elif number == 3:
					chap2p9()
			else: 
				print "Sorry, There is no problem number %d" % number

##	Problem Functions	##

def chap2p2():
	for i in range(40):
		print ""
	print "Welcome to Problem 2.2"
	print "Problem done"
	raw_input("Press return to go back to the mainmenu")
	mainmenu()

def chap2p6():
	for i in range(20):
		print ""
	print "Welcome to Problem 2.2"
	print "Problem done"
	raw_input("Press return to go back to the mainmenu")
	mainmenu()

def chap2p9():
	for i in range(20):
		print ""
	print "Welcome to Problem 2.2"
	print "Problem done"
	raw_input("Press return to go back to the mainmenu")
	mainmenu()


##	Main			##
mainmenu()











		
