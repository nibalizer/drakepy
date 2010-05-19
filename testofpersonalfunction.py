
#Personal functions
def promptForNumber(prompt):
    while True:
	response = raw_input(prompt)
	try:
		if response == 'q':
			exit()
		else: 
			number = float(response)
	   		return number
	except ValueError:
	    print "You did not enter a number.\n"


for i in range(10):

	x = promptForNumber("Lies %d: " % i)
	print x
