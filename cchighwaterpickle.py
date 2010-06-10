#Spencer Krum
#Collatz Conjecture w/ pickle
#10 June 2010

import pickle

print "Collatz Conjecture."
print "Collatz conjecture is that any positive integer will become 1 after the following procedure is applied a sufficient number of times."
print "If the number is even, divide it by two. If the number is odd multiply by three and add one."

def theNumber(prompt):
	while True:	
		number = raw_input(prompt)
		try:	
			number = abs(int(number))
			return number
		except ValueError:
			print "Please enter an integer"
def collatz(number_):
	length = 0
	number = number_
	while (number != 1):
	#	print "The number is %d" % number
		length += 1
		if (number % 2 == 0):
	#		print "The number is even, therefore divide by two"
			number = number/2
		else:
	#		print "The number is odd, therefore multiply by three and add one"
			number = (number*3)+1

	if number_ % 100 == 0:
		print "The number is %d the number of steps was %d" % (number_, length)
	return length, number

x = 1
highwater = []
blank = []
name = raw_input("Name the new file: ")
start = theNumber("Starting number: ")
end = theNumber("Ending number: ")
i = start
while i < end:
	y, a = collatz(i)
	if x <= y:
		print "The number %d has length %d" % (a, y)
		x = y
	highwater.append(y)
	blank.append(i)
	i += 1
picklefile = open(name, 'w')
pickle.dump(highwater, picklefile)




